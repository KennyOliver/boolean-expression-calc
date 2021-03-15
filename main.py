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
  
  # AND
  print(Clr.YELLOW + str(bool_a),Clr.PINK + "AND" + Clr.YELLOW,str(bool_b) + Clr.RESET)
  print(Clr.CYAN,"\t=",bool_a and bool_b,Clr.RESET)
  
  # OR
  print(Clr.YELLOW + str(bool_a),Clr.PINK + "OR" + Clr.YELLOW,str(bool_b) + Clr.RESET)
  print(Clr.CYAN,"\t=",bool_a or bool_b,Clr.RESET)
  
  #XOR
  print(Clr.YELLOW + str(bool_a),Clr.PINK + "XOR" + Clr.YELLOW,str(bool_b) + Clr.RESET)
  print(Clr.CYAN,"\t=",bool_a ^ bool_b,Clr.RESET)
  
  # NOT
  print(Clr.PINK + "NOT",Clr.YELLOW + str(bool_a),",",Clr.PINK + "NOT" + Clr.YELLOW,str(bool_b) + Clr.RESET)
  print(Clr.CYAN,"\t=",not bool_a,",",not bool_b,Clr.RESET)
#====================
# MAIN PROGRAM
print(Clr.UNDERLINE + Clr.CYAN + "<-- Boolean Expression Calculator -->" + Clr.RESET)
print("Enter Boolean values, and see their result using Boolean logic operators!")
print(Clr.PINK + "AND, OR, XOR, NOT" + Clr.RESET)

print(Clr.BLACK,"-" * 30,Clr.RESET)
print(Clr.BOLD + Clr.LIME + "Enter 1-2 Boolean values (separated by a comma)" + Clr.RESET)
print(Clr.ORANGE + "\t(single values get duplicated - ie. 0 or 1)")
print(Clr.LIME + "\teg. True,True (or 1,1)" + Clr.RESET)
expression = input(Clr.BOLD + Clr.LIME + "\t--> " + Clr.RESET)

values = expression.split(",")
first_val, second_val = values[0].lower(), values[-1].lower()
print(Clr.BLACK,"-" * 30,Clr.RESET)

bool_calc(first_val,second_val)
print(Clr.BLACK,"-" * 30,Clr.RESET)