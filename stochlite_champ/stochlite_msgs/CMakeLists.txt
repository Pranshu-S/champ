cmake_minimum_required(VERSION 2.8.3)
project(stochlite_msgs)


include_directories(${catkin_INCLUDE_DIRS})
link_directories(${catkin_LIBRARY_DIRS})

find_package(catkin REQUIRED COMPONENTS 
rospy
roscpp
message_generation 
std_msgs
)


add_message_files(
  DIRECTORY msg
  FILES
  stoch_slope_esti.msg
  contact_foot.msg
)


generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)
