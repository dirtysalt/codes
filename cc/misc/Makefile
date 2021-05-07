all:
	@echo "make {program}.exe"

PYTHON=/usr/include/python2.7/
CXXFLAGS=-std=c++11 -fPIC -g -O2

runnable_so.exe:runnable_so.cc
	g++ -o $@ $(CXXFLAGS)  -shared -e so_main $^

test_pye.so: test_pye.cc
	g++ -o $@ $(CXXFLAGS) -I$(PYTHON)-shared -lboost_python $^

clean:
	rm -rf *.exe *.o *.so *.dSYM
