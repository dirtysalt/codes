package com.example.demo;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RefreshScope
@RestController
public class DynConfigController {
    protected Logger logger = LoggerFactory.getLogger(this.getClass());

    @Value("${dynconf.name}")
    String name;
    @Value("${dynconf.age}")
    int age;

    @GetMapping("/dynconf")
    public String dynConf() {
        return String.format("dynconf. name = %s, age = %s", name, age);
    }
}
