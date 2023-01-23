package com.dirlt.java.mr;

import com.dirlt.java.mr.proto.MessageProtos1;
import com.twitter.elephantbird.mapreduce.output.LzoProtobufBlockOutputFormat;
import com.twitter.elephantbird.util.TypeRef;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 6:32 PM
 * To change this template use File | Settings | File Templates.
 */
public class MessageLzoProtobufOutputFormat extends LzoProtobufBlockOutputFormat<MessageProtos1.Message> {
    public MessageLzoProtobufOutputFormat() {
        super(new TypeRef<MessageProtos1.Message>() {
        });
    }
}
