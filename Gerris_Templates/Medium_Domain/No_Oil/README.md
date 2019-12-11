# How to Generate the text file 
## Install Gerris Flow solver

- If you have a Debian version, install it directly from the repository APT:
 
 `sudo apt update && sudo apt install gerris gfsview3D`

- If you have another distribution of GNU/Linux, refer to this [this link](http://gfs.sourceforge.net/wiki/index.php/Installing_from_source)


## Run the simulation file

- make a build folder, and move the simulation file to it

`mkdir build && cp drops.gfs build/ && cd build/`

- to run it in serial:

`gerris3D drops.gfs`

- to run it in parallel with `NP` processors:

`NP=4` *change it to to the number of processors you have*

`mpirun -np $NP gerris3D drops.gfs`

## Generate the .txt file

at certain time, for staying in the same reference use :

`STEP=900` 

then use this command to generate a .txt file :
 
 `gerris3D -e "GfsOutputSimulation {istep =1 } step-$STEP.txt { format = text }" sim-$STEP-* > /dev/null`

## Move the .txt file to the post process directory

`mv step-$STEP.txt ../../../..`

# No Oil
This Gerris Flow Simulation file is a part of a study on the impact of small droplet (radius ~= 4 mm) on free surface. 
This study is interrested in cases where there is an oil layer over the free surface
In this template the is no oil layer, as it is a control case for the general problem.
 
# Medium domain 
In the experiment, the domain have the dimension of 15.2 cm² by 8cm of height , here we have a 5.76x5.76x11.52 cm³

# Max level 

A level corresponds to the power on with an initial box is divised by, here we have max level = 7, this is for demonstration purposes, to help testing the post=processing code on a low range machine, the most refined edge have the dimension of 6.4 mmx2⁻⁷ = 50µm
