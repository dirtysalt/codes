package main

import java.util

import backtype.storm.StormSubmitter
import backtype.storm.topology.{BasicOutputCollector, TopologyBuilder}
import backtype.storm.topology.base.BaseBasicBolt
import backtype.storm.tuple.Tuple
import storm.kafka.{ZkHosts, SpoutConfig, KafkaSpout}

/**
 * Created by dirlt on 3/30/15.
 */

// https://github.com/apache/storm/tree/master/external/storm-kafka
class SplitBolt extends BaseBasicBolt {
  override def execute(tuple: Tuple, collector: BasicOutputCollector): Unit = {
    val s = new String(tuple.getBinaryByField("bytes"))
    collector.emit(new Values(s, "***" + s))
  }

  override def declareOutputFields(declarer: OutputFieldsDeclarer): Unit = {
    // output 2 copies.
    declarer.declare(new Fields("word-0", "word-1"))
  }
}

class Echo0Bolt extends BaseBasicBolt {
  override def execute(tuple: Tuple, collector: BasicOutputCollector): Unit = {
    val s = tuple.getString(0)
    println("tuple size = " + tuple.size() + ", output by echo0bolt: " + s)
    collector.emit(new Values(s))
  }

  override def declareOutputFields(declarer: OutputFieldsDeclarer): Unit = {
    declarer.declare(new Fields("output0"))
  }
}

class Echo1Bolt extends BaseBasicBolt {
  override def execute(tuple: Tuple, collector: BasicOutputCollector): Unit = {
    val s = tuple.getString(1)
    println("tuple size = " + tuple.size() + ", output by echo1bolt: " + s)
    collector.emit(new Values(s))
  }

  override def declareOutputFields(declarer: OutputFieldsDeclarer): Unit = {
    declarer.declare(new Fields("output1"))
  }
}

class Echo2Bolt(val script: String) extends ShellBolt("python", script) with IRichBolt {
  override def declareOutputFields(declarer: OutputFieldsDeclarer): Unit = {
    declarer.declare(new Fields("output2"))
  }

  override def getComponentConfiguration: util.Map[String, AnyRef] = null
}

object DemoTopology {
  def main(args: Array[String]) {
    val zkHosts = new ZkHosts("127.0.0.1:2181") // zookeeper hosts
    val topicName = "test-ws"
    val zkRoot = "/kafka-spout"
    val zkSpoutId = "client0" // unique spout id.
    val spoutConfig = new SpoutConfig(zkHosts, topicName, zkRoot, zkSpoutId);
    // see storm-kafka's README for more options.
    // spoutConfig.forceFromStart = true
    val spout = new KafkaSpout(spoutConfig)

    val builder: TopologyBuilder = new TopologyBuilder
    builder.setSpout("spout", spout, 1)
    builder.setBolt("split", new SplitBolt, 1).shuffleGrouping("spout")
    builder.setBolt("echo-0", new Echo0Bolt, 1).fieldsGrouping("split", new Fields("word-0"))
    builder.setBolt("echo-1", new Echo1Bolt, 1).fieldsGrouping("split", new Fields("word-1"))
    builder.setBolt("echo-2", new Echo2Bolt("echo.py")).fieldsGrouping("split", new Fields("word-0", "word-1"))

    val conf: Config = new Config
    conf.setDebug(false)
    conf.setNumWorkers(1) // use how many workers.

    val name = "demo" // topology name
    val remote = (args.length != 0) // you need to provide args to force run remotely
    if (!remote) {
      // run locally
      conf.setMaxTaskParallelism(2);
      val cluster: LocalCluster = new LocalCluster
      cluster.submitTopology(name, conf, builder.createTopology)
      // wait 300 seconds
      Thread.sleep(300 * 1000)
      cluster.shutdown
    } else {
      // push to remote.
      StormSubmitter.submitTopology(name, conf, builder.createTopology)
    }
  }
}
