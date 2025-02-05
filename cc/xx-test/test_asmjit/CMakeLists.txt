cmake_minimum_required(VERSION 3.15)
project(test_asmjit CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(test_asmjit main.cpp)
target_include_directories(test_asmjit PRIVATE $ENV{HOME}/utils/installed/include)
target_link_directories(test_asmjit PRIVATE $ENV{HOME}/utils/installed/lib)

# add asmjit library
target_link_libraries(test_asmjit PRIVATE asmjit)


install(TARGETS test_asmjit DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
