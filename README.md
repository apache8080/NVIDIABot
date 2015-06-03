NVIDIABot
=========
Update: In the next few months I will begin working on reprogramming the control system to make it more user friendly. I will be moving the robot to ROS over the next few months.
=========
Currently I have been working with Nvidia's Jetson Tk1 board to convert a FIRST FRC robot into a fully custom robot. This robot uses the Jetson board and an Arduino as it's main processor. For this project I used python as the main language that communicates with the Arduino and the users computer. I created a system similar to the FRC driver station that a user downloads to connect to the robot. On the users computer they can connect any xbox or ps3 controller to begin driving the robot. The connection between the users computer and the robot is over a UDP socket. I used UDP since it is faster than TCP even though UDP will lose more packets. Watch the video here: https://www.youtube.com/watch?v=AkMDzctFkO0.
