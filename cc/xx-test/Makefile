
all: \
	BenchHashFunc.exe \
	BenchHashFuncOnInt.exe \
	BenchRSqrt.exe \
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
	TestBitUnpacking.exe \
	TestTCCCodeGen.exe \
	UInt8MaxTest.exe \
	WatchMemoryOrdering.exe \
	ob_math_pic.exe \
	opt_linear_search.exe \
	xorll.exe \
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

# tcc -> tiny c compiler
LIB_FLAGS=-ltcc -lgtest_main -lbenchmark_main -lbenchmark -lgtest -lpthread -ldl

# Probably not working any more.
# runnable_so.exe:runnable_so.cc
# 	$(CXX) -o $@ -fPIC $(CXX_FLAGS)  -shared -e so_main $^

# test_pye.so: test_pye.cc
# 	$(CXX) -o $@ -fPIC $(CXX_FLAGS) -I$(INC_PYTHON)-shared -lboost_python $^

%.exe:%.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS}

test_cpp_feature.exe:test_cpp_feature.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS} -std=c++20 -latomic

clean:
	rm -rf *.exe *.o *.so *.dSYM
