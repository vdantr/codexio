# Initialize an empty dictionary to store color-count pairs
colorCountDict = {}

# Loop until the user types "End"
while True:
    # Prompt the user for input and remove any leading/trailing whitespace
    pair = input("Please enter a 'color:count' pair (type 'End' to stop): ").strip()

    # If the user typed "End", exit the loop
    if pair == "End":
        break
    # Otherwise, try to split the input string into a color and a count
    else:
        try:
            color, count = pair.split(":")
            # If the color is already in the dictionary, add the count to its existing value
            # Otherwise, create a new key-value pair with the color and count
            colorCountDict[color] = colorCountDict.get(color, 0) + int(count)
        except (ValueError, TypeError):
            # If the input couldn't be split or the count couldn't be converted to an int, print an error message
            print(f"Invalid input: {pair}")

# Check if the dictionary is empty or has only one item
if len(colorCountDict) == 0:
    print("There are no balls in the box so the answer is 0.")
elif len(colorCountDict) == 1:
    print("There are balls of only one color in the box so the answer is 0.")
else:
    # Calculate the total count by summing the values in the dictionary
    totalCount = sum(colorCountDict.values())
    # Subtract 1 from the total count to get the answer
    print(f"There are {totalCount} balls in the box so the answer is {totalCount - 1}.")
