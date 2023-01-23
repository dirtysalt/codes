package com.dirlt.java.scopedtimer;

import com.google.inject.AbstractModule;
import com.google.inject.matcher.Matchers;

public class TimingModule extends AbstractModule {
    protected void configure() {
        bindInterceptor(Matchers.any(), Matchers.annotatedWith(TimingScope.class),
                new TimingProcessor());
    }
}
