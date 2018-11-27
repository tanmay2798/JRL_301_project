#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension
from sensor_msgs.msg import LaserScan
import random
def angle():
      
	rospy.init_node('chatter')
	pub = rospy.Publisher('/rrbot/laser/scan',LaserScan,queue_size=10)
	rate = rospy.Rate(10)
	gold = LaserScan()
	i=0
	while not rospy.is_shutdown():
		
		#gold1 = MultiArrayDimension()
		i=i+1;
		#gold.ranges = [0,-i/100,-i/5000,i/10,i/20,0,0,i/10,-i/10]
		#pub.publish(gold)
		rospy.loginfo(gold.ranges)
		#rospy.loginfo(gold.ranges[0])
		rate.sleep()
		

if __name__ == '__main__':
	try:
		angle()
	except rospy.ROSInterruptException:
		pass    
