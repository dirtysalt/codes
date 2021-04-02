cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Tutorial VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the executable
add_executable(Tutorial src/tutorial.cpp)

configure_file(include/config.h.in include/config.h)

target_include_directories(
  Tutorial PUBLIC
  "${PROJECT_BINARY_DIR}/include"
  )