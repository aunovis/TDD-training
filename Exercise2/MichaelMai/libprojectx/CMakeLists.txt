add_library(libprojectx example.cpp example.h Rover.h)

target_include_directories(libprojectx PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
