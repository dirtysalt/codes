DROP TABLE IF EXISTS event2;

CREATE EXTERNAL TABLE IF NOT EXISTS event2
PARTITIONED BY (
  `day` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
WITH SERDEPROPERTIES (
    'avro.schema.url'='hdfs://localhost:8020/user/dirlt/hive/schema/event2.avsc')
STORED as INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
  'hdfs://localhost:8020/user/dirlt/hive/tables/event2';
