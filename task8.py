def moment(num):
    """Function that converts a num into hours and minutes"""

    hour = num // 60
    mins = num % 60
    time = str(hour) + ' hour ' if (hour == 1) else str(hour) + ' hours '
    time += str(mins) + ' minute ' if (mins == 1) else str(mins) + ' minutes '
    print(time)

moment(60)