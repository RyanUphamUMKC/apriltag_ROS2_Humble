from launch import LaunchDescription
from launch_ros.actions import Node




def generate_launch_description():
    return LaunchDescription([
        Node(
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag',
            remappings=[
                ('image_rect', '/camera/color/image_raw'),
                ('camera_info','/camera/color/camera_info'),
            ]
        ),
    ])