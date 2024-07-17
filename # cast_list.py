# cast_list
def create_cast_list(filename):
    # Initialize an empty list to store the actors' names
    cast_list = []

    # Open the file and read each line
    with open(filename, 'r') as file:
        # Iterate through each line
        for line in file:
            # Split the line using commas
            # The first element (index 0) is the actor's name
            actor_name = line.split(',')[0].strip()

            # Add the actor's name to the cast_list
            cast_list.append(actor_name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')

