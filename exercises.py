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






# TUPLE
print("Kindergarten")
# This is the message displayed
print("Registration of tutor of babies in room A123:")
print("Baby  -  Tutors")
# The parents of babies don't change
dads = ("Jose Lopez: Roberta Lopez", "Pablo Rodriguez:Fernando Rodriguez", "Juana de Lira:Sofia de Lira",
        "Zuly Ponce:Marta Ponce", "Orlando Torres:Rodorfo Torres", "Sharon de la Rosa:Elias de la Rosa")
i = 0
while i < len(dads):
    # The name of the parents will be displayed
    print(dads[i])
    i += 1
# This is the last message
print("These are the tutors of the babies.")
