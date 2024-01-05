# To read the file

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to a file

# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# Append to a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# Create a new file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")