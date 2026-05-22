cmake_minimum_required(VERSION 3.10)
project(test-qjs)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
    /usr/local/include
)
link_directories(
    /usr/local/lib/quickjs
)
add_executable(testqjs.exe testqjs.cpp)
target_link_libraries(testqjs.exe quickjs)
target_link_options(testqjs.exe PRIVATE -ldl -lpthread)
