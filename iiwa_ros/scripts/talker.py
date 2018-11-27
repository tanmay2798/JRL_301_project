#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension
import random
def talker():
      	final_angle = [1,1,1,1,1,1,1,1,1]
	alpha = [-(math.pi)/2.0,(math.pi)/2.0,(math.pi)/2.0,-(math.pi)/2.0,-(math.pi)/2.0,(math.pi)/2.0,0]
	dist = [0.36,0,0.42,0,0.2,0,0.126]
	rospy.init_node('chatter',anonymous=True)
	pub = rospy.Publisher('/iiwa_command/command',Float64MultiArray,queue_size=10)
	rate = rospy.Rate(10)
	gold = Float64MultiArray()
	i=0
	while i<1000:
		gold.data = [0,0,0,0,0,0,0,0,0]
		pub.publish(gold)
		i=i+1;
	i=0

	while i<9:
		j=0;
		while gold.data[i]<final_angle[i]:
			j=j+1;
			gold.data[i] = j/10.0;
			pub.publish(gold)
			rospy.loginfo(gold)
			rospy.loginfo(i)
			rate.sleep()
		i=i+1;	
		rate.sleep()
	
	i=6
	X = [[math.cos(gold.data[i]),-math.sin(gold.data[i])*math.cos(alpha[i]),math.sin(gold.data[i])*math.sin(alpha[i]),0],[math.sin(gold.data[i]),math.cos(gold.data[i])*math.cos(alpha[i]),-math.cos(gold.data[i])*math.sin(alpha[i]),0],[0,math.sin(alpha[i]),math.cos(alpha[i]),dist[i]],[0,0,0,1]]
	while i>=0:
		
		Y = [[math.cos(gold.data[i-1]),-math.sin(gold.data[i-1])*math.cos(alpha[i-1]),math.sin(gold.data[i-1])*math.sin(alpha[i-1]),0],[math.sin(gold.data[i-1]),math.cos(gold.data[i-1])*math.cos(alpha[i-1]),-math.cos(gold.data[i-1])*math.sin(alpha[i-1]),0],[0,math.sin(alpha[i-1]),math.cos(alpha[i-1]),dist[i-1]],[0,0,0,1]]

		for p in range(len(X)):
	   		# iterate through columns of Y
	   			for j in range(len(Y[0])):
	     			  # iterate through rows of Y
	      				for k in range(len(Y)):
		  						X[p][j] += X[p][k] * Y[k][j]
		
		i=i-1;
		rospy.loginfo('hi')
		rospy.loginfo(i)
		rospy.loginfo(X)
		rate.sleep()
	
				

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass    
