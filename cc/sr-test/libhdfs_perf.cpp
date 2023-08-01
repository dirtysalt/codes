/* coding:utf-8
 * Copyright (C) dirlt
 */

#ifdef LIBHDFS3
#include <hdfs3/hdfs.h>
#else
#include <hdfs/hdfs.h>
#endif

#include <unistd.h>

#include <algorithm>
#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <thread>
#include <vector>

class Timer {
public:
    void start() {
        m_StartTime = std::chrono::system_clock::now();
        m_bRunning = true;
    }

    void stop() {
        m_EndTime = std::chrono::system_clock::now();
        m_bRunning = false;
    }

    long long elapsedMilliseconds() {
        std::chrono::time_point<std::chrono::system_clock> endTime;

        if (m_bRunning) {
            endTime = std::chrono::system_clock::now();
        } else {
            endTime = m_EndTime;
        }

        return std::chrono::duration_cast<std::chrono::milliseconds>(endTime - m_StartTime).count();
    }

    double elapsedSeconds() { return elapsedMilliseconds() / 1000.0; }

private:
    std::chrono::time_point<std::chrono::system_clock> m_StartTime;
    std::chrono::time_point<std::chrono::system_clock> m_EndTime;
    bool m_bRunning = false;
};

struct LatencyStats {
    std::vector<int64_t> values;
    int threads = 0;

    void print() {
        std::sort(values.begin(), values.end());
        int t = (threads == 0) ? 1 : threads;
        int size = values.size();
        int64_t sum = 0;
        for (int64_t v : values) {
            sum += v;
        }
        float iops = t * size * 1000.f / sum;
        float avg = sum * 1.0f / size;
        long p00 = values.at(0);
        long p50 = values.at(size / 2);
        long p90 = values.at(size * 90 / 100);
        long p99 = values.at(size * 99 / 100);
        long p100 = values.at(size - 1);
        const char* sep = " - ";
        fprintf(stdout,
                "IOPS: %.2f(T=%d, %d / %ldms)%sLatency: avg = %.2fms, min = %ldms, p50 = %ldms, p90 = %ldms, p99 = "
                "%ldms, "
                "max = %ldms\n",
                iops, t, size, sum, sep, avg, p00, p50, p90, p99, p100);
    }

    void merge(const LatencyStats& s) {
        threads += 1;
        for (auto v : s.values) {
            values.emplace_back(v);
        }
    }
};

const char* getHdfsErrorMessage() {
#ifdef LIBHDFS3
    return hdfsGetLastError();
#else
    char* root_cause = hdfsGetLastExceptionRootCause();
    return root_cause ? root_cause : "";
#endif
}

hdfsFS makeHdfsFS(const char* namenode) {
    auto hdfs_builder = hdfsNewBuilder();
    hdfsBuilderSetNameNode(hdfs_builder, namenode);
    hdfsFS fs = hdfsBuilderConnect(hdfs_builder);
    if (fs == nullptr) {
        fprintf(stderr, "makeHdfsFS failed. namenode = %s, error = %s\n", namenode, getHdfsErrorMessage());
    }
    return fs;
}
struct FileMetadata {
    std::string name;
    int64_t size;
    std::string toString() const {
        std::stringstream ss;
        ss << "file(name = " << name << ", size = " << size << ")";
        return ss.str();
    }
};

std::vector<FileMetadata> listFiles(hdfsFS fs, const char* prefix) {
    std::vector<FileMetadata> files;

    hdfsFileInfo* ret;
    int numEntries = 0;
    ret = hdfsListDirectory(fs, prefix, &numEntries);
    if (ret == nullptr) {
        fprintf(stderr, "listFiles failed. prefix = %s, error = %s\n", prefix, getHdfsErrorMessage());
        return files;
    }

    for (int i = 0; i < numEntries; i++) {
        if (ret[i].mSize == 0) continue;
        files.emplace_back(FileMetadata{.name = ret[i].mName, .size = ret[i].mSize});
    }
    hdfsFreeFileInfo(ret, numEntries);
    return files;
}

hdfsFile openFileForRead(hdfsFS fs, const char* path) {
    hdfsFile file = hdfsOpenFile(fs, path, O_RDONLY, 0, 0, 0);
    if (file == nullptr) {
        fprintf(stderr, "openFile failed. path = %s, error = %s\n", path, getHdfsErrorMessage());
        return nullptr;
    }
    return file;
}

void closeFile(hdfsFS fs, hdfsFile file) {
    hdfsCloseFile(fs, file);
}

