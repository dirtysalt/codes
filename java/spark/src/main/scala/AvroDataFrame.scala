import java.io.File

import com.databricks.spark.avro._
import org.apache.commons.io.FileUtils
import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}

/**
 * Created by dirlt on 9/6/15.
 */
object AvroDataFrame {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
    conf.setAppName("avro-df")
    conf.setMaster("local")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)

    // 读取本地文件
    // 载入非常容易. 在数据上查询非常方便.
    val df = sqlContext.read.avro("events1.avro")
    // directory works too.
    // val df = sqlContext.read.avro("hdfs://localhost:8020/events1.avro")
    df.show()
    df.printSchema()

    // 但是写回有点麻烦, 需要显示指明schema. 对嵌套层次结构数据不太有利
    // 虽然也可以按照avro格式写回, 但是仅限于单层结构.
    import sqlContext.implicits._
    val df2 = df.filter("id = 12345").map(x => x.getAs[String]("id") + "!!!").toDF("new_id")
    df2.show()
    df2.printSchema()
    val path = "/tmp/events1-avro-output"
    FileUtils.deleteDirectory(new File(path))
    df2.write.avro(path)
    val path2 = "/tmp/events1-parquet-output"
    FileUtils.deleteDirectory(new File(path2))
    df2.write.parquet(path2)
    sc.stop()
  }
}
