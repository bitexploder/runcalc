import math

SEC_PER_MIN=60
SEC_PER_HOUR=60*SEC_PER_MIN
FEET_PER_MILE = 5280
FEET_PER_METER = 3.2808399

"""
@mins - minutes to convert to seconds

Minutes to seconds
"""
def mtos(mins):
	return mins*SEC_PER_MIN

"""
@hours - number of hours in pace
@minutes - number of minutes to calculate
@seconds - number of seconds to calculate

Returns the pace flattened out to seconds
"""
def pace_to_seconds(h,m,s):
	accum = 0
	accum += h*(60*60)
        accum += m*60
	accum += s
	return accum

"""
@m - meters

Returns meters to feet
"""
def mtof(m):
	return m * FEET_PER_METER

"""
@m - meters

Returns meters to miles
"""
def mtom(m):
	return mtof(m)/FEET_PER_MILE

"""
@ft - number of feet
@pace  pace tuple (hours, minutes, seconds)

Returns the number of feet covered per second
"""
def feet_per_second(ft, pace):
	return ft/(pace_to_seconds(pace[0],pace[1],pace[2])*1.0)

"""
@fps - Feet traveled per second

Returns feet per second to miles per hour
"""
def fps_to_mph(fps):
	return fps*60*60/FEET_PER_MILE


"""
@distance - distance in miles
@pace - pace tuple (hours, minutes, seconds)

returns speed in miles per hour

"""
def miles_per_hour(distance, time):
	tmp = distance*SEC_PER_HOUR
	seconds = pace_to_seconds(time[0], time[1], time[2])
	fract = tmp%seconds
	whole = tmp/seconds

	if fract == 0:
		whole = whole + 0.0

	return whole



"""
@time - time tuple (h,m,s)
@pace - pace tuple (h,m,s)/mi

returns the distance traveled in miles
"""
def distance(time, pace):
	time = pace_to_seconds(time[0], time[1], time[2])
	pace = pace_to_seconds(pace[0], pace[1], pace[2])
	distance = time/(pace*1.0)
	return distance


"""
@ft - the number of feet (distance traveled)
@time - time tuple (hours,minutes,seconds) to cover distance @ft

Returns pace (hours,minutes,seconds) to travel one mile
"""
def pace(ft, time):
	fps = feet_per_second(ft, (time[0],time[1],time[2]))
	mph = fps_to_mph(fps)
	spm = SEC_PER_HOUR/mph # seconds per mile 
	pace_seconds = (SEC_PER_HOUR/mph)%60
	pace_mins = (spm - pace_seconds)/60
	return (0,pace_mins,pace_seconds)

"""
@distance - miles covered
@time - time tuple (h,m,s) for time it took to cover @distance

Returns pace tuple (h,m,s) per mile
"""
def pace_for_distance(distance, time):
	ft = distance*FEET_PER_MILE
	return pace(ft, time)
	
def test():
	distance=mtof(400)
	the_pace = pace(distance,(0,1,53))
	print "Pace for 400m is ",(the_pace)
	distance=mtof(1000)
	the_pace = pace(distance,(0,4,43))
	print "Pace for 1000m is ",(the_pace)
	distance=mtof(1609.344)
	the_pace = pace(distance,(0,7,33))
	print "Pace for 1609.344m is ",(the_pace)
	distance=mtof(1200)
	the_pace = pace(distance,(0,5,0))
	print "Pace for 1200m is ",(the_pace)
	distance=mtof(400)
	thei_pace = pace(distance,(0,1,40))
	print "Pace for 400 is ",(the_pace)
	mph = miles_per_hour(1, (0,10,0))
	print "Mph for (0,10,0) pace", mph
	mph = miles_per_hour(6.6, (0,60,0))
	print "Mph for (0,60,0) pace", mph

if __name__ == "__main__":
	test()