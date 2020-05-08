package com.example.demo;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;

@Service
public class MongoDBService {
    @Value("${mongodb.uri}")
    private String uri;

    private MongoClient client;
    protected static final Logger logger = LoggerFactory.getLogger(DemoApplication.class);

    @PostConstruct
    public void init() {
        logger.debug("mongodb uri = " + uri);
        client = MongoClients.create(uri);
    }

    public MongoDatabase getDatabase(String db) {
        return client.getDatabase(db);
    }
}
