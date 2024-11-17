CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -Wall -pedantic -O2 -D_GLIBCXX_ASSERTIONS -g -fsanitize=address -fopenmp
# -D_GLIBCXX_DEBUG // bad for openmp performance


%.o: %.cpp QGramIndex.h
	${CXX} ${CXXFLAGS} -I . -c $*.cpp
	

qg_main: QGramIndex.o qg_main.o qg_util.o
	${CXX} ${CXXFLAGS} -I . $^ -o qg_main

qg_test: QGramIndex.o qg_test.o qg_util.o
	${CXX} ${CXXFLAGS} -I . $^ -o qg_test
  
