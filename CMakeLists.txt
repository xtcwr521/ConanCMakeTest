cmake_minimum_required(VERSION 3.5)

project(CMakeConanTest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CONFIGURATION_TYPES "Release;RelWithDebInfo;Debug" CACHE STRING "" FORCE)
set(CMAKE_PREFIX_PATH CONAN_CMAKE_MODULE_PATH)
set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

find_package(nlohmann_json)
find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_subdirectory(lib)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE MyLib nlohmann_json::nlohmann_json)
