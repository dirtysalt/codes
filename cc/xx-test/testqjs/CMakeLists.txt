cmake_minimum_required(VERSION 3.10) # 设置最低要求的CMake版本

project(testqjs.exe) # 设置项目名称

set(CMAKE_CXX_STANDARD 17) # 设置C++标准版本
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 添加头文件搜索路径
include_directories(
    /usr/local/include
)

# 设置源文件列表
set(SOURCE_FILES
    testqjs.cpp
)


# 创建可执行目标
add_executable(${PROJECT_NAME}
  ${SOURCE_FILES}  
)

# 添加链接库(如果有的话)
target_link_libraries(${PROJECT_NAME} /usr/local/lib/quickjs/libquickjs.a)