# OGBD
Octree Grid Body Detector, is a post processing code used mainly to analyze the outputs of Gerris Flow Simulation 

# instructions
- First set up 
for right now: 
- to read the .txt file:

  `python3 read.py`

*answer the questions you are asked (step =900) and there is no Oil*

- Run the code: 

`python3 Reconstruction.py`

this will create to output files `MainPts.npy` and `Gi_Splash.npy`, they represent the data for the all points, and the indices that refer to the Main body respectively

- Delete unwanted files:

`rm data-900.npy`
