#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def name():
	pub = rospy.Publisher("combo",String,queue_size=10)
	rospy.init_node("name", anonymous=True)
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		hello_str = "Gyandev_Manan"
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		name()
	except rospy.ROSInterruptException:
		pass
