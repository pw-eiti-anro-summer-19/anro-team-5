#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import JointState

def talker():
	pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	d=0.0
	while not rospy.is_shutdown():
        	msg=JointState()
		msg.header.stamp=rospy.get_rostime()
		msg.name=['joint_0',"joint_1","joint_2"]
		msg.position=[math.sin(d),math.sin(d),math.sin(d)]
		pub.publish(msg)
		rate.sleep()
		d=d+0.1

if __name__=='__main__':
	try:
	    talker()
	except rospy.ROSInterruptException:
	    pass

