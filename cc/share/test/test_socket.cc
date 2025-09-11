/*
 * Copyright (C) dirlt
 */

#include <sys/epoll.h>
#include <signal.h>
#include <pthread.h>
#include "share/util.h"
#include "share/socket.h"
#include "share/logging.h"

using namespace share;

void* thread_function(void* /*arg*/) {
    DEBUG("start client...");
    int conn = create_tcp_socket();
    set_nonblock(conn);
    DEBUG("start connect...");
    tcp_connect(conn, "127.0.0.1", 19870);
    set_tcp_nodelay(conn);

    char c = 'x';
    if(write(conn, &c, 1) < 0) {
        WARNING("write failed(%s)", SERRNO);
    }
    close(conn);
    return NULL;
}

int main() {
    std::string ip = get_local_ip();
    TRACE("local ip='%s'", ip.c_str());
    // --------------------
    signal(SIGPIPE, SIG_IGN);
    DEBUG("start server...");
    int server = create_tcp_socket();
    set_ip_reuseaddr(server);
    DEBUG("start bind listen...");
    tcp_bind_listen(server, "127.0.0.1", 19870, 10);
    pthread_t tid;
    pthread_create(&tid, NULL, thread_function, NULL);
    int conn = tcp_accept(server);
    DEBUG("conn(%d)", conn);
    char c[1];
    assert(read(conn, c, sizeof(c)) == 1);
    assert(c[0] == 'x');
    close(conn);
    pthread_join(tid, NULL);
    close(server);
}
