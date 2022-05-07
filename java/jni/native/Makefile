#coding:utf-8
#Copyright (C) dirlt

ALL:libnative.so

INCFLAGS=-I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin

${TARGET}:native.cc native.h
	g++ -o $@ $< -shared -fPIC ${INCFLAGS}
	mkdir -p ../src/main/resources && cp $@ ../src/main/resources

native.h:
	javah -o native.h -classpath ../target/classes com.dirlt.java.jni.RunNativeLibrary

clean:
	rm -rf libnative.so ../src/main/resources/libnative.so
