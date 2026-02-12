/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <atomic>
#include <cstdio>
#include <cstring>
#include <memory>
#include <mutex>
#include <random>
#include <string>
#include <thread>
#include <vector>

static size_t NWORKERS = 16;
static size_t BLOCK_SIZE = 1024 * 1024 * 16;
static size_t REPEAT = 1000;
static size_t NDESTS = 16;
static size_t NSOURCES = 16;
static bool NOFREE = false;
int main(int argc, const char* argv[]) {
    int i = 1;
    for (; i < argc; i++) {
        std::string opt = argv[i];
        if (opt == "-W") {
            NWORKERS = std::atoi(argv[++i]);
        } else if (opt == "-B") {
            std::string arg = argv[++i];
            int ratio = 1;
            char unit = arg[arg.size() - 1];
            if (unit == 'M') {
                ratio = 1024 * 1024;
            } else if (unit == 'K') {
                ratio = 1024;
            } else {
                arg += 'B';
            }
            BLOCK_SIZE = std::atoi(arg.substr(0, arg.size() - 1).c_str()) * ratio;
        } else if (opt == "-R") {
            REPEAT = std::atoi(argv[++i]);
        } else if (opt == "--nofree") {
            NOFREE = true;
        } else {
            //;
        }
    }
    printf("%s -W %zu -B %zuB -R %zu %s\n", argv[0], NWORKERS, BLOCK_SIZE, REPEAT, NOFREE ? "--nofree" : "");

    uint8_t* sources[NSOURCES];
    std::thread workers[NWORKERS];

    for (int i = 0; i < NSOURCES; i++) {
        sources[i] = (uint8_t*)malloc(BLOCK_SIZE);
        int value = i & 0xff;
        memset(sources[i], value, BLOCK_SIZE);
    }

    for (int i = 0; i < NWORKERS; i++) {
        auto f = [&](int tid) {
            std::mt19937 gen(tid);

            uint8_t* working_buffers[NDESTS];
            memset(working_buffers, 0x0, sizeof(working_buffers));

            for (size_t j = 0; j < REPEAT; j++) {
                int dst = gen() % NDESTS;
                int src = gen() % NSOURCES;
                if (NOFREE) {
                    // lsb == 0x1 as freed.
                    if ((uint64_t)working_buffers[src] & 0x1) {
                        uint64_t* p = (uint64_t*)(working_buffers + src);
                        *p = (*p) | ~0x1;
                        memcpy(working_buffers[src], sources[src], BLOCK_SIZE);
                    } else {
                        uint64_t* p = (uint64_t*)(working_buffers + src);
                        *p = (*p) | 0x1;
                    }
                } else {
                    if (working_buffers[src] == nullptr) {
                        working_buffers[src] = (uint8_t*)malloc(BLOCK_SIZE);
                        memcpy(working_buffers[src], sources[src], BLOCK_SIZE);
                    } else {
                        free(working_buffers[src]);
                        working_buffers[src] = nullptr;
                    }
                }
            }
        };
        workers[i] = std::thread(f, i);
    }

    for (int i = 0; i < NWORKERS; i++) {
        workers[i].join();
    }
    return 0;
}