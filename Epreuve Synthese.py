"""
Anthony Porporino
Samia Hilal
Epreuve Synthese
"""

import random
#Dictionary used to analyze data to test whether after n units of time, his distance from the center is theoretically proportional to the square root of number of moves
t_d_proportional = {}
def move():
    #This function will make the drunkard move randomly untill he reaches the end of a 10 by 10 grid.
    #It will return his final position, how many times he moved, his distance and number of times he went back to the center
    Drunkards_position = [0,0] #Corresponds to his x and y direction
    number_moves = 0
    center_count = 0
    while (-10 < Drunkards_position[0] < 10) and (-10 < Drunkards_position[1] < 10): #While loop stops the drunk when he reaches end of grid
        direction = random.randrange(1,5) #In this case, 1 = East, 2 = West, 3 = North, and 4 = South
        if direction == 1:
            Drunkards_position[0] += 1
            number_moves += 1
            if Drunkards_position == [0,0]:
                center_count += 1
        elif direction == 2:
            Drunkards_position[0] -= 1
            number_moves += 1
            if Drunkards_position == [0,0]:
                center_count += 1
        elif direction == 3:
            Drunkards_position[1] += 1
            number_moves += 1
            if Drunkards_position == [0,0]:
                center_count += 1
        elif direction == 4:
            Drunkards_position[1] -= 1
            number_moves += 1
            if Drunkards_position == [0,0]:
                center_count += 1
    Distance = abs(Drunkards_position[0]) + abs(Drunkards_position[1])
    t_d_proportional.setdefault(number_moves, Drunkards_position)
    return ("\nHe moved: {} times. \nHis new position is {} \nHis distance from the center is {}.\nHe went back to the tavern for another drink {} time(s)\n\n".format(number_moves,Drunkards_position,Distance,center_count))

#Explains to the user what the program does
print("""Welcome to the Drunkard's Walk program!!!
A drunkard starts off in a tavern in the middle of a 10 by 10 grid.
He walks up, down, left and right randomly and he stops when he reaches the end of the grid.
His position, distance from the center, number of times he moved and
number of times he went back to the tavern are all measured.
He goes back to the middle of the grid after each time the program is run\n""")
while True:
    #Creates a menu giving them options of what they can do
    y = int(input("Enter 1 to run the program a certain amount of times, 2 to analyze the data after having run the program or 3 to exit"))
    if y == 1:
        num = int(input("How many times would you like to run the program"))
        i = 0
        while i < num:
            print(move())
            i += 1
    elif y == 2:
        print("On average, after n units of time, his distance from the center is theoretically proportional to the square root of the number of moves.")
        total_distance_x = 0
        total_distance_y = 0
        total_moves = 0
        for key in t_d_proportional:
            total_distance_x += t_d_proportional[key][0]
            total_distance_y += t_d_proportional[key][1]
            total_moves += key**(.5)
        total_distance = abs(total_distance_x) + abs(total_distance_y)
        print("Total distance: ", total_distance)
        print("Square root total moves: ", total_moves)
        print("Proportionality constant: ", total_distance/total_moves)
    elif y == 3:
        break
    else:
        print("Not a valid input")
