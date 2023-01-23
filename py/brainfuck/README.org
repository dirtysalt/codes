#+title: brainfuck jit

用它来学习JIT是个不错的选择

参考资料: https://github.com/cslarsen/brainfuck-jit

- simple_bf.py
  - Memory 实现了内存模块
  - run_naive 是直接对代码解释执行
  - optimize_sources 是对源代码优化包括操作合并，以及清零操作
  - run_optimized 是对优化后的源代码解释执行 `--optimize`
  - run_bytecode 是对优化后的源代码编译成为bytecode执行 `--bytecode`

- bytecode_bf.py
  - 上面那个版本run_bytecode其实效果不好，大部分时间集中在Memory的函数调用上
  - 所以这个版本对Memory做了个简化访问固定大小的数组
  - 然后将里面所有操作全部转换成了bytecode来执行，提升效果显著
