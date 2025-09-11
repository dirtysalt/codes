all: \
	CheckAllZero.exe \
	CompressFloat.exe \
	bench_cvt_i64toi8.exe \
	test_cvt_i64toi8.exe \
	FloatTest.exe \
	MatrixTranspose.exe \
	MemcopyTest.exe \
	PopCountTest.exe \
	PrintSIMDConstants.exe \
	StringLowerTest.exe \
	StringReplaceTest.exe \
	test_bit_unpack.exe \
	bench_uint8_max.exe \
	WatchMemoryOrdering.exe \
	ob_math_pic.exe \
	opt_linear_search.exe \
	xorll.exe \
	bench_hash_func_int.exe \
	bench_rsqrt.exe \
	bench_select_if.exe \
	test_select_if.exe \
	bench_restrict_sum.exe \
	bench_template_pow.exe \
	MemAlignTest.exe \
	FaultyRelaxedMemory.exe \
	gtest_feature.exe \
	test_tdigest.exe \
	bench_checksum_disk_data.exe \
	fizzbuzz-loop.exe \
	fizzbuzz.exe \
	fizzbuzz-asm.exe \
	fizzbuzz-cjit.exe \
	test_memory_order.exe \
	bench_codegen_simd.exe \
	test_cpp_feature.exe \
	test_perf_event.exe \
	test_boost_fiber.exe \
	test_boost_continuation.exe \
	test_multi_version.exe

x86-linux: \
	test_tcc_codegen.exe \
	test_native_jit.exe


INC_PYTHON=/usr/include/python3.10/
INC_FLAGS=-I$(HOME)/utils/installed/include
LD_FLAGS=-L$(HOME)/utils/installed/lib
CXX_FLAGS=-std=c++17 -g -O3 -march=native # -mavx2 -mavx512f -mavx512bw -mavx512vbmi # clangd does not understand -march
ALL_FLAGS=${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS}
LIB_FLAGS=-lpthread -lz
LIBCXX_FLAGS=-static-libstdc++ -static-libgcc

test_boost_pythonext.so: test_boost_pythonext.cpp
	$(CXX) -o $@ $< -fPIC -O0 -g -I$(INC_PYTHON) -shared -lboost_python310

test_boost_%.exe:test_boost_%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -lboost_context

bench_%.exe:bench_%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -lbenchmark -lbenchmark_main

gtest_%.exe:gtest_%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -lgtest -lgtest_main

%.exe:%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS}

# gnu libatomic
test_cpp_feature.exe:test_cpp_feature.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -std=c++2a -latomic

# https://bellard.org/tcc/
test_tcc_codegen.exe:test_tcc_codegen.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -ltcc -lpthread -ldl

# https://github.com/BitFunnel/NativeJIT
test_native_jit.exe:test_native_jit.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -I${HOME}/repo/NativeJIT/inc \
		-L${HOME}/repo/NativeJIT/build-make/src/NativeJIT -L${HOME}/repo/NativeJIT/build-make/src/CodeGen \
		-lNativeJIT -lCodeGen -lpthread -ldl

# fizzbuss test
fizzbuzz-asm.exe:fizzbuzz-asm.S
	gcc -mavx2 -c $<
	ld -o $@ fizzbuzz-asm.o
	rm fizzbuzz-asm.o

fizzbuzz.exe:fizzbuzz.cpp fizzbuzz-gen.h
	$(CXX) -o $@ $< ${ALL_FLAGS}

fizzbuzz-cjit.exe:fizzbuzz-cjit.c
	$(CC) -o $@ $< -O2 -g -mavx -mavx2 -flax-vector-conversions

clean:
	rm -rf *.exe *.o *.so *.dSYM
