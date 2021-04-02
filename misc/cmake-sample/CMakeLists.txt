cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Tutorial VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 把make详细命令打印出来
set(CMAKE_VERBOSE_MAKEFILE ON)

option(USE_MATHLIB "Use MathLib" ON)

configure_file(include/config.h.in include/config.h)

# add the executable
add_executable(Tutorial src/tutorial.cpp)

target_include_directories(
  Tutorial PUBLIC
  # build目录下面的目录，config.h
  "${PROJECT_BINARY_DIR}/include"
  ${PROJECT_SOURCE_DIR}
  )

if(USE_MATHLIB)
  message("add subdirectory MathLib")
  add_subdirectory(MathLib)
  list(APPEND EXTRA_LIBS MathLib)
  # 如果使用 "MathLib/xxx.h" 的话可能就不需要了
  # list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathLib")
endif()

target_include_directories(
  Tutorial PUBLIC
  # build目录下面的目录，config.h
  "${PROJECT_BINARY_DIR}/include"
  ${EXTRA_INCLUDES}
  )

message("extra libs = ${EXTRA_LIBS}")
target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})
