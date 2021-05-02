#!/usr/bin/env python

import rospy
from champ_msgs.msg import ContactsStamped


global fl_contact
fl_contact = False

global fr_contact
fr_contact = False

global bl_contact
bl_contact = False

global br_contact
br_contact = False

def callback(data):
    global fl_contact
    global fr_contact
    global bl_contact
    global br_contact

    fl_contact = data.contacts[0]
    fr_contact = data.contacts[1]
    bl_contact = data.contacts[2]
    br_contact = data.contacts[3]
    print('------------------------------------')
    print('Front Left Leg - ' + str(fl_contact))
    print('Front Right Leg - ' + str(fr_contact))
    print('Back Left Leg - ' + str(bl_contact))
    print('Back Right Leg - ' + str(br_contact))
    # print(data.contacts)

def listener():
    rospy.init_node('Foot_bool', anonymous=True)
    rospy.Subscriber("foot_contacts", ContactsStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


