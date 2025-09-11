cmake_minimum_required(VERSION 3.15)
set(NAME "test_asmjit2")
project(${NAME} CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(${NAME} main.cpp)
target_include_directories(${NAME} PRIVATE $ENV{HOME}/utils/installed/include)
target_link_directories(${NAME} PRIVATE $ENV{HOME}/utils/installed/lib)

# add asmjit library
target_link_libraries(${NAME} PRIVATE asmjit)


install(TARGETS ${NAME} DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
