package com.dirlt.java.netty;

import org.jboss.netty.bootstrap.ServerBootstrap;
import org.jboss.netty.buffer.ChannelBuffer;
import org.jboss.netty.buffer.ChannelBuffers;
import org.jboss.netty.channel.*;
import org.jboss.netty.channel.socket.nio.NioServerSocketChannelFactory;
import org.jboss.netty.handler.codec.http.*;

import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.Executors;

public class SimpleHTTPServer {
    public static class Metric {
        private Map<String, Long> counter = new HashMap<String, Long>();
        private Map<String, String> status = new HashMap<String, String>();
        private static Metric instance = new Metric();

        public static Metric getInstance() {
            return instance;
        }

        public void addCounter(String name, long value) {
            synchronized (counter) {
                if (counter.containsKey(name)) {
                    counter.put(name, counter.get(name) + value);
                } else {
                    counter.put(name, value);
                }
            }
        }

        public long getCounter(String name) {
            synchronized (counter) {
                if (!counter.containsKey(name)) {
                    return 0L;
                } else {
                    return counter.get(name);
                }
            }
        }

        public void updateStatus(String name, String value) {
            synchronized (status) {
                status.put(name, value);
            }
        }

        public void getStatus(String name) {
            synchronized (status) {
                status.get(name);
            }
        }

        public String toString() {
            StringBuffer sb = new StringBuffer();
            sb.append("----------counter----------\n");
            synchronized (counter) {
                Set<Map.Entry<String, Long>> entries = counter.entrySet();
                for (Map.Entry<String, Long> entry : entries) {
                    sb.append(String.format("%s = %s\n", entry.getKey(), entry.getValue().toString()));
                }
            }
            sb.append("----------status----------\n");
            synchronized (status) {
                Set<Map.Entry<String, String>> entries = status.entrySet();
                for (Map.Entry<String, String> entry : entries) {
                    sb.append(String.format("%s = %s\n", entry.getKey(), entry.getValue()));
                }
            }
            return sb.toString();
        }
    }

    public static class MetricHandler extends SimpleChannelHandler {
        @Override
        public void messageReceived(ChannelHandlerContext ctx, MessageEvent e) {
            Metric metric = Metric.getInstance();
            Channel channel = e.getChannel();
            HttpResponse response = new DefaultHttpResponse(
                    HttpVersion.HTTP_1_1, HttpResponseStatus.OK);
            String content = metric.toString();
            response.setHeader("Content-Length", content.length());
            ChannelBuffer buffer = ChannelBuffers.buffer(content.length());
            buffer.writeBytes(content.getBytes());
            response.setContent(buffer);
            channel.write(response);
        }

        @Override
        public void channelClosed(ChannelHandlerContext ctx, ChannelStateEvent e) {
            ctx.getChannel().close();
        }
    }

    public static class HttpHandler extends SimpleChannelHandler {
        // initialize a handler every time!WTF.
        // only when the channel is closed.
        {
            System.out.println("do init...");
        }

        @Override
        public void messageReceived(ChannelHandlerContext ctx, MessageEvent e) {
            Metric metric = Metric.getInstance();
            metric.addCounter("rpc-count", 1);
            Metric.getInstance().updateStatus(
                    "session#" + ctx.getChannel().getId().toString(),
                    "handling");

            System.out.printf("===session===\n");
            HttpRequest request = (HttpRequest) e.getMessage();
            System.out.println("method = " + request.getMethod());
            System.out.println("uri = " + request.getUri());
            System.out.println("-->header<--");
            for (String key : request.getHeaderNames()) {
                System.out.printf("%s = %s\n", key, request.getHeader(key));
            }

            Channel channel = e.getChannel();
            HttpResponse response = new DefaultHttpResponse(
                    HttpVersion.HTTP_1_1, HttpResponseStatus.OK);
            // we have to use Content-Length here. WTF.
            String content = "Hello,World";
            response.setHeader("Content-Length", content.length());
            ChannelBuffer buffer = ChannelBuffers.buffer(content.length());
            buffer.writeBytes(content.getBytes());
            response.setContent(buffer);
            channel.write(response);
        }

        @Override
        public void writeComplete(ChannelHandlerContext ctx,
                                  WriteCompletionEvent e) {
            Metric.getInstance()
                    .updateStatus(
                            "session#" + ctx.getChannel().getId().toString(),
                            "handled");
            System.out.println("handled");
            // long-lived connection.
            // e.getChannel().close();
        }

        @Override
        public void channelOpen(ChannelHandlerContext ctx, ChannelStateEvent e) {
            System.out.println("accepted");
            Metric.getInstance().updateStatus(
                    "session#" + ctx.getChannel().getId().toString(), "open");
        }

        @Override
        public void channelClosed(ChannelHandlerContext ctx, ChannelStateEvent e) {
            System.out.println("closed");
            Metric.getInstance().updateStatus(
                    "session#" + ctx.getChannel().getId().toString(), "closed");
            ctx.getChannel().close();
        }
    }

    public static void runHttpServer() {
        ChannelFactory factory = new NioServerSocketChannelFactory(
                Executors.newFixedThreadPool(4), // boss
                Executors.newFixedThreadPool(16) // worker. must be >=2 * CPU
                // cores.
        );
        ServerBootstrap bootstrap = new ServerBootstrap(factory);
        bootstrap.setPipelineFactory(new ChannelPipelineFactory() {
            public ChannelPipeline getPipeline() throws Exception {
                ChannelPipeline pipeline = Channels.pipeline();
                pipeline.addLast("decoder", new HttpRequestDecoder());
                pipeline.addLast("encoder", new HttpResponseEncoder());
                pipeline.addLast("handler", new HttpHandler());
                return pipeline;
            }
        });
        bootstrap.bind(new InetSocketAddress(8001));
    }

    public static void runMetricServer() {
        ChannelFactory factory = new NioServerSocketChannelFactory(
                Executors.newFixedThreadPool(4), // boss
                Executors.newFixedThreadPool(16) // worker. must be >=2 * CPU
                // cores.
        );
        ServerBootstrap bootstrap = new ServerBootstrap(factory);
        bootstrap.setPipelineFactory(new ChannelPipelineFactory() {
            public ChannelPipeline getPipeline() throws Exception {
                ChannelPipeline pipeline = Channels.pipeline();
                pipeline.addLast("decoder", new HttpRequestDecoder());
                pipeline.addLast("encoder", new HttpResponseEncoder());
                pipeline.addLast("handler", new MetricHandler());
                return pipeline;
            }
        });
        bootstrap.bind(new InetSocketAddress(8002));
    }

    public static void main(String[] args) {
        runHttpServer();
        runMetricServer();
    }
}
