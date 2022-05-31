#coding:utf-8
#Copyright (C) dirlt

ALL:libnative.so calljvm.exe SMOnFileChannel.exe

JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.0.1.jdk/Contents/Home/
INCFLAGS=-I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin
LDFLAGS=-L$(JAVA_HOME)/lib/server -rpath $(JAVA_HOME)/lib/server

libnative.so:native.cc native.h
	g++ -o $@ $< -shared -fPIC ${INCFLAGS}
	mkdir -p ../src/main/resources && cp $@ ../src/main/resources

native.h:
	javah -o native.h -classpath ../target/classes com.dirlt.java.trash.RunNativeLibrary

calljvm.exe:calljvm.cpp
	g++ -o $@ $< -std=c++11 ${INCFLAGS} ${LDFLAGS} -ljvm

clean:
	rm -rf libnative.so ../src/main/resources/libnative.so calljvm.exe SMOnFileChannel.exe

run_calljvm:calljvm.exe
	CLASSPATH=../target/trash-1.0-SNAPSHOT.jar ./calljvm.exe

SMOnFileChannel.exe:SMOnFileChannel.cpp
	g++ -o $@ $< -std=c++11
