from VividHues import Clr
#====================
def bool_calc(bool_a,bool_b):
  """ boolean calculator """
  if bool_a in ["0","false"]:
    bool_a = False
  elif bool_a in ["1","true"]:
    bool_a = True
  
  if bool_b in ["1","true"]:
    bool_b = True
  elif bool_b in ["0","false"]:
    bool_b = False
  
  print(Clr.YELLOW + str(bool_a),"AND",str(bool_b) + Clr.RESET)
  print("\t=",bool_a and bool_b)
  
  print(Clr.YELLOW + str(bool_a),"OR",str(bool_b) + Clr.RESET)
  print("\t=",bool_a or bool_b)
  
  print(Clr.YELLOW + "NOT",str(bool_a),",","NOT",str(bool_b) + Clr.RESET)
  print("\t=",not bool_a,",",not bool_b)
#====================
# MAIN PROGRAM
expression = input(Clr.LIME + "Enter 1-2 boolean values (separate by a comma)\n\te.g. True,True\n\t--> " + Clr.RESET)

values = expression.split(",")
first_val, second_val = values[0].lower(), values[-1].lower()

bool_calc(first_val,second_val)