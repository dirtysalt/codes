package com.example.utils;

import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.codecs.pojo.PojoCodecProvider;
import org.bson.types.ObjectId;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.bson.codecs.configuration.CodecRegistries.fromProviders;
import static org.bson.codecs.configuration.CodecRegistries.fromRegistries;

public class MongoDBPlayer {
    public static void main(String[] args) {
        Logger logger = LoggerFactory.getLogger("");

        CodecRegistry pojoCodecRegistry = fromRegistries(MongoClientSettings.getDefaultCodecRegistry(),
                fromProviders(PojoCodecProvider.builder().automatic(true).build()));
        MongoClientSettings settings = MongoClientSettings.builder()
                .codecRegistry(pojoCodecRegistry)
                .build();
        MongoClient mongoClient = MongoClients.create(settings);

        MongoDatabase db = mongoClient.getDatabase("test");
        MongoCollection<Document> coll = db.getCollection("spring");
        coll.deleteMany(new Document());
        MongoCollection<PeopleModel> coll2 = db.getCollection("spring", PeopleModel.class);

        String[] names = {"yan", "mike", "hanson"};
        int[] ages = {10, 20, 30};
        for (int i = 0; i < names.length; i++) {
            PeopleModel p = new PeopleModel();
            p.setName(names[i]);
            p.setAge(ages[i]);
            coll2.insertOne(p);
        }

        Document doc = coll.find().first();
        if (doc != null) {
            logger.info(doc.toJson());
            ObjectId oid = doc.getObjectId("_id");
            logger.info(oid.toString());
            logger.info(oid.getDate().toString());
        }

        for (PeopleModel p : coll2.find()) {
            logger.info("people. id = {}, name = {}, age = {}",
                    p.getId(), p.getName(), p.getAge());
        }
    }
}
