/*
 * Copyright (C) dirlt
 */

#ifndef __CC_BENCH_DEFINE_H__
#define __CC_BENCH_DEFINE_H__

#define TC(func,arg) do {                       \
        for(int i=0;i<kThreadNumber;i++){           \
            pthread_create(&tid[i],NULL,func,arg);    \
        }                                           \
    }while(0)
#define TW() do {                               \
        for(int i=0;i<kThreadNumber;i++){           \
            pthread_join(tid[i],NULL);                \
        }                                           \
    }while(0)

#define RTC(func,arg) do {                      \
        for(int i=0;i<kReadThreadNumber;i++){       \
            pthread_create(&rtid[i],NULL,func,arg);   \
        }                                           \
    }while(0)
#define WTC(func,arg) do {                        \
        for(int i=0;i<kWriteThreadNumber;i++){        \
            pthread_create(&wtid[i],NULL,func,arg);     \
        }                                             \
    }while(0)
#define RTW() do {                              \
        for(int i=0;i<kReadThreadNumber;i++){       \
            pthread_join(rtid[i],NULL);               \
        }                                           \
    }while(0)
#define WTW() do {                              \
        for(int i=0;i<kWriteThreadNumber;i++){      \
            pthread_join(wtid[i],NULL);               \
        }                                           \
    }while(0)

#endif // __CC_BENCH_DEFINE_H__
