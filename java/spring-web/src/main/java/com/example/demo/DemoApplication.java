package com.example.demo;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.ApplicationContext;
import org.springframework.core.env.Environment;
import org.springframework.scheduling.annotation.EnableScheduling;

import java.util.Arrays;

@SpringBootApplication
@EnableScheduling
@EnableDiscoveryClient
public class DemoApplication implements CommandLineRunner {
    @Autowired
    Environment env;
    @Autowired
    ApplicationContext ctx;

    @Autowired
    MongoDBService mongodb;

    protected final Logger logger = LoggerFactory.getLogger(this.getClass());

    public static void main(String[] args) {
        System.setProperty("JM.SNAPSHOT.PATH", "/tmp/jm.snapshot/");
        SpringApplication.run(DemoApplication.class, args);
    }

    public void run(String[] args) {
        System.out.printf("[env]running on port %s\n", env.getProperty("server.port"));
        System.out.printf("[env]dynconf.name = %s, dynconf.age = %d\n", env.getProperty("dynconf.name"),
                Integer.parseInt(env.getProperty("dynconf.age")));

        System.out.println("Let's inspect the beans provided by Spring Boot:");

        String[] beanNames = ctx.getBeanDefinitionNames();
        Arrays.sort(beanNames);
        for (String beanName : beanNames) {
            System.out.println(beanName);
        }
    }
}
