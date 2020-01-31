cmake_minimum_required(VERSION 3.10)

project(Hangout2 CXX)
set(CMAKE_CXX_STANDARD 17)

enable_testing()

add_subdirectory(libHangout2)
add_subdirectory(Hangout2)
add_subdirectory(Hangout2-test)
