def is_leap(year):
    leap = False
    # Write your logic here
    multiple_of_four = True if year % 4 == 0 else False
    multiple_of_oneh = True if year % 100 == 0 else False
    multiple_of_fourh = True if year % 400 == 0 else False
    
    if multiple_of_four and not multiple_of_oneh:
        return True
    elif all((multiple_of_four, multiple_of_oneh, multiple_of_fourh)):
        return True
    else:
        return False
year =int(input())
print(is_leap (year))
#this give true for leap years only for above logic
