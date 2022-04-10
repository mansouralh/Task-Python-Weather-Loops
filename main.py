# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    # Your code here
    for element in elements:
        print(element)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    # Your code here
    return [int((temperature - 32) * (5/9)) for temperature in temperatures]


# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    # Your code here
    return [temperature for temperature in temperatures if temperature > threshold]


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Print temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    # Your code here
    printer(to_celsius(hottest_days(temperatures, threshhold)))
