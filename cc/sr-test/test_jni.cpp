#include <stdio.h>

// #include "jni.h"

struct JNIEnv;
extern "C" JNIEnv* getJNIEnv(void);

int main() {
    JNIEnv* env = getJNIEnv();
    if (env) {
        printf("Got JNIEnv: %p\n", env);
    } else {
        printf("Failed to get JNIEnv\n");
    }
    return 0;
}