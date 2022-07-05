# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    # Your code here
    
    for element in elements :
        print("this is element"+element)



# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    # Your code here
    
   
    tempinc=[]
   
    for tempc in temperatures:
        tempinc.append ((tempc-32)*5/9)
    return tempinc
   

# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    # Your code here
    exceed= []
    for temp in temperatures:
        if  temp> threshold:
            return temp
        exceed.append(temp)
    return exceed

    
    
   
# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    # Your code here
    tempsinc = []
    for tempsc in temperatures:
        
        if (tempsc > threshhold):
            return tempsc
        tempsinc.append((tempsc-32)*5/9)
    print (tempsinc)
