/* coding:utf-8
 * Copyright (C) dirlt
 */
#include "Common.h"
#include "tdigest.h"

int main() {
    DeferOp op([]() { printf("defer op ...\n"); });
    {
        starrocks::TDigest td;
        for (int i = 0; i < 20; i++) {
            td.add((float)i, 10);
        }
        printf("p90 = %.2f\n", td.quantile(0.9));
    }
    {
        starrocks::TDigest td;
        for (int i = 0; i < 100; i++) {
            td.add((float)i, 10);
        }
        printf("p90 = %.2f\n", td.quantile(0.9));
    }
    return 0;
}
