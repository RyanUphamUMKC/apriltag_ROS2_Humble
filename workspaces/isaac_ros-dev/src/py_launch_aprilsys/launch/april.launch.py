

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

print("comedy")

def generate_launch_description():
    package_prefix_april = get_package_share_directory('isaac_ros_apriltag')
    package_prefix_realsense = get_package_share_directory('realsense2_camera')
    print(package_prefix_april)

    return LaunchDescription([
    
        # include the child launch file
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([package_prefix_april+ '/launch/isaac_ros_apriltag.launch.py']),
            
            ),
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([package_prefix_realsense, '/launch/rs_launch.py']),
            
            ),
            
            
            #Node(
            #package='py_launch_aprilsys',
            #executable='SaveCSV.py',
            #name='saveCSV',
        #),
    ])
