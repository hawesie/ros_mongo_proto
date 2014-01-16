#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point, Quaternion

def talker():
    chat = rospy.Publisher('chatter', String)
    pose = rospy.Publisher('poser', Pose)
    rospy.init_node('talker')
    count = 0
    while not rospy.is_shutdown():
        str = "hello world %s" % rospy.get_time()
        rospy.loginfo(str)
        chat.publish(String(str))
        p = Pose(Point(count, count, count), Quaternion(count, count,  count, count))
        pose.publish(p)
        rospy.sleep(1.0)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
