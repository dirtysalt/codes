#coding:utf-8
#Copyright (C) dirlt

TARGET=libnative.so

${TARGET}:native.cc native.h
	g++ -o $@ $< -shared -fPIC -O2 -ltcmalloc -I${JAVA_HOME}/include
	mkdir -p ../src/main/resources && cp $@ ../src/main/resources

native.h:
	javah -o native.h -classpath ../target/classes com.dirlt.java.jni.Main

clean:
	rm -rf ${TARGET} ../src/main/resources/${TARGET}