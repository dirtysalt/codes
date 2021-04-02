# CMake 使用教程

https://cmake.org/cmake/help/latest/guide/tutorial/index.html

## 运行命令

```
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=`pwd`/install -DUSE_MATHLIB=ON ..
make
make install
```

## 配置编译选项

```
cmake .. -DUSE_MATHLIB=ON/OFF
```

## 配置安装位置

```
cmake -DCMAKE_INSTALL_PREFIX=`pwd`/install ..
make install
```
