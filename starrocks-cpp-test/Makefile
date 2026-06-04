# makefile.
SRCC=gcc
SRCXX=g++
SR_BUILD_TYPE=RELEASE
LD_FLAGS=-L${HOME}/installed/lib -L${HOME}/installed/lib64 -L${TP_INSTALL_DIR}/lib -L${TP_INSTALL_DIR}/lib64
CK_FLAGS=-I./CK/ -I./CK/base/
SR_FLAGS=-I${STARROCKS_HOME}/be/src
INC_FLAGS=-I${HOME}/installed/include -I${TP_INSTALL_DIR}/include ${SR_FLAGS} ${CK_FLAGS} 
CXX_FLAGS=-std=c++20 -O3 -g -mavx2 -mavx512f
LIB_FLAGS=-lcctz -lbenchmark -lbenchmark_main -lpthread
LIBCXX_FLAGS=-static-libstdc++ -static-libgcc
# LIBCXX_FLAGS=


all: \
	hash_set_perf.exe \
	b2i_perf.exe \
	malloc_perf.exe \
	filter_range_perf.exe \
	filter_range_test.exe \
	runtime_filter_perf.exe \
	float_distance_perf.exe \
	python_udf_checker.exe \
	test_cctz_timezone.exe \
	test_jni.exe

%.exe: %.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS}

test_jni.exe: test_jni.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} -lhdfs -L$(JAVA_HOME)/lib/server -ljvm ${LIBCXX_FLAGS}

clean:
	rm -rf *.exe perf.data*
