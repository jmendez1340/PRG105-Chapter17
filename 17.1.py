class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second
    """

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 10
time.minute = 16
time.second = 21

print time.time_to_int()