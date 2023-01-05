# face_detect_ROS2
### In this repository face is detected by *haarcascade* then this information publising to rostopics with using *ROS2*.

<h1>
  <div id="header" align="center">
  <img src="https://user-images.githubusercontent.com/68682737/210886289-a761c854-bee2-480f-9f83-a717a3d4491d.png" width="500" height="350">
  <img src="https://user-images.githubusercontent.com/68682737/210888136-6ae516ed-e714-4061-a6f1-d313e5086d77.png" width="500" height="350">
    </div>
</h1>


## Requirements:
- OpenCV 2.x, 3.x, 4.x

- ![haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- ROS2 
To communicate ROS2 and our face detection python scripts,we should create basic publisher in our code.![Writing a simple publisher and subscriber (Python)](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html). When face is detected this information will publish to topic.
![Screenshot from 2023-01-06 00-40-44](https://user-images.githubusercontent.com/68682737/210890293-3338fb49-cba1-458a-be15-e4f1ce74ba14.png)
