#!/usr/bin/env python3.8.10
import rospy
from geometry_msgs.msg  import Twist
import numpy as np
  
k = np.random.normal(size=(20300))
i= -1
p = Twist()
    
def callback(data):
    
    rospy.loginfo("No noise data.linear.x = %s", data.linear.x)
    global i
    i += 1
    
    p.linear.x = data.linear.x + k[i]
    p.linear.y = data.linear.y + k[i]
    p.linear.z = data.linear.z + k[i]
    
    p.angular.x = data.angular.x + k[i]
    p.angular.y = data.angular.y + k[i]
    p.angular.z = data.angular.z + k[i]
   
    
    rospy.loginfo("After adding noise = %s", p.linear.x )
    rospy.loginfo("%s ", p.linear.y )
    rospy.loginfo("%s ", p.linear.z )
    rospy.loginfo("%s ", p.angular.x )
    rospy.loginfo("%s ", p.angular.y )
    rospy.loginfo("%s ", p.angular.z )
    

def subs_bot():

    rospy.init_node('subs_bot', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback)
    
    rate = rospy.Rate(10)
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    
    while not rospy.is_shutdown():
        pub.publish(p)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    subs_bot()
