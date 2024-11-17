CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -g -Wall -pedantic -O2 -D_GLIBCXX_DEBUG -fsanitize=address

%.o: %.cpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp

align_main: Alignment.o align_main.o
	${CXX} ${CXXFLAGS} -I . $^ -o align_main

align_test: Alignment.o align_test.o
	${CXX} ${CXXFLAGS} -I . $^ -o align_test

