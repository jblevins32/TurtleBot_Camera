# Turtlebot Camera

This repository is for testing the Raspi Camera on the Turtlebot with ROS2 publisher and subscriber nodes.

In the package directory, run in one terminal:

`colcon build --packages-select py_pubsub`
`source install/setup.bash`
`ros2 run py_pubsub talker`

In another terminal:

`colcon build --packages-select py_pubsub`
`source install/setup.bash`
`ros2 run py_pubsub listener`
