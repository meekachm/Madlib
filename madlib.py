
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

#mablib variable
adj_1 = input("Enter adjective: ")
adj_2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
bodypart = input("Enter a bodypart: ")
verb = input("Enter an action verb in the past tense: ")
room = input("Enter a type of room: ")
food = input("Enter a type of food: ")
adj_3 = input("Enter adjective: ")

#madlib story
madlib = (f"""It was a {adj_1} August day. 
          I awoke to the {adj_2} aroma of a {animal} roasting outside my window. 
          My {bodypart} grumbled, signaling I was hungry. 
          I {verb} out of bed and went to the {room} to check if there was anything I could eat, where I found {food}. 
          I ate it and it was {adj_3}!""")

#displaying madlib results
print(madlib)