# Used to generate items for layout or other things.
'''
for i in range(500):
    interval_string = str(i)
    value = ""
    if i < 10:
        value = "00" + interval_string + " ="
    elif i < 100:
        value = "0" + interval_string + " ="
    else:
        value = interval_string + " ="
    print(value)
    '''

for i in range(100):
    interval_string = str(i) + ':[0, 0],'
    print(interval_string)