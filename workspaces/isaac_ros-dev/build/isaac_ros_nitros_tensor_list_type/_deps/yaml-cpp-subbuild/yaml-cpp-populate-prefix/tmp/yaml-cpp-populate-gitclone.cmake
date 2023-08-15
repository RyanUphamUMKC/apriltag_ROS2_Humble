# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

if(EXISTS "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitclone-lastrun.txt" AND EXISTS "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitinfo.txt" AND
  "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitclone-lastrun.txt" IS_NEWER_THAN "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitinfo.txt")
  message(STATUS
    "Avoiding repeated git clone, stamp file is up to date: "
    "'/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitclone-lastrun.txt'"
  )
  return()
endif()

execute_process(
  COMMAND ${CMAKE_COMMAND} -E rm -rf "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-src"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to remove directory: '/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-src'")
endif()

# try the clone 3 times in case there is an odd git clone issue
set(error_code 1)
set(number_of_tries 0)
while(error_code AND number_of_tries LESS 3)
  execute_process(
    COMMAND "/usr/bin/git" 
            clone --no-checkout --config "advice.detachedHead=false" "https://github.com/jbeder/yaml-cpp.git" "yaml-cpp-src"
    WORKING_DIRECTORY "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps"
    RESULT_VARIABLE error_code
  )
  math(EXPR number_of_tries "${number_of_tries} + 1")
endwhile()
if(number_of_tries GREATER 1)
  message(STATUS "Had to git clone more than once: ${number_of_tries} times.")
endif()
if(error_code)
  message(FATAL_ERROR "Failed to clone repository: 'https://github.com/jbeder/yaml-cpp.git'")
endif()

execute_process(
  COMMAND "/usr/bin/git" 
          checkout "yaml-cpp-0.6.3" --
  WORKING_DIRECTORY "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-src"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to checkout tag: 'yaml-cpp-0.6.3'")
endif()

set(init_submodules TRUE)
if(init_submodules)
  execute_process(
    COMMAND "/usr/bin/git" 
            submodule update --recursive --init 
    WORKING_DIRECTORY "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-src"
    RESULT_VARIABLE error_code
  )
endif()
if(error_code)
  message(FATAL_ERROR "Failed to update submodules in: '/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-src'")
endif()

# Complete success, update the script-last-run stamp file:
#
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitinfo.txt" "/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitclone-lastrun.txt"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to copy script-last-run stamp file: '/workspaces/isaac_ros-dev/build/isaac_ros_nitros_tensor_list_type/_deps/yaml-cpp-subbuild/yaml-cpp-populate-prefix/src/yaml-cpp-populate-stamp/yaml-cpp-populate-gitclone-lastrun.txt'")
endif()
