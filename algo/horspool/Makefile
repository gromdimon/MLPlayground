CXX = /usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -g -Wall -pedantic -O2 -D_GLIBCXX_DEBUG -fsanitize=address

%.o: %.cpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp

horspool_main: horspool.o horspool_main.o
	${CXX} ${CXXFLAGS} -I . $^ -o horspool_main

horspool_test: horspool.o horspool_test.o
	${CXX} ${CXXFLAGS} -I . $^ -o horspool_test

