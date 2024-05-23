# Define a list of people to invite to dinner
invitees = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Print invitation messages to each person
for person in invitees:
    print(f"Dear {person},\nI would like to invite you to dinner at my place. It would be an honor to have your company.\nPlease let me know if you can make it!\nBest regards,\n[Abdul Ajnas]")
    print()  # Add an empty line for clarity between invitations

# Print the name of the guest who can't make it
guest_cant_make_it = "Albert Einstein"
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.\n")

# Replace the name of the guest who can't make it with a new person
new_invitee = "Isaac Newton"
invitees[invitees.index(guest_cant_make_it)] = new_invitee

# Print a second set of invitation messages to each remaining person
for person in invitees:
    print(f"Dear {person},\nI would like to invite you to dinner at my place. It would be an honor to have your company.\nPlease let me know if you can make it!\nBest regards,\n[Abdul Ajnas]")
    print()  # Add an empty line for clarity between invitations
