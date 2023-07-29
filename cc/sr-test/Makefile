# makefile.

LD_FLAGS=-L${HOME}/installed/lib -L${HOME}/installed/lib64
CK_FLAGS=-ICK/ -ICK/base/
INC_FLAGS=-I${HOME}/installed/include ${SR_FLAGS} ${CK_FLAGS} 
CXX_FLAGS=-std=c++20 -O3 -g -mavx2 -mavx512f
LIB_FLAGS=-lbenchmark -lbenchmark_main -lpthread
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
	libhdfs_perf.exe

%.exe: %.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS}

libhdfs_perf.exe: libhdfs_perf.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} libhdfs.a ${LD_FLAGS} -L$(JAVA_HOME)/jre/lib/amd64/server -ljvm ${LIB_FLAGS} ${LIBCXX_FLAGS}

clean:
	rm -rf *.exe perf.data*
