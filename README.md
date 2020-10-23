# CoppeliaSim-Python-Connecting-

Program Environment
|-- Operating System: Ubuntu 18.04
|-- CoppeliaSim Version: 4.1.0
|-- Python Version: 3.6.9

Connect Method: Blue-zero Remote API
|-- The API Files is stored in the "<Root Path of Simulator>/programming/b0RemoteApiBindings"
|-- The Python Client Environment Configuration is shown in the picture in following.

|-- One of configurations of Simulator Server: Add a Script-Model into the Scene
|--|-- Select the purpose Scene
|--|-- Add a Script-Model: "File / Load Model... / tools / B0 remote Api server.ttm
|--|-- Configure the node information of the added model, the result seems as the following figure


Notes: The "Node name" and "Channel name" must be same at both two platform (Python and CoppliaSim)
