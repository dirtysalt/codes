/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include "native.h"

JNIEXPORT void JNICALL Java_com_dirlt_java_jni_Main_hello (JNIEnv *, jclass) {
  printf("hello,world\n");
}
