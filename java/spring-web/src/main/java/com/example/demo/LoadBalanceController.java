package com.example.demo;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

//@RestController
public class LoadBalanceController {
    @Autowired
    private RestTemplate restTemplate;
    @Autowired
    private LoadBalancerClient lbClient;
    @Value("${spring.application.name}")
    private String appName;

    //实例化 RestTemplate 实例
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    protected Logger logger = LoggerFactory.getLogger(this.getClass());

    @GetMapping(value = "/lb/hello/{string}")
    public String lbHello(@PathVariable String string) {
        ServiceInstance inst = lbClient.choose(appName);
        String url = String.format("http://%s:%s/hello?name=%s", inst.getHost(), inst.getPort(), string);
        System.err.println("request url:" + url);
        return restTemplate.getForObject(url, String.class);
    }
}
