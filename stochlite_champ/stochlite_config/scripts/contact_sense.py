#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ContactsState
from stochlite_msgs.msg import contact_foot
#from geometry_msgs.msg import Vector3

# global count

global states
states = contact_foot()
states.bl_contact = True
states.fl_contact = True
states.fr_contact = True
states.br_contact = True

def callback_fl(data):
    global states
    # print(states)
    # print(data.states)
    if len(data.states) != 0:
        # print("True")
        states.fl_contact = True
    else:
        # print("False")
        states.fl_contact = False
    
def callback_fr(data):
    global states
    # print(states)
    # print(data.states)
    if len(data.states) != 0:
        # print("True")
        states.fr_contact = True
    else:
        # print("False")
        states.fr_contact = False

def callback_bl(data):
    global states
    # print(states)
    # print(data.states)
    if len(data.states) != 0:
        # print("True")
        states.bl_contact = True
    else:
        # print("False")
        states.bl_contact = False

def callback_br(data):
    global states
    # print(states)
    # print(data.states)
    if len(data.states) != 0:
        # print("True")
        states.br_contact = True
    else:
        # print("False")
        states.br_contact = False
 
def listener():

   
    rospy.init_node('contact_sense', anonymous=True)

    rospy.Subscriber('/fl_contact',ContactsState,callback_fl)
    rospy.Subscriber('/fr_contact',ContactsState,callback_fr)
    rospy.Subscriber('/bl_contact',ContactsState,callback_bl)
    rospy.Subscriber('/br_contact',ContactsState,callback_br)

    contact_publisher = rospy.Publisher('contact_var',contact_foot, queue_size = 10)
    rate = rospy.Rate(100)
    global states
    while not rospy.is_shutdown():
        contact_publisher.publish(states)
        rate.sleep()

   
    
    rospy.spin()

if __name__ == '__main__':
    listener()
