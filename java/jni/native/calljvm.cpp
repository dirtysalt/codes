/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <jni.h>
#include <pthread.h>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <thread>

// https://github.com/c9n/hadoop/blob/master/hadoop-hdfs-project/hadoop-hdfs/src/main/native/libhdfs/jni_helper.c

// =====================================================================

/* Use gcc type-checked format arguments. */
#define TYPE_CHECKED_PRINTF_FORMAT(formatArg, varArgs) __attribute__((format(printf, formatArg, varArgs)))

/*
 * Mutex and thread data types defined by pthreads.
 */
typedef pthread_mutex_t mutex;
typedef pthread_t threadId;

mutex jvmMutex = PTHREAD_MUTEX_INITIALIZER;

int mutexLock(mutex* m) {
    int ret = pthread_mutex_lock(m);
    if (ret) {
        fprintf(stderr, "mutexLock: pthread_mutex_lock failed with error %d\n", ret);
    }
    return ret;
}

int mutexUnlock(mutex* m) {
    int ret = pthread_mutex_unlock(m);
    if (ret) {
        fprintf(stderr, "mutexUnlock: pthread_mutex_unlock failed with error %d\n", ret);
    }
    return ret;
}

/** Key that allows us to retrieve thread-local storage */
static pthread_key_t gTlsKey;

/** nonzero if we succeeded in initializing gTlsKey. Protected by the jvmMutex */
static int gTlsKeyInitialized = 0;

/**
 * The function that is called whenever a thread with libhdfs thread local data
 * is destroyed.
 *
 * @param v         The thread-local data
 */
static void hdfsThreadDestructor(void* v) {
    JavaVM* vm;
    JNIEnv* env = (JNIEnv*)v;
    jint ret;

    // ret = (*env)->GetJavaVM(env, &vm);
    ret = env->GetJavaVM(&vm);
    if (ret) {
        fprintf(stderr, "hdfsThreadDestructor: GetJavaVM failed with error %d\n", ret);
        // (*env)->ExceptionDescribe(env);
        env->ExceptionDescribe();
    } else {
        //(*vm)->DetachCurrentThread(vm);
        vm->DetachCurrentThread();
    }
}

int threadLocalStorageGet(JNIEnv** env) {
    int ret = 0;
    if (!gTlsKeyInitialized) {
        ret = pthread_key_create(&gTlsKey, hdfsThreadDestructor);
        if (ret) {
            fprintf(stderr, "threadLocalStorageGet: pthread_key_create failed with error %d\n", ret);
            return ret;
        }
        gTlsKeyInitialized = 1;
    }
    *env = (JNIEnv*)pthread_getspecific(gTlsKey);
    return ret;
}

int threadLocalStorageSet(JNIEnv* env) {
    int ret = pthread_setspecific(gTlsKey, env);
    if (ret) {
        fprintf(stderr, "threadLocalStorageSet: pthread_setspecific failed with error %d\n", ret);
        hdfsThreadDestructor(env);
    }
    return ret;
}

#define HAVE_BETTER_TLS
/*
 * Most operating systems support the more efficient __thread construct, which
 * is initialized by the linker.  The following macros use this technique on the
 * operating systems that support it.
 */
#ifdef HAVE_BETTER_TLS
#define THREAD_LOCAL_STORAGE_GET_QUICK()        \
    static __thread JNIEnv* quickTlsEnv = NULL; \
    {                                           \
        if (quickTlsEnv) {                      \
            return quickTlsEnv;                 \
        }                                       \
    }

#define THREAD_LOCAL_STORAGE_SET_QUICK(env) \
    { quickTlsEnv = (env); }
#else
#define THREAD_LOCAL_STORAGE_GET_QUICK()
#define THREAD_LOCAL_STORAGE_SET_QUICK(env)
#endif

// ============================================================
/**
 * Length of buffer for retrieving created JVMs.  (We only ever create one.)
 */
#define VM_BUF_LENGTH 1

/**
 * Get the global JNI environemnt.
 *
 * We only have to create the JVM once.  After that, we can use it in
 * every thread.  You must be holding the jvmMutex when you call this
 * function.
 *
 * @return          The JNIEnv on success; error code otherwise
 */
