cmake_minimum_required(VERSION 3.10)

project(Elevator CXX)
set(CMAKE_CXX_STANDARD 17)

enable_testing()

add_subdirectory(libElevator)
add_subdirectory(Elevator)
add_subdirectory(Elevator-test)
