add_library(libElevator elevator.h elevator.cpp)

target_include_directories(libElevator PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
