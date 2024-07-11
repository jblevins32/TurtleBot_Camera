# Turtlebot Camera

This repository is for testing the Raspi Camera on the Turtlebot with ROS2 publisher and subscriber nodes

In the package directory, run in one terminal:
\begin{enumerate}
	\item colcon build --packages-select py_pubsub
	\item source install/setup.bash
	\item ros2 run py_pubsub talker
\end{enumerate}

 In another terminal:
 	- colcon build --packages-select py_pubsub
	- source install/setup.bash
	- ros2 run py_pubsub listener
