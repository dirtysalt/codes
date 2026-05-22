/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <assert.h>
#include <math.h>
#include <stdio.h>

union Value {
    struct Float {
        unsigned int base : 23;
        unsigned int exp : 8;
        unsigned int sign : 1;
    } p;
    float f;
    unsigned int i;
};

long _pow2(unsigned int x) {
    long res = 1;
    long base = 2;
    while (x) {
        if (x & 0x1) res *= base;
        base = base * base;
        x = x >> 1;
    }
    return res;
}
float pow2(int x) {
    unsigned int _x = x;
    if (x < 0) _x = -x;
    long res = _pow2(_x);
    if (x < 0)
        return 1.0f / res;
    else
        return 1.0f * res;
}

void testSyn(float f) {
    union Value value;
    value.f = f;
    printf("=============testSyn==============\n");
    printf("float = %.6f, int = %d, parts = (%d,%d,%d)\n", value.f, value.i, value.p.sign, value.p.exp, value.p.base);
    float res = 0.0f;
    if (!(value.p.exp == 0 && value.p.base == 0)) {
        float base = 1 + value.p.base * 1.0f / (1 << 23);
        float exp = pow2((int)value.p.exp - 0x7f);
        printf("syn base = %.6f, exp = %.6f\n", base, exp);
        res = base * exp;
        if (value.p.sign) res = -res;
    }
    printf("syn result = %.6f\n", res);
    assert(fabs(res - f) < 1e-6);
}

void testOp(float f) {
    printf("==========testOp==========\n");
    union Value value;
    value.f = f;
    // flip sign bit.
    value.i = value.i ^ 0x80000000;
    assert(fabs(value.f + f) < 1e-6);

    // multiple 4
    const int scale = 2;
    value.f = f;
    value.i = value.i + scale * (1 << 23);
    assert(fabs(value.f - (1 << scale) * f) < 1e-6);
}

/*
        .loc 1 72 0
        movl	$-1, -36(%rbp)
        .loc 1 73 0
        movl	-36(%rbp), %eax
        movl	%eax, %edx
        shrl	$31, %edx
        addl	%edx, %eax
        sarl	%eax
        movl	%eax, -36(%rbp)
*/

int main() {
    volatile int x = -3;
    x = x / 2;
    printf("%d\n", x);
    float data[] = {0.15625f, 15622.76f, 0.0f};
    unsigned int size = sizeof(data) / sizeof(data[0]);
    for (unsigned int i = 0; i < size; i++) {
        float f = data[i];
        testSyn(f);
        testSyn(-f);
        testOp(f);
    }
    return 0;
}
