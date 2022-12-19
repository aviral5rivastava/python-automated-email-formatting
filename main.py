start_letter_file = open("./Input/Letters/starting_letter.txt", mode="r")
name_file = open("./Input/Names/invited_names.txt", mode="r")

name_list = name_file.readlines()
letter_format = start_letter_file.read()

for name in name_list:
    with open(f"./Output/ReadyToSend/{name}.text", mode="w") as new_file:
        new_letter_format = letter_format.replace("[name]", name.strip())
        new_file.write(new_letter_format)
start_letter_file.close()
name_file.close()
