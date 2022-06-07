<h1 align="center">
  Rotation Trigonometry
</h1>

This project is a uses uses a general rotation matrix to calculate the rotation
of a model consisting of [x,y,z] vertices to represent each point in it's shape.
The models consist of a sequence of numpy arrays to represent each vertex and
a sequence of tuples with 2 indexes to represent the edges of the model. The
model of choice is generated at the start and rendered using pygame.

## Demo
<p align="center">
    <img src="/media/demo_cube.gif" height="400">
    <img src="/media/demo_sphere.gif" height="400">
</p>


## Setup

clone and install the python requirements
```
git clone https://github.com/Serphyus/Rotation-Trigonometry
cd Rotation-Trigonometry
pip install -r requirements.txt
```

## Usage

run the main.py located in the src directory
```
py src/main.py
```

choose model to render
```
Available Models:
1  : cube
2  : sphere

> _
```
