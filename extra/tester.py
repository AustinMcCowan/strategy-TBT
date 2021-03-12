# [None, None], [None, True], [True, None] Will be successful
# [True, True] Will be unsuccessful
# result = [True, True]

# Just another safeguard to insure a problem hasn't occured in unit placement 
# Reason for not 'if result[0] == result[1]:' is because they could both be None, which is fine.
'''if None not in result:
    raise Exception("Error has occured during draw: Red unit and blue unit coexist on one tile")
else:
    print(result)'''

x_coordinates = []
y_coordinates = []
frameheight, framewidth = 100, 100
current_x, current_y = 1, 1
interval_height = frameheight / 10
interval_width = framewidth / 10
set_height = interval_height - 1
set_width = interval_width - 1

for i in range(10): 
    x_coordinates.append([current_x, set_width])
    current_x = set_width + 2 # Removes overlapping 
    set_width += interval_width

    y_coordinates.append([current_y, set_height])
    current_y = set_height + 2 # Removes overlapping
    set_height += interval_height

print(x_coordinates)
print(y_coordinates)

current_x = x_coordinates[1][0] - 1
current_y = y_coordinates[2][0] - 1
edge_x = x_coordinates[1][1] + 1
edge_y = y_coordinates[2][1] + 1
x_size = (edge_x - current_x)
y_size = (edge_y - current_y)
position_x = current_x + (x_size/2)
position_y = current_y + (y_size/2)
print(position_x)
print(position_y)