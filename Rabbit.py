def getGardenInput():
    '''
    Prompts the user for the number of rows, columns, and carrots in the garden.
    Doesn't take any parameters and returns a number of rows and columns in the garden (grid) and a list of the coordinates of the carrots in the garden.
    '''

    rows = int(input('Please enter the number of rows: '))
    cols = int(input('Please enter the number of columns: '))
    carrot_count = int(input('Please enter the number of carrots: '))
    carrots = []
    for i in range(carrot_count):
        row = int(input(f'Please enter the row of carrot {i + 1}: '))
        col = int(input(f'Please enter the column of carrot {i + 1}: '))
        carrots.append((row, col))

    return rows, cols, carrots


def locateCarrotGroups(carrots):
    '''
    Finds all contiguous groups of carrots in the garden.
    Takes a list of the coordinates of the carrots in the garden as a parameter and returns 2D-array of the coordinates of the carrots.
    '''

    visitedCarrots = set()
    groups = []

    for carrot in carrots:
        # If the carrot with given coordinates has not been visited, perform a BFS to find all the contiguous carrots adjacent to the current carrot.
        if carrot not in visitedCarrots:
            group = [carrot]
            visitedCarrots.add(carrot)
            queue = [carrot]
            while queue:
                row, col = queue.pop(0)
                for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                    if (r, c) in carrots and (r, c) not in visitedCarrots:
                        group.append((r, c))
                        visitedCarrots.add((r, c))
                        queue.append((r, c))
            groups.append(group)

    return groups


# Get input from the user
rows, cols, carrots = getGardenInput()

# Locate contiguous groups of carrots
groups = locateCarrotGroups(carrots)

# Print the number of jumps 
print(len(groups))
