CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -Wall -pedantic -O2 -D_GLIBCXX_ASSERTIONS -g -fsanitize=address
# -D_GLIBCXX_DEBUG // bad for openmp performance


%.o: %.cpp ACTrie.hpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp


act_main: ACTrie.o act_main.o
	${CXX} ${CXXFLAGS} -I . $^ -o act_main

act_test: ACTrie.o act_test.o
	${CXX} ${CXXFLAGS} -I . $^ -o act_test

