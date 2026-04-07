#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Twist

def move_random_turtle():
    rospy.init_node('random_turtle_node', anonymous=True)
    
   
    pub = # Step 1: Declare a publisher to the topic controlling random turtlebot velocity.
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = random.uniform(1.5, 2.5)
        vel_msg.angular.z = random.uniform(-2.0, 2.0)
        # Step 2: Publish the velocity message to the topic.
        
        rate.sleep()

if __name__ == '__main__':
    try:
        move_random_turtle()
    except rospy.ROSInterruptException:
        pass
