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
import time

if __name__ == "__main__":
#    parser = argparse.ArgumentParser()  #taking information from command line initialization
#    parser.add_argument('-xx', '--xx, help = 'the x component of the rotation matrix.' )
#    parser.add_argument('-xy', '--xy', help = 'the y component of the rotation matrix.' )
#    parser.add_argument('-xz', '--xz', help = 'the z component of the rotation matrix.' )
#    parser.add_argument('-yx', '--yx', help = 'the x component of the rotation matrix.' )
#    parser.add_argument('-yy', '--yy', help = 'the y component of the rotation matrix.' )
#    parser.add_argument('-yz', '--yz', help = 'the z component of the rotation matrix.' )
#    parser.add_argument('-zx', '--zx', help = 'the x component of the rotation matrix.' )
#    parser.add_argument('-zy', '--zy', help = 'the y component of the rotation matrix.' )
#    parser.add_argument('-zz', '--zz', help = 'the z component of the rotation matrix.' )
#    parser.add_argument('-r', '--radius', help = 'the radius of the arc.' )

#    xx = int(args.xx)
#    xy = int(args.xy)
#    xz = int(args.xz)
#    yx = int(args.yx)
#    yy = int(args.yy)
#    yz = int(args.yz)
#    zx = int(args.zx)
#    zy = int(args.zy)
#    zz = int(args.zz)
#    rotmatrix=PyKDL.Rotation(xx,yx,zx,xy,yy,zy,zx,zy,zz)

    p = dvrk.psm("PSM3")
    #p.home()
    #p.move_joint(numpy.array([0.0, 0.0, .20, 0.0, 0.0, 0.0, .3])) # removing the tooltip

    initialframe =p.get_current_position()
    radius = 0.05##int(args.radius)
    initialpos = initialframe.p #getting the initial endeffector position
    initialrot = initialframe.M
  
    #rot_axis = PyKDL.Vector(k[0,0], k[1,0], k[2,0]) #the vector rot_axisendicular to the tooltip - the the rotation vector of the circle
    rot_axis = PyKDL.Vector(1,0,0)
    rot_axis = rot_axis/PyKDL.Vector.Norm(rot_axis)
  
    parallel = initialrot.UnitZ()*-1  #vector from center of the circle to the point on the circle (tooltip)
    center = initialpos-radius*parallel
    time.sleep(0.5)
    for angle in range(0, -46, -1): #first 90 degrees in 1 degree increments
             
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*rot_axis*parallel+center
              p.move(k)
              currentpos = k
              zz = center - currentpos
              zz = zz/PyKDL.Vector.Norm(zz) #z component of the rotation matrix
              y = zz * rot_axis #y component of the rotation matrix
              rotmatrix = PyKDL.Rotation(rot_axis, y, zz) #since the y axis of the tooltip is parellel to the y axis of the global rotation matrix
            
              p.move(rotmatrix)
           
              time.sleep(0.5)  
            
    for angle in range(-45,46,1):
            
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*rot_axis*parallel+center
              p.move(k)
              currentpos = k
              zz = center - currentpos
              zz = zz/PyKDL.Vector.Norm(zz)
              y = zz*rot_axis
              rotmatrix = PyKDL.Rotation(rot_axis,y,zz)
              p.move(rotmatrix)
            
              time.sleep(0.5)   
 
    for angle in range(45,0, -1):
            
              k= (radius * math.cos(math.pi*angle/180) * parallel) +radius*math.sin(math.pi*angle/180)*rot_axis*parallel+center
              p.move(k)
              currentpos = k
              zz = center - currentpos
              zz = zz/PyKDL.Vector.Norm(zz)
              y = zz*rot_axis
              rotmatrix = PyKDL.Rotation(rot_axis,y,zz)
              p.move(rotmatrix)
        
              time.sleep(0.5)

