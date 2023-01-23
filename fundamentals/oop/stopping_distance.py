def stoppingDistance(speed): #in MPH
    speed = speed/2.237 #converts MPH to MPS
    reaction_time = 1.5 #In seconds
    friction_co = 0.7 # common baseline
    gravity = 9.81
    reaction_distance = speed * reaction_time
    braking_distance = (speed ** 2)/(2 * friction_co * gravity) #returns in meters
    stopping_distance_in_feet = round((reaction_distance + braking_distance) / 3.28) #returns in feet
    print(f'{stopping_distance_in_feet} feet')

stoppingDistance(1000)