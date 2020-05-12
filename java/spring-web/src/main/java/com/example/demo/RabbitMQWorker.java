package com.example.demo;

import org.springframework.stereotype.Component;

@Component
public class RabbitMQWorker {

    public void receiveMessage(byte[] message) {
        String s = new String(message);
        System.out.println("Received: <" + s + ">");
    }
}
