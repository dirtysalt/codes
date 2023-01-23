package com.dirlt.java.scopedtimer;

import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;

public class TimingProcessor implements MethodInterceptor {
    public Object invoke(MethodInvocation invocation) throws Throwable {
        TimingScope x = (TimingScope) invocation.getMethod().getAnnotation(TimingScope.class);
        System.out.printf("TimingProcessor intercept with value = %s\n", x.value());
        return invocation.proceed();
    }
}
