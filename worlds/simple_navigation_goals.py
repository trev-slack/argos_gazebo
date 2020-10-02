#!/usr/bin/env python
__author__ = "Trevor Slack"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Trevor Slack"
__email__ = "trevor.slack@colorado.edu"
__status__ = "prototype"

import rospy
import sys
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



class Waypoint():
	def __init__(self,args):
		#set arg values
		self.namespace = args[1]
		self.x = args[2]
		self.y = args[3]
		self.theta = args[4]
		#initialize client
		self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
		self.main()



	def main(self):
		""" Publish waypoints in the form of MoveBase Action messages
		requries args:
			x = x location [m]
			y = y location [m]
			theta = z roation [rad]
			namespace = namespace of robot
		"""
















if __name__ == "__main__":
	#take in args
	if len(sys.args)<5:
		print("usage: simple_naviagtion_goals.py namespace x y theta")
	else:
		try:
			#create node
			rospy.init_node('argos_waypoint_node',anonymous=True)
			#create waypoint class
			myWaypoint = Waypoint(sys.args)
		#node interrupted
		except rospy.ROSInterruptException:
			pass
