cmake_minimum_required(VERSION 3.23)
cmake_policy(SET CMP0167 NEW)
project({name})
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

{find_packages}

file(GLOB_RECURSE SOURCES src/*.cpp)
file(GLOB_RECURSE HEADERS include/*.h)

add_library({name}_core)

target_sources({name}_core
    PRIVATE
        ${{SOURCES}}
    PUBLIC
        FILE_SET myHeaders
        TYPE HEADERS
        BASE_DIRS include
        FILES
            ${{HEADERS}}
)
target_include_directories({name}_core PUBLIC include)
target_compile_options({name}_core PRIVATE -Wall -Wextra -Werror)
target_compile_features({name}_core PRIVATE cxx_std_23)

{link_libraries}

add_executable({name} src/main.cpp)
target_link_libraries({name} PRIVATE {name}_core)
