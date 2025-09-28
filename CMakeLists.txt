cmake_minimum_required(VERSION 3.10)
project(OpenCV)
find_package(OpenCV REQUIRED)
include_directories(include ${OpenCV_INCLUDE_DIRS})
add_executable(add_executable src/main.cpp src/imagep.cpp)

target_link_libraries(add_executable ${OpenCV_LIBS})
