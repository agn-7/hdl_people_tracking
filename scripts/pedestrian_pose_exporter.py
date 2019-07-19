#!/usr/bin/env python

import rospy

from visualization_msgs.msg import MarkerArray
from sensor_msgs.msg import PointCloud2


__author__ = 'aGn'

PATH_TO_SAVE = rospy.get_param('/hdl_people_tracking/path_to_save')
MARKER_TOPIC = rospy.get_param('/hdl_people_tracking/marker_topic')


class PoseExporter(object):
    def __init__(self):
        self.frame = 0
        print("The .csv files store in " + PATH_TO_SAVE)
        rospy.Subscriber(MARKER_TOPIC, MarkerArray, self.export_pose, queue_size=1)
        rospy.Subscriber("/velodyne_points", PointCloud2, self.get_frame, queue_size=1)

    def get_frame(self, pcl):
        self.frame += 1

    def export_pose(self, marker):
        print(self.frame)
        print(marker.markers[0].header.frame_id)
        print(marker.markers[0].pose.position)

        # with open(PATH_TO_SAVE + 'groundtruth_lineara.csv', mode='a') as file_:
        #     file_.write("{},{},{}".format(self.frame, pose_x_1, pose_y_1))
        #     file_.write("\n")
        #
        # with open(PATH_TO_SAVE + 'groundtruth_rotary.csv', mode='a') as file_:
        #     file_.write("{},{},{}".format(self.frame, pose_x_2, pose_y_2))
        #     file_.write("\n")


if __name__ == "__main__":
    rospy.init_node('hdl_people_tracking', anonymous=True)
    PoseExporter()
    rospy.spin()
