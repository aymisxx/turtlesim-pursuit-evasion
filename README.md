# **turtlesim-pursuit-evasion**

ROS1 turtlesim pursuit-evasion mini-project featuring random target motion, pose-based tracking, and closed-loop pursuit control.

---

## Overview

`turtlesim-pursuit-evasion` is a compact ROS1 micro-project built in the classic `turtlesim` environment. It models a simple pursuit scenario between two agents:

- **random_turtle**: a target turtle driven by randomly generated linear and angular velocity commands.
- **chasing_turtle**: a chaser turtle that subscribes to live pose updates and continuously steers toward the target.

Despite its lightweight setup, the project demonstrates a complete closed-loop robotics workflow using ROS publishers, subscribers, topic-based communication, and geometric feedback control.

## Demo

A recorded execution of the complete project is included in:

```bash
assets/demo.mp4
```

This video serves as the primary execution reference for the project and shows the full runtime behavior inside `turtlesim`.

## Highlights

- ROS1 publisher-subscriber based control pipeline.
- Random target motion generation.
- Real-time pose feedback using `turtlesim/Pose`.
- Closed-loop target pursuit using relative geometry.
- Compact and visual robotics micro-project for feedback-based tracking.

## Repository Structure

```bash
.
├── assets
│   └── demo.mp4
├── chasing_turtle_node.py
├── CMakeLists.txt
├── LICENSE
├── package.xml
├── random_turtle_node.py
├── README.md
└── scripts
    ├── chasing_turtle_node.py
    └── random_turtle_node.py
```

## System Description

The project consists of two ROS nodes:

### `random_turtle_node.py`

Publishes velocity commands to `random_turtle`, causing the turtle to wander with randomly changing forward and angular velocities.

### `chasing_turtle_node.py`

Subscribes to the poses of both turtles, computes the relative displacement and heading to the target, and publishes pursuit commands to `chasing_turtle`.

Together, these two nodes create a simple pursuit-evasion behavior loop in simulation.

## Control Logic

The chaser follows a basic geometric feedback strategy:

1. Read the current poses of the target and chaser.
2. Compute relative displacement:
   - `dx = x_target - x_chaser`.
   - `dy = y_target - y_chaser`.
3. Compute Euclidean distance to the target.
4. Compute heading angle using `atan2(dy, dx)`.
5. Publish:
   - linear velocity proportional to target distance.
   - angular velocity proportional to heading error.

This causes the chaser to continuously reorient toward the target and move forward until the separation becomes small.

## Dependencies

This package uses:

- ROS1
- `catkin`
- `rospy`
- `geometry_msgs`
- `std_msgs`
- `turtlesim`

## Build Instructions

Clone the repository into the `src` directory of a catkin workspace and build it:

```bash
cd ~/catkin_ws/src
git clone https://github.com/<your-username>/turtlesim-pursuit-evasion.git
cd ..
catkin_make
source devel/setup.bash
```

## Running the Project

### 1. Start ROS master

```bash
roscore
```

### 2. Launch turtlesim

```bash
rosrun turtlesim turtlesim_node
```

### 3. Remove the default turtle

```bash
rosservice call /kill "turtle1"
```

### 4. Spawn the two turtles

```bash
rosservice call /spawn 5 5 0 "random_turtle"
rosservice call /spawn 2 2 0 "chasing_turtle"
```

### 5. Run the random-motion node

```bash
rosrun turtlesim_pursuit_evasion random_turtle_node.py
```

### 6. Run the chasing node

```bash
rosrun turtlesim_pursuit_evasion chasing_turtle_node.py
```

## What This Project Demonstrates

Although small in scope, this project captures several core robotics concepts:

- feedback-driven control.
- perception-to-action flow through ROS topics.
- relative pose-based target tracking.
- simulation-first prototyping of autonomous behavior.

It serves as a clean foundational example before moving toward more advanced problems such as visual tracking, pursuit-evasion planning, multi-agent coordination, and autonomous interception.

## Execution Reference

A full recorded run of the project is provided in:

```bash
assets/demo.mp4
```

## Notes

- This project is implemented in **ROS1**.
- The package name is **`turtlesim_pursuit_evasion`**.
- The repository preserves a compact, standalone micro-project centered on feedback-based turtle pursuit in simulation.

## Future Extensions

Possible improvements include:

- adding a launch file for one-command execution.
- measuring interception time as a quantitative metric.
- introducing obstacle-aware pursuit.
- replacing random motion with a more deliberate evasion policy.
- porting the package to ROS2.

## License

This repository includes an `MIT-LICENSE` file.

---