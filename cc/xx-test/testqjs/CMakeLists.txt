cmake_minimum_required(VERSION 3.10)
project(testqjs)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
    /usr/local/include
)
add_executable(testqjs.exe testqjs.cpp)
target_link_libraries(testqjs.exe /usr/local/lib/quickjs/libquickjs.a)