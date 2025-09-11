/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"

int main() {
    perf_init();
    struct perf_count counts;
    disable_perf_count();
    reset_perf_count();
    enable_perf_count();

    constexpr int arraySize = 4 * 1024;
    constexpr int N = 10000000;
    int data[arraySize];
    memset(data, 0x77, arraySize);
    size_t chksum = 0x7f7f7f7f;
    for (int i = 0; i < N; i++) {
        long sum = 0;
        for (int j = 0; j < arraySize; j++) {
            sum += data[j];
        }
        chksum = chksum ^ sum;
        chksum = chksum ^ (long)i;
    }
    printf("checksum = %zu\n", chksum);

    disable_perf_count();
    read_perf_count(&counts);

    int iterations = N;
    int num = arraySize;

    printf("perf stats: %6.2f cycles/elem, %6.2f instrs/elem, %5.2f instrs/cycle, %5.2f branches/elem, "
           "%5.2f%% branch misses, %5.2f%% cache misses, %5.2fGHz",
           ((double)counts.cycles) / ((double)iterations) / ((double)num),
           ((double)counts.instructions) / ((double)iterations) / ((double)num),
           ((double)counts.instructions) / ((double)counts.cycles),
           ((double)counts.branch_instructions) / ((double)iterations) / ((double)num),
           100.0 * ((double)counts.branch_misses) / ((double)counts.branch_instructions),
           100.0 * ((double)counts.cache_misses) / ((double)counts.cache_references),
           ((double)counts.cycles) / counts.seconds / 1000000000.0);
    perf_close();
}