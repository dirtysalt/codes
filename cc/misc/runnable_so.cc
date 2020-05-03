/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <cstdlib>

#ifndef BEGIN_DECLS
#ifdef __cplusplus
#define BEGIN_DECLS extern "C" {
#define END_DECLS }
#else
#define BEGIN_DECLS
#define BEGIN_DECLS
#endif
#endif

BEGIN_DECLS
#ifndef __i386
#define LD_SO_PATH "/lib64/ld-linux-x86-64.so.2"
#else
#define LD_SO_PATH "/lib/ld-linux.so.2"
#endif

#if defined(__DATE__) && defined(__TIME__)
#define BUILD_DATE  (__DATE__ " " __TIME__)
#else
#define BUILD_DATE  "unknown"
#endif


const char interp[] __attribute__((section(".interp"))) = LD_SO_PATH;
void so_main() {
    printf("LD_SO_PATH : %s\n", LD_SO_PATH);
    printf("BuildDate : %s\n", BUILD_DATE);
    exit(0);
}

END_DECLS
