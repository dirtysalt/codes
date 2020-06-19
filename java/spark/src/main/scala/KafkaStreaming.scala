import org.apache.spark.SparkConf
import org.apache.spark.streaming.kafka.KafkaUtils
import org.apache.spark.streaming.{Seconds, StreamingContext}

/**
 * Created by dirlt on 8/28/15.
 */
object KafkaStreaming {
  def main(args: Array[String]) {
    val Array(zkHosts, topics) = args

    // Create context with 2 second batch interval
    val sparkConf = new SparkConf().setAppName("kafka-streaming")
    val ssc = new StreamingContext(sparkConf, Seconds(2))
    // val chkPath = "/tmp/checkpoint"
    // ssc.checkpoint(chkPath)

    // 4 threads to read this topic. consumer groups id as "client-ssc"
    // not exactly-once delivery.
    val topicMap = topics.split(",").map((_, 4)).toMap
    val lines = KafkaUtils.createStream(ssc, zkHosts, "client-ssc", topicMap).map(_._2)
    lines.print()

    // Start the computation
    ssc.start()
    ssc.awaitTermination()
  }
}
