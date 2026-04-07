#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class ChasingTurtle:
    def __init__(self):
        rospy.init_node('chasing_turtle_node', anonymous=True)
        
        self.random_turtle_pose = Pose()
        self.chasing_turtle_pose = Pose()
        
        self.pub = # Step 3: Declare a publisher to the topic controlling chasing turtlebot velocity.
        
        # Step 4: Subscribe to the topic publishing random turtlebot pose.
        
        # Step 5: Subscribe to the topic publishing chasing turtlebot pose.
        
        
        self.rate = rospy.Rate(10)

    def random_turtle_callback(self, msg):
        self.random_turtle_pose = msg

    def chasing_turtle_callback(self, msg):
        self.chasing_turtle_pose = msg

    def move(self):
        while not rospy.is_shutdown():
            distance = # Step 6: Calculate the distance between the chasing turtlebot and the random turtlebot.
            angle_to_goal = math.atan2(self.random_turtle_pose.y - self.chasing_turtle_pose.y,
                                     self.random_turtle_pose.x - self.chasing_turtle_pose.x)

            vel_msg = Twist()
            vel_msg.linear.x = min(1.5, 1.5 * distance)
            vel_msg.angular.z = 2.0 * (angle_to_goal - self.chasing_turtle_pose.theta)

            self.pub.publish(vel_msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        chaser = ChasingTurtle()
        chaser.move()
    except rospy.ROSInterruptException:
        pass