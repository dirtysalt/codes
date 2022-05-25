
all: \
	CheckAllZero.exe \
	CompressFloat.exe \
	ConvertI64ToI8Bench.exe \
	ConvertI64ToI8Test.exe \
	FloatTest.exe \
	MatrixTranspose.exe \
	MemcopyTest.exe \
	PopCountTest.exe \
	PrintSIMDConstants.exe \
	StringLowerTest.exe \
	StringReplaceTest.exe \
	test_bit_unpacking.exe \
	test_tcc_codegen.exe \
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
	test_memory_align.exe \
	test_relaxed_memory.exe \
	test_cpp_feature.exe \
	test_gtest_function.exe

INC_PYTHON=/usr/include/python2.7/
INC_FLAGS=-I$(HOME)/utils/installed/include
LD_FLAGS=-L$(HOME)/utils/installed/lib
CXX_FLAGS=-std=c++17 -O3 -march=native # -mavx2 -mavx512f -mavx512bw -mavx512vbmi
ALL_FLAGS=${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS}
LIB_FLAGS=-lpthread -ldl

runnable_so.so:runnable_so.cc
	$(CXX) -o $@ $< -fPIC -O0 -g -shared -e so_main

test_pye.so: test_pye.cc
	$(CXX) -o $@ $< -fPIC -O0 -g -I$(INC_PYTHON)-shared -lboost_python

%.exe:%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS}

bench_%.exe:bench_%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -lbenchmark -lbenchmark_main

test_%.exe:test_%.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -lgtest -lgtest_main

test_cpp_feature.exe:test_cpp_feature.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -std=c++20 -latomic

test_tcc_codegen.exe:test_tcc_codegen.cpp
	$(CXX) -o $@ $< ${ALL_FLAGS} -ltcc -lpthread -ldl

clean:
	rm -rf *.exe *.o *.so *.dSYM
