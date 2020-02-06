cmake_minimum_required(VERSION 3.10)

project(projectx CXX)
set(CMAKE_CXX_STANDARD 17)

enable_testing()

add_subdirectory(libprojectx)
add_subdirectory(projectx)
add_subdirectory(projectx-test)
