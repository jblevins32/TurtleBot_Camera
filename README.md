# Turtlebot Camera

This repository is for testing the Raspi Camera on the Turtlebot with ROS2 publisher and subscriber nodes.

In the package directory, run in one terminal:

1. `colcon build --packages-select py_pubsub`
2. `source install/setup.bash`
3. `ros2 run py_pubsub talker`

In another terminal:

1. `colcon build --packages-select py_pubsub`
2. `source install/setup.bash`
3. `ros2 run py_pubsub listener`
