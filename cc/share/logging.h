/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_LOGGER_INL_H__
#define __CC_SHARE_LOGGER_INL_H__

#include <cstdlib>
#include <cstdio>
#include <cerrno>
#include <cstring>

#define SERRNO (strerror(errno))
#define SERRNO2(n) (strerror(n))

#ifndef NDEBUG
#define DEBUG(fmt,...)                                          \
    (fprintf(stderr, "[DEBUG][%s][%s:%d]"fmt,                   \
             __FUNCTION__, __FILE__, __LINE__, ##__VA_ARGS__))
#else
#define DEBUG(fmt,...)
#endif

#define NOTICE(fmt,...)                                         \
    (fprintf(stderr, "[NOTICE][%s][%s:%d]"fmt,                  \
             __FUNCTION__, __FILE__, __LINE__, ##__VA_ARGS__))
#define TRACE(fmt,...)                                              \
    (fprintf(stderr, "[TRACE][%s][%s:%d]"fmt,                       \
             __FUNCTION__, __FILE__, __LINE__, ##__VA_ARGS__))
#define WARNING(fmt,...)                                            \
    (fprintf(stderr, "[WARNING][%s][%s:%d]"fmt,                     \
             __FUNCTION__, __FILE__, __LINE__, ##__VA_ARGS__))
#define FATAL(fmt,...)                                              \
    (fprintf(stderr, "[FATAL][%s][%s:%d]"fmt,                       \
             __FUNCTION__, __FILE__, __LINE__, ##__VA_ARGS__))

#endif // __CC_SHARE_LOGGER_INL_H__
