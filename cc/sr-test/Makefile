LD_FLAGS=-L${STARROCKS_THIRDPARTY}/installed/lib -L${STARROCKS_THIRDPARTY}/installed/lib64 -L${HOME}/installed/lib -L${HOME}/installed/lib64
CK_FLAGS=-ICK/ -ICK/base/
SR_FLAGS=-I${STARROCKS_THIRDPARTY}/installed/include -I${STARROCKS_HOME}/be/src/ -I${STARROCKS_HOME}/gensrc/build/
INC_FLAGS=${SR_FLAGS} ${CK_FLAGS} -I${HOME}/installed/include
CXX_FLAGS=-std=c++20 -msse4.2 -mavx2 -O3 -g -mavx512f
MY_LIB_FLAGS=-latomic -lroaring -lgtest -lbenchmark -lgtest_main -lbenchmark_main -lpthread
LIBC_LIB_FLAGS=-static-libstdc++ -static-libgcc

all: \
	phmapbench.exe \
	hash_set_perf.exe \
	test_roaring_bitmap.exe

%.exe: %.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${MY_LIB_FLAGS} ${LIBC_LIB_FLAGS}

clean:
	rm -rf *.exe perf.data*
