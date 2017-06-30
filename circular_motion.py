# 28th June, 2017
#Viral 
# The following code moves the PSM such that it follows the trajectory of the arc of a circle. 90 degrees in one direction
#and then reverses that trajectory until it reaches its initial position and repeats the same thing on the other direction
# Input Arguments: rotational axis


import sys
import argparse
import dvrk
import numpy
import PyKDL 
import time
import numpy as np
import math


if __name__ == "__main__":
    p = dvrk.psm("PSM1")
    p.home()
    p.move_joint(numpy.array([0.0, 0.0, .20, 0.0, 0.0, 0.0, 0.0])) # removing the tooltip

    radius = 0.05
    initialpos =PyKDL.Vector(p.get_current_position()[0,3], p.get_current_position()[1,3], p.get_current_position()[2,3]) #getting the initial endeffector position
    perp = PyKDL.Vector(k[0,0], k[1,0], k[2,0]) #the vector perpendicular to the tooltip
    parallel = PyKDL.Vector(k[0,2], k[1,2], k[2,2])*-1  #vector from center of the circle to the point on the circle (tooltip)
    center = initialpos-radius*parallel
    temp = 1
    
    for x in xrange(90): #first 90 degrees in 1 degree increments 
              angle = temp
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*perp*parallel+center
              p.move(k)
              currentpos = PyKDL.Vector(p.get_current_position()[0,3], p.get_current_position()[1,3], p.get_current_position()[2,3])
              zz = center - currentpos 
              zz = zz/PyKDL.Vector.Norm(zz) #z component of the rotation matrix
              x = zz*perp #x component of the rotation matrix
              rotmatrix = PyKDL.Rotation(perp,x,zz) #since the x axis of the tooltip is parellel to the y axis of the global rotation matrix
              p.move(rotmatrix)
              temp = temp + 1
              

    for x in xrange(180):
              angle = temp
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*perp*parallel+center
              p.move(k)
              currentpos = PyKDL.Vector(p.get_current_position()[0,3], p.get_current_position()[1,3], p.get_current_position()[2,3])
              zz = center - currentpos
              zz = zz/PyKDL.Vector.Norm(zz)
              x = zz*perp
              rotmatrix = PyKDL.Rotation(perp,x,zz)
              p.move(rotmatrix)
              temp = temp -1
     
    for x in xrange(90):
              angle = temp
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*perp*parallel+center
              p.move(k)
              currentpos = PyKDL.Vector(p.get_current_position()[0,3], p.get_current_position()[1,3], p.get_current_position()[2,3])
              zz = center - currentpos
              zz = zz/PyKDL.Vector.Norm(zz)
              x = zz*perp
              rotmatrix = PyKDL.Rotation(perp,x,zz)
              p.move(rotmatrix)
              temp= temp + 1
              
              




