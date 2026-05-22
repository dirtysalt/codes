# makefile.
SRCC=gcc
SRCXX=g++
LD_FLAGS=-L${HOME}/installed/lib -L${HOME}/installed/lib64
CK_FLAGS=-I./CK/ -I./CK/base/
SR_FLAGS=-I${STARROCKS_HOME}/be/src
INC_FLAGS=-I${HOME}/installed/include ${SR_FLAGS} ${CK_FLAGS} 
CXX_FLAGS=-std=c++20 -O3 -g -mavx2 -mavx512f
LIB_FLAGS=-lbenchmark -lbenchmark_main -lpthread
LIBCXX_FLAGS=-static-libstdc++ -static-libgcc
# LIBCXX_FLAGS=

SR_BUILD_TYPE=RELEASE
SR_INC_FLAGS=-I${TP_INSTALL_DIR}/include -I${STARROCKS_HOME}/gensrc/build/
SR_LIB_FLAGS= \
  ${STARROCKS_HOME}/be/output/tmp/${SR_BUILD_TYPE}/libExprs.a \
  ${STARROCKS_HOME}/be/output/tmp/${SR_BUILD_TYPE}/libUtil.a \
  ${STARROCKS_HOME}/be/output/tmp/${SR_BUILD_TYPE}/libGutil.a \
  ${STARROCKS_HOME}/be/output/tmp/${SR_BUILD_TYPE}/libCommon.a \
  ${TP_INSTALL_DIR}/lib/libprotobuf.a \
  ${TP_INSTALL_DIR}/lib64/libfmt.a \
  ${TP_INSTALL_DIR}/lib/libglog.a \
  ${TP_INSTALL_DIR}/lib/libgflags.a \
  ${TP_INSTALL_DIR}/lib/libre2.a \
  ${TP_INSTALL_DIR}/lib/libsimdjson.a \
  ${TP_INSTALL_DIR}/lib/libvelocypack.a \
  ${TP_INSTALL_DIR}/lib64/libbenchmark.a \
  ${TP_INSTALL_DIR}/lib64/libbenchmark_main.a \
  -lpthread

all: \
	hash_set_perf.exe \
	b2i_perf.exe \
	malloc_perf.exe \
	filter_range_perf.exe \
	filter_range_test.exe \
	runtime_filter_perf.exe \
	float_distance_perf.exe \
	libhdfs_perf.exe \
	libhdfs3_perf.exe \
	parse_json_perf.exe \
	python_udf_checker.exe \
	test_jni.exe

%.exe: %.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} ${LIB_FLAGS} ${LIBCXX_FLAGS}

libhdfs_perf.exe: libhdfs_perf.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS}  ${LD_FLAGS} -L$(JAVA_HOME)/lib/server ${HOME}/installed/lib/libhdfs.a -ljvm -lpthread ${LIBCXX_FLAGS}

libhdfs3_perf.exe: libhdfs_perf.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} -DLIBHDFS3 ${LD_FLAGS}  ${HOME}/installed/lib/libhdfs3.a ${HOME}/installed/lib/libprotobuf.a -lxml2 -lgsasl -lkrb5 -luuid -lpthread ${LIBCXX_FLAGS}

parse_json_perf.exe: parse_json_perf.cpp
	$(CXX) -o $@ $< ${SR_INC_FLAGS} ${INC_FLAGS} ${CXX_FLAGS} -O0 ${LD_FLAGS} ${SR_LIB_FLAGS} ${LIBCXX_FLAGS}

test_jni.exe: test_jni.cpp
	$(CXX) -o $@ $< ${INC_FLAGS} ${CXX_FLAGS} ${LD_FLAGS} libhdfs.a -L$(JAVA_HOME)/lib/server -ljvm ${LIBCXX_FLAGS}

clean:
	rm -rf *.exe perf.data*
