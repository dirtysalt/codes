DROP TABLE IF EXISTS event1;

CREATE EXTERNAL TABLE IF NOT EXISTS event1
PARTITIONED BY (
  `day` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
WITH SERDEPROPERTIES (
    'avro.schema.url'='hdfs://localhost:8020/user/dirlt/hive/schema/event1.avsc')
STORED as INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
  'hdfs://localhost:8020/user/dirlt/hive/tables/event1';
