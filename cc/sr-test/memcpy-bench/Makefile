# makefile.

LD_FLAGS=-L${HOME}/installed/lib -L${HOME}/installed/lib64
CK_FLAGS=-I../CK/ -I../CK/base/ -I../CK/base/pcg-random/
INC_FLAGS=-I${HOME}/installed/include ${CK_FLAGS} 
CXX_FLAGS=-std=c++20 -O3 -g -mavx2 -fno-tree-loop-distribute-patterns -Wno-old-style-cast -Wno-cast-qual -Wno-cast-align
LIB_FLAGS=-lbenchmark -lpthread -ldl
LIBCXX_FLAGS=-static-libstdc++ -static-libgcc

OBJS=memcpy_jart.o \
	glibc/memcpy-ssse3.o glibc/memcpy-ssse3-back.o \
	glibc/memmove-avx512-no-vzeroupper.o \
	glibc/memmove-sse2-unaligned-erms.o \
	glibc/memmove-avx-unaligned-erms.o \
	glibc/memmove-avx512-unaligned-erms.o

all: \
	memcpy-bench.exe \
	ck-memcpy-bench.exe \
	memcpy-test.exe

ck-memcpy-bench.exe:ck-memcpy-bench.o ${OBJS}
	$(CXX) -o $@ $^ ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS} -static -lboost_program_options

memcpy-bench.exe:memcpy-bench.o ${OBJS}
	$(CXX) -o $@ $^ ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS} -lbenchmark_main


memcpy-test.exe:memcpy-test.o ${OBJS}
	$(CXX) -o $@ $^ ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS}


memcpy-bench.o:memcpy-bench.cpp memcpy-impl.h
ck-memcpy-bench.o:ck-memcpy-bench.cpp memcpy-impl.h
memcpy-test.o:memcpy-test.cpp memcpy-impl.h

%.o:%.cpp
	$(CXX) -o $@ -c $< ${INC_FLAGS} ${CK_FLAGS} ${CXX_FLAGS}

%.o:%.S
	$(CXX) -o $@ -c $< ${INC_FLAGS} ${CK_FLAGS} ${CXX_FLAGS}

clean:
	rm -rf *.exe perf.data* *.o ${OBJS} core.*
