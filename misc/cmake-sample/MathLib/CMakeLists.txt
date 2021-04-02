add_library(MathLib mathlib.c)

target_include_directories(MathLib
  # 如果外部使用这个lib的话，会在-I这里把这个dir加入进来
  # 然后直接使用目录里面的路径就行了，这样在外面就可以简化配置
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
  )

install(TARGETS MathLib DESTINATION lib)
install(FILES mathlib.h DESTINATION include)