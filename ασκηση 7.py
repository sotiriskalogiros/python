from datetime import datetime
  
# Get a datetime object
now = datetime.now()
  
# General functions
print "Year: %d" % now.year
print "Month: %d" % now.month
print "Day: %d" % now.day
print "Weekday: %d" % now.weekday() # Day of week Monday = 0, Sunday = 6

