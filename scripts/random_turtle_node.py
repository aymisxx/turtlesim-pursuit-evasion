#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Twist

def move_random_turtle():
    rospy.init_node('random_turtle_node', anonymous=True)
    
   
    import rospy
from geometry_msgs.msg import Twist
import random

def random_movement():
    rospy.init_node('random_turtle', anonymous=True)
    pub = rospy.Publisher('/random_turtle/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = random.uniform(0, 2)  # Random speed
        twist.angular.z = random.uniform(-2, 2)  # Random rotation
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        random_movement()
    except rospy.ROSInterruptException:
        pass

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
