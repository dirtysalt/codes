package com.dirlt.java.finagle;

import java.net.InetSocketAddress;
import java.nio.ByteOrder;

import org.jboss.netty.buffer.ChannelBuffer;
import org.jboss.netty.buffer.ChannelBuffers;
import org.jboss.netty.handler.codec.http.DefaultHttpResponse;
import org.jboss.netty.handler.codec.http.HttpRequest;
import org.jboss.netty.handler.codec.http.HttpResponse;
import org.jboss.netty.handler.codec.http.HttpResponseStatus;
import org.jboss.netty.handler.codec.http.HttpVersion;

import com.twitter.finagle.Service;
import com.twitter.finagle.builder.ServerBuilder;
import com.twitter.finagle.http.Http;
import com.twitter.util.Future;

public class SimpleHTTPServer {
	public static void main(String[] args) {
		Service<HttpRequest, HttpResponse> service = new Service<HttpRequest, HttpResponse>() {
			public Future<HttpResponse> apply(HttpRequest request) {
				HttpResponse res = new DefaultHttpResponse(
						HttpVersion.HTTP_1_1, HttpResponseStatus.OK);
				ChannelBuffer cbuf = ChannelBuffers.buffer(
						ByteOrder.BIG_ENDIAN, 1024);
				cbuf.writeBytes("Hello,World".getBytes());
				res.setContent(cbuf);	
				return Future.value(res);
			}
		};
		ServerBuilder.safeBuild(service,
				ServerBuilder.get().codec(Http.get()).name("HttpServer")
						.bindTo(new InetSocketAddress("localhost", 8001)));

	}
}
