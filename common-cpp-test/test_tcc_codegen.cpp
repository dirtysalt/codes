/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"
#include "libtcc.h"

using namespace std;

const char* TEXT = R"START(
int add(int x, int y) {
if (x > 10) {
return x + y;
} else {
return x + y - 20;
}
}
)START";

typedef int (*add_function_t)(int x, int y);

add_function_t run() {
    TCCState* tcc = tcc_new();
    int code = tcc_set_output_type(tcc, TCC_OUTPUT_MEMORY);
    if (code == -1) {
        printf("set output type failed\n");
        return 0;
    }

    code = tcc_compile_string(tcc, TEXT);
    if (code == -1) {
        printf("not good program\n");
        return 0;
    }
    // tcc_add_library(tcc, "c");
    int size = tcc_relocate(tcc, NULL);
    void* mem = malloc(size);
    code = tcc_relocate(tcc, mem);
    if (code == -1) {
        printf("relocate failed\n");
    }
    add_function_t f = (add_function_t)(tcc_get_symbol(tcc, "add"));
    if (f == 0) {
        printf("symbol not found\n");
        return 0;
    }

    tcc_delete(tcc);
    return f;
}

int main() {
    std::vector<add_function_t> ptrs;

    const int N = 1000;
    Timer t;
    t.start();
    for (int j = 0; j < N; j++) {
        ptrs.clear();
        for (int i = 0; i < 10; i++) {
            add_function_t f = run();
            if (f == nullptr) return 0;
            ptrs.push_back(f);
        }
        if (j == (N - 1)) {
            for (add_function_t f : ptrs) {
                printf("%d\n", f(1, 2));
            }
        }
    }
    t.stop();
    std::cout << "time = " << t.elapsedMilliseconds() << "ms" << std::endl;
    return 0;
}
