#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def roll():
	pub = rospy.Publisher("combo",String,queue_size=10)
	rospy.init_node("roll", anonymous=True)
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		hello_str = "190100051_190110043"
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		roll()
	except rospy.ROSInterruptException:
		pass
