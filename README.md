# CoppeliaSim-Python-Connecting-
Program Environment

|-- Operating System: Ubuntu 18.04

|-- CoppeliaSim Version: 4.1.0

|-- Python Version: 3.6.9

Connect Method: Blue-zero Remote API

|-- The API Files is stored in the "<Root Path of Simulator>/programming/b0RemoteApiBindings"
  
|-- The Python Client Environment Configuration is shown in the picture in following.
|-- (From the "Enabling the B0-based remote API - client side" in helpFiles of CoppeliaSim
![image](https://github.com/huangyh43/CoppeliaSim-Python-Connecting-/blob/main/Readme_Pic/PythonClient.png)

|-- One of configurations of Simulator Server: Add a Script-Model into the Scene

|--|-- Select the purpose Scene

|--|-- Add a Script-Model: "File / Load Model... / tools / B0 remote Api server.ttm

|--|-- Configure the node information of the added model, the result seems as the following figure
![image](https://github.com/huangyh43/CoppeliaSim-Python-Connecting-/blob/main/Readme_Pic/serverRes.png)

	Notes: The "Node name" and "Channel name" must be same at both two platform (Python and CoppliaSim)
