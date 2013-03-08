Running Calculator Library for Python
=======
This library contains functions to easily convert from imperial and metric running calculations.

### Import the module
	import runcalc.runcalc as runcalc

### Given a distance in meters, and time, calculate the pace:

	# 400 meters in 65 seconds
	distance = runcalc.mtof(400) # meters to feet
	the_pace = runcalc.pace(distance, (0, 0, 65)) # calculate pace (h, m, s)
	print the_pace

	-- output: (0, 4.0, 21.518399602492025) (this is... quite fast)

Notice the pace function requires feet.

### Given a distance in miles and a time (6.05 miles in 55:37) calculate the pace.

	# 6.05 miles in 55 minutes and 37 seconds
	the_pace = runcalc.pace_for_distance(6.05, (0, 55, 37))
	print "pace_for_distance ", the_pace

	-- output: pace_for_distance  (0, 9.0, 11.570247933884275) (h, m, s)


### Given a distance (in miles) and a time, calculate miles per hour:

	# Miles per hour for 6.05 miles in 55 minutes and 31 seconds. 
	mph = runcalc.miles_per_hour(6.05, (0, 55, 31)) # second tuple is (h, m, s)
	print mph

	-- output: Mph  6.5385770039

### You can also easily convert meters to miles (for usage in the functions that require miles): 

	>>> runcalc.mtom(400)
	0.2485484772727273


Take a look around. It is actually a well documented library and it brings me little shame, other than exposing my love affair with the imperial measurements system. 


