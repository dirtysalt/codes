package com.dirlt.java.mr2;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableRecordReader;
import org.apache.hadoop.hbase.mapreduce.TableSplit;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.hbase.util.Pair;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;

import javax.security.auth.login.Configuration;
import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 1/5/13
 * Time: 2:18 PM
 * To change this template use File | Settings | File Templates.
 */
public class MultipleTableInputFormat extends InputFormat<ImmutableBytesWritable, Result> {
    private static final String kSeparator = "!";
    private static String hexString = "0123456789ABCDEF";

    private static String encode(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * 2);
        for (int i = 0; i < bytes.length; i++) {
            sb.append(hexString.charAt((bytes[i] & 0xf0) >> 4));
            sb.append(hexString.charAt((bytes[i] & 0x0f) >> 0));
        }
        return sb.toString();
    }

    private static byte[] decode(String bytes) {
        ByteArrayOutputStream bos = new ByteArrayOutputStream(bytes.length() / 2);
        for (int i = 0; i < bytes.length(); i += 2)
            bos.write((hexString.indexOf(bytes.charAt(i)) << 4 | hexString.indexOf(bytes.charAt(i + 1))));
        return bos.toByteArray();
    }

    public static String convertScanToString(Scan scan) throws IOException {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        DataOutputStream dos = new DataOutputStream(out);
        scan.write(dos);
        return encode(out.toByteArray());
    }

    public static String convertTableInputToString(String tableName, Scan... scans) throws IOException {
        StringBuffer sb = new StringBuffer();
        sb.append(tableName);
        for (Scan scan : scans) {
            sb.append(kSeparator);
            sb.append(convertScanToString(scan));
        }
        return sb.toString();
    }

    public static Scan convertStringToScan(String base64) throws IOException {
        ByteArrayInputStream bis = new ByteArrayInputStream(decode(base64));
        DataInputStream dis = new DataInputStream(bis);
        Scan scan = new Scan();
        scan.readFields(dis);
        return scan;
    }

    public static Object[] convertStringToTableInput(String s) throws IOException {
        String[] ss = s.split(kSeparator);
        Object[] objects = new Object[ss.length];
        objects[0] = ss[0]; // table name.
        for (int i = 1; i < ss.length; i++) {
            objects[i] = convertStringToScan(ss[i]);
        }
        return objects;
    }

    // ReflectionUtils.newInstance will call it.
    public void setConf(Configuration configuration) {
    }

    public Configuration getConf() {
        return null;
    }

    @Override
    public List<InputSplit> getSplits(JobContext context) throws IOException {
        List<InputSplit> rs = new LinkedList<InputSplit>();
        Path[] paths = FileInputFormat.getInputPaths(context);
        for (Path path : paths) {
            // actually it's not a real path. we just want to use Path object to hold the info.
            String s = path.toString().substring(path.getParent().toString().length() + 1);
            Object[] objects = convertStringToTableInput(s);
            String tableName = (String) objects[0];
            HTable table = new HTable(context.getConfiguration(), tableName);
            for (int i = 1; i < objects.length; i++) {
                Scan scan = (Scan) objects[i];
                List<InputSplit> inputSplits = getSplitsEachScan(table, scan, context);
                rs.addAll(inputSplits);
            }
            table.close();
        }
        return rs;
    }

    protected boolean includeRegionInSplit(final byte[] startKey, final byte[] endKey) {
        return true;
    }

    // we just want to hold the scan object.
    public static class MultipleTableSplit extends TableSplit {
        private Scan scan = null;

        public MultipleTableSplit() {
            this.scan = new Scan();
        }

        public MultipleTableSplit(byte[] tableName, byte[] start, byte[] end, final String regionLocation, Scan scan) {
            super(tableName, start, end, regionLocation);
            this.scan = scan;
        }

        public Scan getScan() {
            return scan;
        }

        @Override
        public void readFields(DataInput in) throws IOException {
            super.readFields(in);
            scan.readFields(in);
        }

        @Override
        public void write(DataOutput out) throws IOException {
            super.write(out);
            scan.write(out);
        }

    }

    public List<InputSplit> getSplitsEachScan(HTable table, Scan scan, JobContext context) throws IOException {
        Pair<byte[][], byte[][]> keys = table.getStartEndKeys();
        if (keys == null || keys.getFirst() == null ||
                keys.getFirst().length == 0) {
            throw new IOException("Expecting at least one region.");
        }
        List<InputSplit> splits = new ArrayList<InputSplit>(keys.getFirst().length);
        for (int i = 0; i < keys.getFirst().length; i++) {
            if (!includeRegionInSplit(keys.getFirst()[i], keys.getSecond()[i])) {
                continue;
            }
            String regionLocation = table.getRegionLocation(keys.getFirst()[i]).
                    getServerAddress().getHostname();
            byte[] startRow = scan.getStartRow();
            byte[] stopRow = scan.getStopRow();
            // determine if the given start an stop key fall into the region
            if ((startRow.length == 0 || keys.getSecond()[i].length == 0 ||
                    Bytes.compareTo(startRow, keys.getSecond()[i]) < 0) &&
                    (stopRow.length == 0 ||
                            Bytes.compareTo(stopRow, keys.getFirst()[i]) > 0)) {
                byte[] splitStart = startRow.length == 0 ||
                        Bytes.compareTo(keys.getFirst()[i], startRow) >= 0 ?
                        keys.getFirst()[i] : startRow;
                byte[] splitStop = (stopRow.length == 0 ||
                        Bytes.compareTo(keys.getSecond()[i], stopRow) <= 0) &&
                        keys.getSecond()[i].length > 0 ?
                        keys.getSecond()[i] : stopRow;
                InputSplit split = new MultipleTableSplit(table.getTableName(),
                        splitStart, splitStop, regionLocation, scan);
                splits.add(split);
            }
        }
        return splits;
    }

    @Override
    public RecordReader<ImmutableBytesWritable, Result> createRecordReader(
            InputSplit split, TaskAttemptContext context)
            throws IOException {
        MultipleTableSplit tSplit = (MultipleTableSplit) split;
        TableRecordReader trr = new TableRecordReader();
        Scan sc = new Scan(tSplit.getScan());
        sc.setStartRow(tSplit.getStartRow());
        sc.setStopRow(tSplit.getEndRow());
        trr.setScan(sc);
        trr.setHTable(new HTable(context.getConfiguration(), tSplit.getTableName()));
        try {
            trr.initialize(tSplit, context);
        } catch (InterruptedException e) {
            throw new InterruptedIOException(e.getMessage());
        }
        return trr;
    }
}
