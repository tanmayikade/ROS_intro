#!/usr/bin/env python3.8.10
import rospy
from std_msgs.msg import String
  
def publisher():
      
    pub = rospy.Publisher('chatter', String, queue_size=10)
   
    # initializing the publishing node
    rospy.init_node('publisher_dummy', anonymous=True)
      
    # lets define how many times per second
    # will the data be published
    # let's say 10 times/second or 10Hz
    rate = rospy.Rate(10)
    n=0
    # to keep publishing as long as the core is running, use while loop
    while not rospy.is_shutdown():
        data = "This is published - " + str(n)
          
        # you could simultaneously display the data
        # on the terminal and to the log file
        rospy.loginfo(data)
          
        # publish the data to the topic using publish()
        pub.publish(data)
          
        # keep a buffer based on the rate defined earlier
        rate.sleep()
        n=n+1
  
  
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
