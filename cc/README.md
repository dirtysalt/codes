# 目录结构

- itachi. 仿照kylin写的异步网络框架 [based on libev]
- nasty. 用flex/bison写的lisp分析器（或许可以作为某种参考代码使用）
- share. 公共代码（早年的时候喜欢封装东西，现在看起来没太大用途）
- misc. 测试和分析代码
  - `ob_math_pic.cc` 生成分形 [图形](./misc/ob_math_pic.jpg)
  - `runable_so.cc` 生成可执行.so文件
  - `test_pye.cc` 用boost编写python extension
  - `xorll.cc` XOR 链表
  - `FloatTest.c` 一些浮点和整数时间转换操作
  - `MatrixTranpose.cpp` 矩阵转置的cache优化
  - `PopCountTest.cpp` 计算popcount的几种方法
  - `opt_linear_search.cc` 循环展开对搜索线性搜索的影响
  - `primes.go` 使用CSP的方式来过滤素数
  - `ConvertI64ToI8.cpp` 把int64数组批量转为int8的性能测试
