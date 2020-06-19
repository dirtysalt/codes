import com.dirlt.avro.Event
import org.apache.avro.mapred._
import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.hadoop.io.NullWritable
import org.apache.spark.api.java.JavaPairRDD
import org.apache.spark.{SparkConf, SparkContext}

/**
 * Created by dirlt on 9/6/15.
 */
object AvroRawRDD {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
    conf.setAppName("avro-rdd")
    conf.setMaster("local")
    val sc = new SparkContext(conf)
    // sc.hadoopConfiguration.set("fs.default.name", "hdfs://localhost:8020")
    val path = "/tmp/events1.avro"
    val rdd = sc.hadoopFile(path, classOf[AvroInputFormat[Event]], classOf[AvroWrapper[Event]], classOf[NullWritable])
    rdd.map (x => {
      val event = x._1.datum()
      event.toString
    }).foreach(println)
    val output = rdd.map (x => {
      val event = x._1.datum()
      val builder = Event.newBuilder(event)
      builder.setEvent(event.getEvent + "!!!")
      (new AvroWrapper(builder.build()), NullWritable.get())
    })
    output.map(_._1.toString).collect().foreach(println)
    val output2 = JavaPairRDD.fromRDD[AvroWrapper[Event], NullWritable](output)
    val outputPath = "/tmp/events1-avro-output"
    FileSystem.get(sc.hadoopConfiguration).delete(new Path(outputPath))

    sc.hadoopConfiguration.set("avro.output.schema",Event.getClassSchema.toString)
    output2.saveAsHadoopFile(outputPath, classOf[AvroWrapper[Event]], classOf[NullWritable], classOf[AvroOutputFormat[Event]])

    // validate.
    val rdd2 = sc.hadoopFile(outputPath, classOf[AvroInputFormat[Event]], classOf[AvroWrapper[Event]], classOf[NullWritable])
    val rdd22 = rdd2.map(_._1.datum().getEvent.toString).collect()
    rdd22.foreach(x => {
      val len = x.length()
      assert(x.substring(len - 3) == "!!!")
    })
    sc.stop()
  }
}
