CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -Wall -pedantic -O2 -D_GLIBCXX_ASSERTIONS -g -fsanitize=address -fopenmp
# -D_GLIBCXX_DEBUG // bad for openmp performance

%.o: %.cpp blst_util.h BLAST_Neighborhood.hpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp
	
	
blst_main: BLAST_Neighborhood.o blst_main.o blst_util.o
	${CXX} ${CXXFLAGS} -I . $^ -o blst_main

blst_test: BLAST_Neighborhood.o blst_test.o blst_util.o
	${CXX} ${CXXFLAGS} -I . $^ -o blst_test
  