void readData(hdfsFS fs, hdfsFile file, const char* path, uint8_t* buf, int64_t offset, int64_t size) {
    int ret = 0;

    ret = hdfsSeek(fs, file, offset);
    if (ret != 0) {
        fprintf(stderr, "seekFile failed. path = %s, error = %s\n", path, getHdfsErrorMessage());
        return;
    }

    int64_t now = 0;
    while (now < size) {
        tSize r = hdfsRead(fs, file, buf + now, size - now);
        if (r == -1) {
            if (errno == EINTR) continue;
            fprintf(stderr, "readFile failed. path = %s, error = %s\n", path, getHdfsErrorMessage());
            return;
        }
        if (r == 0) break;
        now += r;
    }
    if (now != size) {
        fprintf(stderr, "!!!readFile not fully. path = %s\n", path);
    }
}

struct Task {
    Task() : rnd(std::random_device()()) {}

    std::mt19937 rnd;

    hdfsFS fs;
    const std::vector<FileMetadata>* files;
    int block_size = 128 * 1024;
    int round = 1;
    int repeat = 1;
    int64_t scan_size = 0;
    LatencyStats stats;

    void runOnce(const FileMetadata& f) {
        Timer timer;
        int64_t file_size = f.size;
        if (scan_size != 0) {
            file_size = std::min(file_size, scan_size);
        }
        std::uniform_int_distribution<int64_t> dist(0, file_size - block_size - 1);
        std::vector<uint8_t> buf(block_size);
        hdfsFile file = openFileForRead(fs, f.name.c_str());
        for (int i = 0; i < repeat; i++) {
            timer.start();
            int64_t offset = dist(rnd);
            readData(fs, file, f.name.c_str(), buf.data(), offset, block_size);
            timer.stop();
            stats.values.emplace_back(timer.elapsedMilliseconds());
        }
        hdfsCloseFile(fs, file);
    }

    void run() {
        std::uniform_int_distribution<int> dist(0, files->size() - 1);
        for (int i = 0; i < round; i++) {
            int idx = dist(rnd);
            const FileMetadata& f = files->at(idx);
            runOnce(f);
        }
        stats.print();
    }
};

int main(int argc, const char** argv) {
    const char* namenode = nullptr;
    const char* path = nullptr;
    int block_size = 4;
    int scan_size = 200;
    int repeat = 1;
    int round = 100;
    int threads = 16;

    int idx = 1;
    while (idx < argc) {
        std::string s(argv[idx]);
        if (s == "--endpoint") {
            namenode = argv[idx + 1];
            idx += 2;
        } else if (s == "--path") {
            path = argv[idx + 1];
            idx += 2;
        } else if (s == "--block") {
            block_size = atoi(argv[idx + 1]);
            idx += 2;
        } else if (s == "--scan") {
            scan_size = atoi(argv[idx + 1]);
            idx += 2;
        } else if (s == "--round") {
            round = atoi(argv[idx + 1]);
            idx += 2;
        } else if (s == "--repeat") {
            repeat = atoi(argv[idx + 1]);
            idx += 2;
        } else if (s == "--thread") {
            threads = atoi(argv[idx + 1]);
            idx += 2;
        } else {
            idx += 1;
        }
    }

    fprintf(stdout,
            "%s: endpoint = %s, path = %s, threads = %d, block_size = %dKB, scan_size = %dMB, round = %d, repeat = "
            "%d\n",
            argv[0], namenode, path, threads, block_size, scan_size, round, repeat);

    block_size *= 1024;
    scan_size *= 1024 * 1024;
    hdfsFS fs = makeHdfsFS(namenode);
    std::vector<FileMetadata> files = listFiles(fs, path);
    for (const FileMetadata& f : files) {
        std::cout << f.toString() << "\n";
    }

    // std::vector<uint8_t> buf;
    // buf.resize(block_size);
    // for (const FileMetadata& f : files) {
    //     Timer timer;
    //     timer.start();
    //     hdfsFile file = openFileForRead(fs, f.name.c_str());
    //     readData(fs, file, f.name.c_str(), buf.data(), 0, block_size);
    //     hdfsCloseFile(fs, file);
    //     timer.stop();
    //     std::cout << "Read path = " << f.toString() << ", time = " << timer.elapsedMilliseconds() << "\n";
    // }

    std::vector<Task> tasks(threads);
    for (int i = 0; i < threads; i++) {
        Task& t = tasks[i];
        t.fs = fs;
        t.files = &files;
        t.block_size = block_size;
        t.scan_size = scan_size;
        t.repeat = repeat;
        t.round = round;
    }

    std::vector<std::thread> T;
    for (int i = 0; i < threads; ++i) {
        std::thread t(&Task::run, &tasks[i]);
        T.emplace_back(std::move(t));
    }

    LatencyStats stats;
    for (int i = 0; i < threads; i++) {
        T[i].join();
        stats.merge(tasks[i].stats);
    }

    stats.print();

    return 0;
}
