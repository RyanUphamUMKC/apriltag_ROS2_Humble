# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_isaac_ros_nitros_tensor_list_type_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED isaac_ros_nitros_tensor_list_type_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(isaac_ros_nitros_tensor_list_type_FOUND FALSE)
  elseif(NOT isaac_ros_nitros_tensor_list_type_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(isaac_ros_nitros_tensor_list_type_FOUND FALSE)
  endif()
  return()
endif()
set(_isaac_ros_nitros_tensor_list_type_CONFIG_INCLUDED TRUE)

# output package information
if(NOT isaac_ros_nitros_tensor_list_type_FIND_QUIETLY)
  message(STATUS "Found isaac_ros_nitros_tensor_list_type: 0.31.0 (${isaac_ros_nitros_tensor_list_type_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'isaac_ros_nitros_tensor_list_type' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${isaac_ros_nitros_tensor_list_type_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(isaac_ros_nitros_tensor_list_type_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "ament_cmake_export_dependencies-extras.cmake;ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake")
foreach(_extra ${_extras})
  include("${isaac_ros_nitros_tensor_list_type_DIR}/${_extra}")
endforeach()
