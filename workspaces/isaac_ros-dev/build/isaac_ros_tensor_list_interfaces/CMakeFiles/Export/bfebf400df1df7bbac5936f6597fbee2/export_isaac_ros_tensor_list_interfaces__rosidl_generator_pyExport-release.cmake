#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "isaac_ros_tensor_list_interfaces::isaac_ros_tensor_list_interfaces__rosidl_generator_py" for configuration "Release"
set_property(TARGET isaac_ros_tensor_list_interfaces::isaac_ros_tensor_list_interfaces__rosidl_generator_py APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(isaac_ros_tensor_list_interfaces::isaac_ros_tensor_list_interfaces__rosidl_generator_py PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libisaac_ros_tensor_list_interfaces__rosidl_generator_py.so"
  IMPORTED_SONAME_RELEASE "libisaac_ros_tensor_list_interfaces__rosidl_generator_py.so"
  )

list(APPEND _cmake_import_check_targets isaac_ros_tensor_list_interfaces::isaac_ros_tensor_list_interfaces__rosidl_generator_py )
list(APPEND _cmake_import_check_files_for_isaac_ros_tensor_list_interfaces::isaac_ros_tensor_list_interfaces__rosidl_generator_py "${_IMPORT_PREFIX}/lib/libisaac_ros_tensor_list_interfaces__rosidl_generator_py.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
