# makefile.

LD_FLAGS=-L${HOME}/installed/lib -L${HOME}/installed/lib64 -L${STARROCKS_THIRDPARTY}/installed/lib -L${STARROCKS_THIRDPARTY}/installed/lib64 
CK_FLAGS=-ICK/ -ICK/base/
SR_FLAGS=-I${STARROCKS_THIRDPARTY}/installed/include -I${STARROCKS_HOME}/be/src/ -I${STARROCKS_HOME}/gensrc/build/
INC_FLAGS=-I${HOME}/installed/include ${SR_FLAGS} ${CK_FLAGS} 
CXX_FLAGS=-std=c++20 -O3 -g -mavx2 -mavx2 -mavx512f
LIB_FLAGS=-lbenchmark -lbenchmark_main -lpthread
#LIBC_LIB_FLAGS=-static-libstdc++ -static-libgcc
LIBC_LIB_FLAGS=

all: \
	hash_set_perf.exe \

%.exe: %.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS} ${LIBC_LIB_FLAGS}

clean:
	rm -rf *.exe perf.data*
