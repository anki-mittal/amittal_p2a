# Instruction to run the code

* Install the required dependencies
```cmd
  sudo pip install scipy math matplotlib tqdm
```

1. LOADING THE ENVIRONMENT
    -
    Run main.blend file and dorp down at bar in scripting tab and run env.py. 
    * Make sure map path is added in line 7.
    * For now 3 maps are already loaded in the blender env. Hide and unhide the map according to the requirement.

2. ADDING MAP PATH
    -
    In env3D.py add map path location at line 8.For eg. For eg.
    ```python
    file_path = '/home/ankitmittal/Documents/STUDY/RBE595/HW2a/amittal_p2a/src/sample_maps/map2.txt' 
    ```

3. SET STARTING AND GOAL POSITION
    -
    In env3D.py set starting and goal positon in line 52 and 53 repectively.
    ```python
    self.start = np.array([0, 20, 2])
    self.goal = np.array([10, 20, 3])
    ```

4. SET STARTING POSITION FOR BLENDER
    -
    In main.py in blender set the starting location of the drone for blender environment in line 93 - 95.
    ```python
    startx = 0
    starty = 20
    startz = 2
    ```
# Results

1. SIMULATION
   -
![Alt Text](https://github.com/anki-mittal/planning-through-trees/blob/master/outputs/map1/ezgif-5-f7068a1501.gif)

2. IMPLEMENTATION
   -
[![Watch the video](https://cdn.shopify.com/s/files/1/0263/8469/5395/files/Ryze-Tello-review-hover-outdoor-front-749x500.jpg)](https://youtu.be/6rkf0EhJAjg)




