/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <stdio.h>
#include "mathlib.h"
#include "primes.h"

#if defined(HAVE_LOG) && defined(HAVE_EXP)
#include <math.h>
double mylog(double x) {
    return log(x);
}
double myexp(double x) {
    return exp(x);
}
#else
double mylog(double x) {
    printf("'mylog' not implemented\n");
    return -1.0;
}
double myexp(double x) {
    printf("'myexp' not implemented\n");
    return -1.0;
}
#endif

int add(int x, int y)  {
    printf("use library add\n");
    return x + y;
}

int isPrime(int x) {
    return _primes[x];
}
