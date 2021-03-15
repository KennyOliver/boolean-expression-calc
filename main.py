from VividHues import Clr
#====================
# MAIN PROGRAM
expression = input(Clr.LIME + "Enter 2 boolean values (separate by a comma)\n\te.g. True,True\n\t--> " + Clr.RESET)

separate = expression.split(",")
first_value, second_value = separate[0].lower(), separate[-1].lower()


if first_value in [0,"false"]:
  first_value = False
else:
  first_value = True

if second_value in [1,"true"]:
  second_value = True
else:
  second_value = False


print(Clr.YELLOW + str(first_value),"AND",str(second_value) + Clr.RESET)
print("\t=",first_value and second_value)

print(Clr.YELLOW + str(first_value),"OR",str(second_value) + Clr.RESET)
print("\t=",first_value or second_value)

print(Clr.YELLOW + "NOT",str(first_value),",","NOT",str(second_value) + Clr.RESET)
print("\t=",not first_value,",",not second_value)