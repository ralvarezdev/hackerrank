def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            leap = year % 400 == 0

        else:
            leap = True

    return leap


year = int(input())