# Task1 for 1st Week
* Working with ubuntu 20.04 as VM
  - Install ROS
  - Install Pycharm or any Python IDE
  - Install TensorFlow
  - Install OpenCV
  
  
I'm Already Installed Ubuntu-20.04 on Virtualbox
So I will start to complete the tasks from here.

1. ### Then to Install Robot Operating System for Ubuntu 20.04 :
So Now to Install the Recommended Complete Bundle use:
``` sudo apt install ros-desktop-full ```

And to Initialize Rosedep Tool
``` sudo rosdep init ```
run this command  Update it: 
 ``` rosdep update ```

now we need to Setting Up Path 




2. ### To Install Pycharm 
Open a Terminal window and execution of the bellow command
```  sudo snap install pycharm-community --classic ``` 
PyCharm should be installed

start PyCharm by:
```  pycharm-community ``` 


##### Now if Python is not installed you can install it by :
 ```  sudo apt-get install python3 ``` 

3. ### To Install Tensorflow run the following commands :-

 
Then install python3 pip by -
``` sudo apt-get install python3-pip``` 

4. ### Now, Install Tensorflow by -
```  pip3 install tensorflow ```  


To Install OpenCV :-
```  sudo apt install python3-opencv ``` 

5. ###To verify the installation:
```  python3 -c "import cv2; print(cv2.__version__)" ```  

