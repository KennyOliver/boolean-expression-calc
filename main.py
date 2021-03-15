from VividHues import Clr
#====================
# MAIN PROGRAM
expression = input(Clr.LIME + "Enter 2 boolean values (separate by a comma)\n\te.g. True,True\n\t--> " + Clr.RESET)

values = expression.split(",")
first_val, second_val = values[0].lower(), values[-1].lower()


if first_val in [0,"false"]:
  first_val = False
elif first_val in [1,"true"]:
  first_val = True

if second_val in [1,"true"]:
  second_val = True
elif second_val in [0,"false"]:
  second_val = False


print(Clr.YELLOW + str(first_val),"AND",str(second_val) + Clr.RESET)
print("\t=",first_val and second_val)

print(Clr.YELLOW + str(first_val),"OR",str(second_val) + Clr.RESET)
print("\t=",first_val or second_val)

print(Clr.YELLOW + "NOT",str(first_val),",","NOT",str(second_val) + Clr.RESET)
print("\t=",not first_val,",",not second_val)