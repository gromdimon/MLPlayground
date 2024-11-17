CXX=/usr/bin/g++
LDFLAGS =
CPPFLAGS = 
INC =
CXXFLAGS = -std=c++17 -Wall -pedantic -O3 -D_GLIBCXX_ASSERTIONS -g -fsanitize=address

%.o: %.cpp
	${CXX} ${CXXFLAGS} -I . -c $*.cpp
	

suftab_main: suftab.o suftab_main.o
	${CXX} ${CXXFLAGS} -I . $^ -o suftab_main

suftab_test: suftab.o suftab_test.o
	${CXX} ${CXXFLAGS} -I . $^ -o suftab_test
  
suftab_bench: suftab.o suftab_bench.o
	${CXX} ${CXXFLAGS} -I . $^ -o suftab_bench
