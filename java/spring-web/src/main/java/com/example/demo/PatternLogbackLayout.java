package com.example.demo;


import ch.qos.logback.classic.PatternLayout;


public class PatternLogbackLayout extends PatternLayout {
    static {
        defaultConverterMap.put("traceId", TraceIdPatternConverter.class.getName());
    }
}
