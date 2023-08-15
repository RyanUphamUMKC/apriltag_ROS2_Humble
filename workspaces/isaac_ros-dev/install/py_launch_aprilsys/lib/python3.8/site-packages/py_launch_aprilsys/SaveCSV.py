#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
import tf2_ros
from tf2_ros import Buffer
from tf2_ros import TransformListener
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Transform
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Vector3
import numpy as np
#import ros2_numpy.ros2_numpy as np



class SaveCSV(Node):
    def __init__(self):
        super().__init__("saveCSV")
        self.get_logger().info("hello world")
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.transform_subscriber_ = self.create_subscription(TFMessage, "/tf", self.transform_callback, 10)

    def transform_callback(self, msg: TFMessage):
        
        #self.tf_buffer = Buffer()
        xVal = msg.transform
        print(xVal)
        print("------\n")
        print(type(xVal))
        print("------\n")
        if len(xVal) > 0:
            print(type(xVal[0]))
            print("------\n")
        
        t = self.tf_Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        

        #self.get_logger().info(msg)


def main(args = None):
    rclpy.init(args = args)
    node = SaveCSV()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()














    import sys
import math

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from tf2_ros.transform_listener import TransformListener
from tf2_ros.buffer import Buffer
from tf2_ros import LookupException

class TfListener(Node):

    def __init__(self, first_turtle, second_turtle):
        super().__init__('tf_listener')
        self.first_name_ = first_turtle
        self.second_name_ = second_turtle
        self.get_logger().info("Transforming from {} to {}".format(self.second_name_, self.first_name_))
        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, self)
        self.cmd_ = Twist ()
        self.publisher_ = self.create_publisher(Twist, "{}/cmd_vel".format(self.second_name_),10)
        self.timer = self.create_timer(0.33, self.timer_callback) #30 Hz = 0.333s

    def timer_callback(self):
        try:
            trans = self._tf_buffer.lookup_transform(self.second_name_, self.first_name_, rclpy.time.Time())
            self.cmd_.linear.x = math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)
            self.cmd_.angular.z = 4 * math.atan2(trans.transform.translation.y , trans.transform.translation.x)
            self.publisher_.publish(self.cmd_)

            #I want you to listen to the transformation

        except LookupException as e:
            self.get_logger().error('failed to get transform {} \n'.format(repr(e)))

def main(argv=sys.argv):
    rclpy.init(args=argv)
    node = TfListener(sys.argv[1], sys.argv[2])
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
