
#include <sys/poll.h>
#include <unistd.h>

#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

int run() {
    int pipefd[2];

    if (pipe(pipefd) == -1) {
        fprintf(stderr, "create pipe error\n");
        return -1;
    }

    pid_t cpid = fork();
    if (cpid == -1) {
        fprintf(stderr, "fork failed\n");
        return -1;

    } else if (cpid == 0) {
        dup2(pipefd[1], STDOUT_FILENO);
        dup2(pipefd[1], STDERR_FILENO);
        // run child process
        // close all resource
        // std::unordered_set<int> reserved_fd{0, 1, 2, pipefd[0]};
        // auto status = close_all_fd_except(reserved_fd);
        // if (!status.ok()) {
        //     std::cout << "close fd failed:" << status.to_string() << std::endl;
        //     exit(-1);
        // }

        pid_t self_pid = getpid();
        std::string str_pid = std::to_string(self_pid);
        // char command[] = "python3";
        std::string command = "python3";
        std::string script = "/home/disk2/zhangyan/output/be/lib/py-packages/flight_server.py";
        std::string unix_socket = "/home/disk2/zhangyan/output/be/lib/py-packages/a.out";
        std::string python_home_env = "PYTHONHOME=/home/disk4/zhangyan/utils/miniconda3/";
        char* const args[] = {command.data(), script.data(), unix_socket.data(), nullptr};
        char* const envs[] = {python_home_env.data(), nullptr};
        // exec flight server
        if (execvpe("/home/disk4/zhangyan/utils/miniconda3/bin/python3", args, envs)) {
            std::cout << "execvp failed:" << std::strerror(errno) << std::endl;
            exit(-1);
        }

    } else {
        close(pipefd[1]);

        pollfd fds[1];
        fds[0].fd = pipefd[0];
        fds[0].events = POLLIN;

        // wait util worker start
        int ret = poll(fds, 1, 1000);
        if (ret == -1) {
            fprintf(stderr, "poll failed\n");
        } else if (ret == 0) {
            fprintf(stderr, "child failed\n");
        }

        while (1) {
            char buffer[4096];
            ssize_t n = read(pipefd[0], buffer, sizeof(buffer));
            if (n == 0) break;
            buffer[n] = '\0';
            fprintf(stderr, "stderr = %s", buffer);
        }
    }
    return 0;
}

int main() {
    return run();
}