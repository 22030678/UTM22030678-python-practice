# LIST
print("Kindergarten")
# This is the message displayed
print("An attendance list of babies in room A123 is shown:")
print("List")
# These are the names
babies = ["Jose Lopez", "Pablo Rodriguez", "Juan de Lira",
          "Raul Esparza", "Zuly Ponce", "Orlando Torres ", "Sharon De la Rosa"]
# The list is displayed
print(babies)
# A question is asked to confirm the registration of all babies
question = (input("Do they all have assistance?"))
# There are two options:
if question == 'not':
    # If babies are not on the list, they are added
    babies.append(input("Enter the name of the baby to take list: "))
    # The new list is displayed
    print("Updated list: ")
    for i in babies:
        print(i)
# If all the babies are in the list a last message is shown
else:
    print("Everyone has assistance:")
