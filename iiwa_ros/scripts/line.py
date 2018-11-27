#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
import time


def scan_callback(msg):
	global g_range_ahead
	global ang_turn
	g_range_ahead = min(msg.ranges)
	clr =  msg.ranges.index(max(msg.ranges))
	#ang = msg.angle_min + (msg.angle_max-msg.angle_min)/len(msg.ranges)*clr
	#ang_turn=ang
	#rospy.loginfo(ang)

def callback(data):
	global distancex
	global distancey 
	global angle
	distancex = data.pose.pose.position.x
	distancey = data.pose.pose.position.y
	angle = data.pose.pose.orientation.z

distancex = 1
distancey = 1	
angle=1
ang_turn=1
g_range_ahead = 1 # anything to start
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.loginfo(g_range_ahead)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('red_light_green_light',anonymous=True)
start = rospy.Time.now()
driving_forward = True
state_change_time = rospy.Time.now()#-rospy.Time.now()
rate = rospy.Rate(10)
last=angle
state=0;

while not rospy.is_shutdown():
	rospy.loginfo(g_range_ahead)
	#rospy.loginfo(ang_turn)
	rospy.loginfo(distancex)
	rospy.loginfo(distancey)
	

	#ssssrospy.loginfo(rospy.Duration(5))
	twist = Twist()
	rospy.Subscriber('odom',Odometry,callback)
	#rospy.spin()

	if (g_range_ahead < 1):
		driving_forward=False
	'''else:
		driving_forward=True'''
	
	if driving_forward:
		twist.linear.x = 1
		last = angle
		start = rospy.Time.now()
	#elif distancex<6.0:
	else:

		if distancex>4.0 and distancey>4.0:
			twist.angular.z = 0.3

		elif distancex < 2.0 or distancey > 4.0:
			twist.angular.z = -0.3
			#rospy.loginfo(distance)
			#rospy.loginfo('hi')
		elif distancey<2.5 and distancex<5.0:
			twist.angular.z=-0.3
		else:
			twist.angular.z = 0.3
			#rospy.loginfo(distance)
			#rospy.loginfo('yo')


		if g_range_ahead>1.2:
			driving_forward=True
	#else:
	#	twist.angular.z=0.3
		

	cmd_vel_pub.publish(twist)

	rospy.loginfo(twist)
	rate.sleep()

'''else:
		if state==0:
			if (g_range_ahead >1.5):
				driving_forward=True
		if state==1:
			if (g_range_ahead >1):
				driving_forward=True
		
		if rospy.Time.now() - start <=rospy.Duration(4) and state==0:
			twist.angular.z = 0.3
		else:
			twist.angular.z = -0.3
			state=1'''
