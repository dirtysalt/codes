import org.apache.hadoop.hbase.client.{Put, Result, Scan}
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapreduce.{TableInputFormat, TableOutputFormat}
import org.apache.hadoop.hbase.protobuf.ProtobufUtil
import org.apache.hadoop.hbase.util.{Base64, Bytes}
import org.apache.hadoop.mapreduce.Job
import org.apache.spark.rdd.PairRDDFunctions
import org.apache.spark.{SparkConf, SparkContext}

/**
 * Created by dirlt on 9/11/15.
 */
object TestOnHBase {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
    conf.setAppName("test-on-hbase")
    conf.setMaster("local")

    val sc = new SparkContext(conf)
    val job = new Job(sc.hadoopConfiguration)
    job.setOutputKeyClass(classOf[ImmutableBytesWritable])
    job.setOutputValueClass(classOf[Result])
    job.setOutputFormatClass(classOf[TableOutputFormat[ImmutableBytesWritable]])
    job.getConfiguration.set(TableOutputFormat.OUTPUT_TABLE, "t1")

    implicit def strToBytes(s: String) = Bytes.toBytes(s)

    val rdd = sc.parallelize(Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3").toList, 3)
    val hbase_rdd = rdd.map(x => {
      val (k:String, v:String) = x
      val p = new Put(k)
      p.addImmutable("cf", "v", v)
      (new ImmutableBytesWritable(), p)
    })
    new PairRDDFunctions(hbase_rdd).saveAsNewAPIHadoopDataset(job.getConfiguration)

    job.getConfiguration.set(TableInputFormat.INPUT_TABLE, "t1")
    val scan = new Scan()
    scan.addColumn("cf", "v")
    val proto = ProtobufUtil.toScan(scan);
    val scan_string = Base64.encodeBytes(proto.toByteArray)
    job.getConfiguration.set(TableInputFormat.SCAN, scan_string)
    val rdd2 = sc.newAPIHadoopRDD(job.getConfiguration, classOf[TableInputFormat],
      classOf[ImmutableBytesWritable], classOf[Result])
    rdd2.map(x => {
      val k = x._1.asInstanceOf[ImmutableBytesWritable]
      val r = x._2.asInstanceOf[Result]
      val v = r.getValue("cf", "v")
      new String(k.get()) + ":" + new String(v)
    }).collect().foreach(println)
    sc.stop()

  }
}
