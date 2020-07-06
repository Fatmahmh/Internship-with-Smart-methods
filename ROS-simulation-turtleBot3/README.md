### TurtleBot3 simulator

##### 1. To install the dependent packages run :
``` cd ~/catkin_ws/src/ ``` 

 ``` git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git ``` 
 
``` git clone https://github.com/ROBOTIS-GIT/turtlebot3.git ```

``` cd ~/catkin_ws && catkin_make ```

##### TurtleBot3 has three models, you have to set which model you want to use before you launch TurtleBot3 by add this line at the bottom of the file:
``` gedit ~/.bashrc ```

``` export TURTLEBOT3_MODEL=burger ```
###### reload .bashrc so that you do not have to log out and log back in.
``` source ~/.bashrc ```

##### 2. to download the TurtleBot3 simulation files.
``` cd ~/catkin_ws/src/ ```

``` git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git ```

``` cd ~/catkin_ws && catkin_make ```

#### 3. To launch the virtual robot using Gazebo

###### First,launch TurtleBot3 in an empty environment by : 

``` roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch ```

![myimage-alt-tag](https://github.com/Fatmahmh/Internship-with-Smart-methods/blob/master/ROS-simulation-turtleBot3/outup.PNG
) 


 ###### 4. to control the movement of your TurtleBot 

![myimage-alt-tag](https://github.com/Fatmahmh/Internship-with-Smart-methods/blob/master/ROS-simulation-turtleBot3/output2.PNG
) 

 <iframe src="url video in google drive/preview" ></iframe>
 <iframe allowfullscreen="allowfullscreen" src="https://drive.google.com/file/d/1GKe_pZYlBWLd-BUhvMF0lplc7uzU8q8o/view?usp=sharing" ></iframe>

