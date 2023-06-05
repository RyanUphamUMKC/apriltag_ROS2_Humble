from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    package_prefix_april = get_package_share_directory('apriltag_ros')
    package_prefix_realsense = get_package_share_directory('realsense2_camera')

    return LaunchDescription([
    
        # include the child launch file
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([package_prefix_april, '/launch/apriltag.launch.py']),
            ),
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([package_prefix_realsense, '/launch/rs_launch.py']),
            ),
    ])