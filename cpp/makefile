# *****************************************************
# Variables to control Makefile operation

CXX = g++
CXXFLAGS = -Wall -g -std=c++0x

main: main.o
	$(CXX) $(CXXFLAGS) -o main main.cpp linked_list.hpp camels.cpp

ifeq ("x", "y")
main: main.o camels.o
	$(CXX) $(CXXFLAGS) -o main main.o camels.o

main.o: main.cpp linked_list.hpp camels.hpp 
	$(CXX) $(CXXFLAGS) -c main.cpp 

linked_list.hpp: 
	$(CXX) $(CXXFLAGS) -c linked_list.hpp 

camels.o: camels.hpp 
	$(CXX) $(CXXFLAGS) -c camels.cpp

clean:
	rm -rf main.o camels.o
endif
