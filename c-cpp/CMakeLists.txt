cmake_minimum_required(VERSION 3.1)

project(Attention2Message)

# find_package(vector REQUIRED)

# add_library(name_of_dir SHARED name_of_files)

add_executable(attention2msg src/attention2msg.cpp)

# ----- only use this when add_library is used -----
# target_link_libraries(executable_file PUBLIC ${PROJECT_SOURCE_DIR}/include)
