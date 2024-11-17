CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -Wall -pedantic -O2 -D_GLIBCXX_ASSERTIONS -g -fsanitize=address
# -D_GLIBCXX_DEBUG // bad for openmp performance

%.o: %.cpp PDA.hpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp
	

pda_main: PDA.o pda_main.o
	${CXX} ${CXXFLAGS} -I . $^ -o pda_main

pda_test: PDA.o pda_test.o
	${CXX} ${CXXFLAGS} -I . $^ -o pda_test
  