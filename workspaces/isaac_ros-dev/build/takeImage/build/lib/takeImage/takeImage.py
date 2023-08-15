#! /usr/bin/python

#modified from https://gist.github.com/rethink-imcmahon/77a1a4d5506258f3dc1f



# rospy for the subscriber
import rclpy
from rclpy.node import Node
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2


class TakeImage(Node):
    def __init__(self):
        super().__init__("saveCSV")
        self.get_logger().info("running node takeImage")
        self.image_subscriber_ = self.create_subscription(Image, "/camera/color/image_raw", self.image_callback, 1)

    def image_callback(self, msg: Image):
        self.get_logger().info("saving image")
        bridge = CvBridge()
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg, "passthrough")
        except CvBridgeError as e:
            print(e)
        else:
            # Save your OpenCV2 image as a jpeg 
            cv2.imwrite('___CAM_IMAGE___.jpeg', cv2_img)
            self.get_logger().info("saved image")

        


def main(args = None):
    rclpy.init(args = args)
    node = TakeImage()
    rclpy.spin_once(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()







