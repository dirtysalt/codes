/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <condition_variable>
#include <mutex>
#include "config.h"

#ifdef USE_MATHLIB
#include "MathLib/mathlib.h"
#else
int add(int x, int y) {
    printf("use native add\n");
    return x + y;
}
#endif

using namespace std;

int main(int argc, const char**argv) {
    // report version
    std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
              << Tutorial_VERSION_MINOR << std::endl;
    int z = add(10, 20);
    std::cout << "add(10, 20) = " << z <<std::endl;
    return 0;
}
