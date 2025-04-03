#This program is titled 'Rotation Test' and is part of a function and unit test package. The function being tested
# takes an input from the user representing degrees of a rotation. The function will remove unnecessary rotations above 360.
# The accompanied unit test will test various conditions. 
#Gavin Van Horn
#April 2nd, 2025

def rotation_correction(rotation):
    rotation = int(rotation)
    if rotation <= 360 and rotation >= 0:
        print(rotation)
        return rotation
    elif rotation > 360:
        rotation = rotation % 360
        print(rotation)
        return rotation
    else:
        rotation = (rotation % 360 + 360) % 360
        print(rotation)
        return rotation
rotation_correction(100)
rotation_correction(-250)