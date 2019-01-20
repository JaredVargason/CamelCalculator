# *****************************************************
# Variables to control Makefile operation

CXX = g++
CXXFLAGS = -Wall -g -std=c++0x

ifeq ("x", "y")
main:
	$(CXX) $(CXXFLAGS) linked_list.cpp camels.cpp main.cpp 
endif

main: main.o linked_list.o camels.o
	$(CXX) $(CXXFLAGS) -o main main.o linked_list.o camels.o

main.o: main.cpp linked_list.hpp camels.hpp 
	$(CXX) $(CXXFLAGS) -c main.cpp 

linked_list.o: linked_list.hpp
	$(CXX) $(CXXFLAGS) -c linked_list.cpp

camels.o: camels.hpp 
	$(CXX) $(CXXFLAGS) -c camels.cpp
clean:
	rm -rf main.o camels.o linked_list.o