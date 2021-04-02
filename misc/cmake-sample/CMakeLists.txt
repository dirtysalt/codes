cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Tutorial VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 把make详细命令打印出来
set(CMAKE_VERBOSE_MAKEFILE ON)

# 设置各种配置选项
option(USE_MATHLIB "Use MathLib" ON)
if(USE_MATHLIB)
  message("add subdirectory MathLib")
  add_subdirectory(MathLib)
  list(APPEND EXTRA_LIBS MathLib)
  # 如果使用 "MathLib/xxx.h" 的话可能就不需要了
  # list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathLib")
  # 另外如果子项目里面增加了interface的话，那么主目录直接使用xxx.h也可以
endif()

# 配置config.h
configure_file(include/config.h.in include/config.h)

# add the executable
add_executable(Tutorial src/tutorial.cpp)

target_include_directories(
  Tutorial PUBLIC
  # build目录下面的include/config.h
  "${PROJECT_BINARY_DIR}/include"
  "${PROJECT_SOURCE_DIR}/include" # 顶层目录
  # ${EXTRA_INCLUDES} # 其他配置

)
target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/include/config.h" "${PROJECT_SOURCE_DIR}/include/tutorial.h" DESTINATION include)
