代码结构
=====

- bench/test_cvt_i64toi8.cpp # 把int64数组批量转为int8的性能测试
- bench_hash_func_int.cpp # Hash function在整数上的性能测试
- bench_rsqrt.cpp # 平方根倒数的性能测试
- bench/test_select_if.cpp # Select-If性能测试
- bench_uint8_maxc.pp # max(uint8_a, uint8_b) 性能测试
- CompressFloat # 尝试压缩浮点数(但是好像不太成功)
- FloatTest.cpp # 一些浮点和整数时间转换操作
- MatrixTranpose.cpp # 矩阵转置的cache优化
- MemAlignTest.cpp # false-sharing的性能影响
- ob_math_pic.cpp # 生成分形 [图形](./ob_math_pic.jpg)
- opt_linear_search.cpp # 循环展开对搜索线性搜索的影响
- PopCountTest.cpp # 计算popcount的几种方法
- csp-primes.go # 使用CSP的方式来过滤素数
- runnable_so.cc # 可以运行的so文件
- StringLowerTest.cpp # SIMD来实现string lower
- StringReplaceTest.cpp # SIMD来实现char replacement
- test_bit_unpack.cpp # 测试bit unpacking性能
- test_pye.cc # 用boost编写python extension
- test_tcc_codegen # tcc来做codegen的性能
- xorll.cpp # XOR 链表