static JNIEnv* getGlobalJNIEnv(void) {
    JavaVM* vmBuf[VM_BUF_LENGTH];
    JNIEnv* env;
    jint rv = 0;
    jint noVMs = 0;
    jthrowable jthr;
    char* hadoopClassPath;
    const char* hadoopClassPathVMArg = "-Djava.class.path=";
    size_t optHadoopClassPathLen;
    char* optHadoopClassPath;
    int noArgs = 1;
    char* hadoopJvmArgs;
    char jvmArgDelims[] = " ";
    char *str, *token, *savePtr;
    JavaVMInitArgs vm_args;
    JavaVM* vm;
    JavaVMOption* options;

    rv = JNI_GetCreatedJavaVMs(&(vmBuf[0]), VM_BUF_LENGTH, &noVMs);
    if (rv != 0) {
        fprintf(stderr, "JNI_GetCreatedJavaVMs failed with error: %d\n", rv);
        return NULL;
    }

    if (noVMs == 0) {
        //Get the environment variables for initializing the JVM
        hadoopClassPath = getenv("CLASSPATH");
        if (hadoopClassPath == NULL) {
            fprintf(stderr, "Environment variable CLASSPATH not set!\n");
            return NULL;
        }
        optHadoopClassPathLen = strlen(hadoopClassPath) + strlen(hadoopClassPathVMArg) + 1;
        optHadoopClassPath = (char*)malloc(sizeof(char) * optHadoopClassPathLen);
        snprintf(optHadoopClassPath, optHadoopClassPathLen, "%s%s", hadoopClassPathVMArg, hadoopClassPath);

        // Determine the # of LIBHDFS_OPTS args
        hadoopJvmArgs = getenv("LIBHDFS_OPTS");
        if (hadoopJvmArgs != NULL) {
            hadoopJvmArgs = strdup(hadoopJvmArgs);
            for (noArgs = 1, str = hadoopJvmArgs;; noArgs++, str = NULL) {
                token = strtok_r(str, jvmArgDelims, &savePtr);
                if (NULL == token) {
                    break;
                }
            }
            free(hadoopJvmArgs);
        }

        // Now that we know the # args, populate the options array
        options = (JavaVMOption*)calloc(noArgs, sizeof(JavaVMOption));
        if (!options) {
            fputs("Call to calloc failed\n", stderr);
            free(optHadoopClassPath);
            return NULL;
        }
        options[0].optionString = optHadoopClassPath;
        hadoopJvmArgs = getenv("LIBHDFS_OPTS");
        if (hadoopJvmArgs != NULL) {
            hadoopJvmArgs = strdup(hadoopJvmArgs);
            for (noArgs = 1, str = hadoopJvmArgs;; noArgs++, str = NULL) {
                token = strtok_r(str, jvmArgDelims, &savePtr);
                if (NULL == token) {
                    break;
                }
                options[noArgs].optionString = token;
            }
        }

        //Create the VM
        vm_args.version = JNI_VERSION_1_2;
        vm_args.options = options;
        vm_args.nOptions = noArgs;
        vm_args.ignoreUnrecognized = 1;

        rv = JNI_CreateJavaVM(&vm, (void**)&env, &vm_args);

        if (hadoopJvmArgs != NULL) {
            free(hadoopJvmArgs);
        }
        free(optHadoopClassPath);
        free(options);

        if (rv != 0) {
            fprintf(stderr,
                    "Call to JNI_CreateJavaVM failed "
                    "with error: %d\n",
                    rv);
            return NULL;
        }
        // jthr = invokeMethod(env, NULL, STATIC, NULL,
        //                  "org/apache/hadoop/fs/FileSystem",
        //                  "loadFileSystems", "()V");
        // if (jthr) {
        //     printExceptionAndFree(env, jthr, PRINT_EXC_ALL, "loadFileSystems");
        // }
    } else {
        //Attach this thread to the VM
        vm = vmBuf[0];
        rv = vm->AttachCurrentThread((void**)&env, 0);
        if (rv != 0) {
            fprintf(stderr,
                    "Call to AttachCurrentThread "
                    "failed with error: %d\n",
                    rv);
            return NULL;
        }
    }

    return env;
}

/**
 * getJNIEnv: A helper function to get the JNIEnv* for the given thread.
 * If no JVM exists, then one will be created. JVM command line arguments
 * are obtained from the LIBHDFS_OPTS environment variable.
 *
 * Implementation note: we rely on POSIX thread-local storage (tls).
 * This allows us to associate a destructor function with each thread, that
 * will detach the thread from the Java VM when the thread terminates.  If we
 * failt to do this, it will cause a memory leak.
 *
 * However, POSIX TLS is not the most efficient way to do things.  It requires a
 * key to be initialized before it can be used.  Since we don't know if this key
 * is initialized at the start of this function, we have to lock a mutex first
 * and check.  Luckily, most operating systems support the more efficient
 * __thread construct, which is initialized by the linker.
 *
 * @param: None.
 * @return The JNIEnv* corresponding to the thread.
 */
JNIEnv* getJNIEnv(void) {
    JNIEnv* env;
    THREAD_LOCAL_STORAGE_GET_QUICK();
    mutexLock(&jvmMutex);
    if (threadLocalStorageGet(&env)) {
        mutexUnlock(&jvmMutex);
        return NULL;
    }
    if (env) {
        mutexUnlock(&jvmMutex);
        return env;
    }

    env = getGlobalJNIEnv();
    mutexUnlock(&jvmMutex);
    if (!env) {
        fprintf(stderr, "getJNIEnv: getGlobalJNIEnv failed\n");
        return NULL;
    }
    if (threadLocalStorageSet(env)) {
        return NULL;
    }
    THREAD_LOCAL_STORAGE_SET_QUICK(env);
    return env;
}

// ============================================================
int runGreet(JNIEnv* env) {
    jclass mainClass = env->FindClass("com/dirlt/java/jni/CalledByNative");
    if (mainClass == nullptr) {
        fprintf(stderr, "class not found");
        return 1;
    }
    jmethodID greetMethod = env->GetStaticMethodID(mainClass, "greet", "()V");
    if (greetMethod == nullptr) {
        fprintf(stderr, "method not found");
        return 1;
    }

    env->CallStaticVoidMethod(mainClass, greetMethod);
    return 0;
}

int main() {
    JNIEnv* env = getJNIEnv();
    runGreet(env);

    // fork a thread A, and run it.
    auto p = [env]() {
        // not working
        // runGreet(env);
        JNIEnv* new_env = getJNIEnv();
        runGreet(new_env);
    };
    std::thread A(p);
    A.join();
}
