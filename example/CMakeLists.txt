cmake_minimum_required(VERSION 3.23)
cmake_policy(SET CMP0167 NEW)
project(example)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SOURCES src/*.cpp)
file(GLOB_RECURSE HEADERS include/*.h)

add_library(example_core)
target_sources(example_core
    PRIVATE
        ${SOURCES}
    PUBLIC
        FILE_SET myHeaders
        TYPE HEADERS
        BASE_DIRS include
        FILES
            ${HEADERS}
)
target_include_directories(example_core PUBLIC include)
target_compile_options(example_core PRIVATE -Wall -Wextra -Werror)
target_compile_features(example_core PRIVATE cxx_std_23)

add_executable(example src/main.cpp)
target_link_libraries(example PRIVATE example_core)
