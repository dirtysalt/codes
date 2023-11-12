/* coding:utf-8
 * Copyright (C) dirlt
 */

// #include <condition_variable>
// #include <mutex>
// #include <thread>

#include <errno.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <vector>
using namespace std;

int main() {
    int fd = open("/tmp/test-file-channel.txt", O_RDWR);
    if (fd < 0) {
        fprintf(stderr, "open file failed: %s\n", strerror(errno));
        return -1;
    }
    void* addr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (addr == NULL) {
        fprintf(stderr, "mmap failed: %s\n", strerror(errno));
        return -1;
    }
    fprintf(stderr, "addr = %p\n", addr);
    char* p = (char*)addr;
    fprintf(stderr, "content = %s\n", p);
    p[0] = '!';

    int ret = munmap(addr, 4096);
    if (ret != 0) {
        fprintf(stderr, "munmap failed: %s\n", strerror(errno));
        return -1;
    }
    close(fd);
    return 0;
}
