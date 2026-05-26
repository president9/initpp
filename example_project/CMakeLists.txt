cmake_minimum_required(VERSION 3.23)
cmake_policy(SET CMP0167 NEW)
project(example_project)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SOURCES src/*.cpp)
file(GLOB_RECURSE HEADERS include/*.h)

add_library(example_project_core)
target_sources(example_project_core
    PRIVATE
        ${SOURCES}
    PUBLIC
        FILE_SET myHeaders
        TYPE HEADERS
        BASE_DIRS include
        FILES
            ${HEADERS}
)
target_include_directories(example_project_core PUBLIC include)
target_compile_options(example_project_core PRIVATE -Wall -Wextra -Werror)
target_compile_features(example_project_core PRIVATE cxx_std_23)

add_executable(example_project src/main.cpp)
target_link_libraries(example_project PRIVATE example_project_core)
