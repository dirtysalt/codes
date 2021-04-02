add_library(MathLib mathlib.c ${CMAKE_CURRENT_BINARY_DIR}/primes.h)

target_include_directories(MathLib
  # 如果外部使用这个lib的话，会在-I这里把这个dir加入进来
  # 然后直接使用目录里面的路径就行了，这样在外面就可以简化配置
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
  PRIVATE ${CMAKE_CURRENT_BINARY_DIR}
  )

# 如果按照shared libs来编译的话，编译开关就会打开-fPIC
set_target_properties(MathLib PROPERTIES
  POSITION_INDEPENDENT_CODE ${BUILD_SHARED_LIBS}
  )

install(TARGETS MathLib  DESTINATION lib)
install(FILES mathlib.h DESTINATION include)

include(CheckSymbolExists)
check_symbol_exists(log "math.h" HAVE_LOG)
check_symbol_exists(exp "math.h" HAVE_EXP)
if(NOT (HAVE_LOG AND HAVE_EXP))
  unset(HAVE_LOG CACHE)
  unset(HAVE_EXP CACHE)
  set(CMAKE_REQUIRED_LIBRARIES "m")
  check_symbol_exists(log "math.h" HAVE_LOG)
  check_symbol_exists(exp "math.h" HAVE_EXP)
  if(HAVE_LOG AND HAVE_EXP)
    target_link_libraries(MathLib PRIVATE m)
  endif()
endif()

if(HAVE_LOG AND HAVE_EXP)
  target_compile_definitions(MathLib
    PRIVATE "HAVE_LOG" "HAVE_EXP")
endif()

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/primes.h
  COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/../tools/genprimes.py ${CMAKE_CURRENT_BINARY_DIR}/primes.h
  # DEPENDS <target>
  )

target_compile_options(MathLib PRIVATE -W -Wall)