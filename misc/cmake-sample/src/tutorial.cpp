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

using namespace std;

int main(int argc, const char**argv) {
    // report version
    std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
              << Tutorial_VERSION_MINOR << std::endl;
    return 0;
}
