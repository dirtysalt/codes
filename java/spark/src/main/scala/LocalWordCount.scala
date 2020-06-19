import org.apache.spark.{SparkConf, SparkContext}

object LocalWordCount {
  def main(args: Array[String]) {
    val passwdFile = "/etc/passwd";
    val conf = new SparkConf().setAppName("local-wc")
    conf.setMaster("local")
    val sc = new SparkContext(conf)
    val data = sc.textFile(passwdFile, 2)
    val wcs = data.flatMap(x => x.split("[:, ]")).map(x => (x.toLowerCase, 1)).reduceByKey((a, b) => a + b).collect()
    println("word count on " + passwdFile)
    wcs.foreach(println)
    sc.stop()
  }
}