## -To Create a ROS workspace


* A ROS workspace build by the following commands:
``` $ mkdir -p ~/catkin_ws/src ```
 ``` $ cd ~/catkin_ws/ ```
``` $ catkin_make ```  
* source the new setup.*sh file by:
``` $ source devel/setup.bash ```
* run  ```echo $ROS_PACKAGE_PATH ``` to make sure your workspace is properly overlayed by the setup script.
 
## -To Create a new package

#### Each package must have its own folder and The package must contain a catkin compliant package.xml file provides meta information about the package and CMakeLists.txt which uses catkin.

* To create a new catkin package move to catkin workspace you created by : 
```$ cd ~/catkin_ws/src```
* use the catkin_create_pkg to create a new package called 'my-pkg' which depends on std_msgs and rospy:
``` $ catkin_create_pkg my-pkg std_msgs rospy```
* you need to build the packages in the catkin workspace by:
 ``` $ cd ~/catkin_ws ``` 
 ``` $ catkin_make ``` 
* add the workspace to your ROS environment you need to source the generated setup file:
``` $ . ~/catkin_ws/devel/setup.bash```

## - Create publisher & subscriber nodes using Python
### 1. Writing the Publisher Node :
##### we will make a publisher called "talker" and subscriber called "listener".

* First Change directory into the package by:
``` $ roscd my-pkg ```
* create a 'scripts' folder to store our Python scripts in:
``` $ mkdir scripts ```
  ```  $ cd scripts ```
* Then write your own Publisher Node code or download the example script talker.py to your new scripts directory and make it executable by :
``` $ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py ```
``` $ chmod +x talker.py ```

### 2. Writing the Subscriber Node
* write your own Subscriber Node code or Download the listener.py file into your scripts directory:
``` $ roscd my-pkg/scripts/ ```
``` $ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py ```
``` $ chmod +x listener.py ```

* Then, edit the catkin_install_python() call in your CMakeLists.txt so it looks like the following:
```
catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
) 
```


## -Running the publisher and subscriber.
* run ``` $ roscore ``` to make sure is ros up aand running 
* move to your catkin workspace and source your workspace's setup.sh file by : 
 ```$ cd ~/catkin_ws ```
``` $ source ./devel/setup.bash ```

#### * 1. Running the Publisher
``` $ rosrun my-pkg talker.py ```   or move to the scripts folder then run ```Python3 talker.py ```
#### * 2. Running the Subscriber
``` $ rosrun my-pkg listener.py```  or move to the scripts folder then run ``` Python3 listener.py``` 
