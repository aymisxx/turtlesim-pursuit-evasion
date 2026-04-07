#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class ChasingTurtle:
    def __init__(self):
        rospy.init_node('chasing_turtle', anonymous=True)

        # Declare a publisher for sending velocity commands to the chasing turtle
        self.pub = rospy.Publisher('/chasing_turtle/cmd_vel', Twist, queue_size=10)

        # Declare subscribers to get positions of both turtles
        rospy.Subscriber('/random_turtle/pose', Pose, self.random_turtle_callback)
        rospy.Subscriber('/chasing_turtle/pose', Pose, self.chasing_turtle_callback)

        self.random_turtle_pose = None
        self.chasing_turtle_pose = None
        self.rate = rospy.Rate(10)  # 10 Hz update rate

    def random_turtle_callback(self, msg):
        """Callback function to get the random turtle's position."""
        self.random_turtle_pose = msg

    def chasing_turtle_callback(self, msg):
        """Callback function to get the chasing turtle's position and initiate movement."""
        self.chasing_turtle_pose = msg
        self.chase()

    def chase(self):
        """Moves the chasing turtle towards the random turtle."""
        if self.random_turtle_pose is None or self.chasing_turtle_pose is None:
            return

        twist = Twist()
        dx = self.random_turtle_pose.x - self.chasing_turtle_pose.x
        dy = self.random_turtle_pose.y - self.chasing_turtle_pose.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0.5:  # Only move if the turtles are not already too close
            angle_to_target = math.atan2(dy, dx)
            twist.linear.x = min(1.5 * distance, 2.0)  # Cap the speed
            twist.angular.z = 2 * (angle_to_target - self.chasing_turtle_pose.theta)

        self.pub.publish(twist)

if __name__ == '__main__':
    try:
        turtle_chaser = ChasingTurtle()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
