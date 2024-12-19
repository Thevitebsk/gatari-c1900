inp="";instruct=[];reg={}

def itergal(code:str)->bool:
 "Interpreter for Gatari ASM Language"
 code=code.split()
 if code[0]=="REG":reg[code[1]]=int(code[2])
 elif code[0]=="ADD":reg[code[1]]=reg[code[1]]+int(code[2])
 else:print(f"\"{code[0]}\" IS NOT VALID GAL OPERATOR");return 1

def GAL():
 global l
 "Gtari ASM Language Interface"
 while True:
  inp=input("C/GAL:").upper()
  instruct.append(inp)
  if inp=="END":instruct.clear();reg.clear();break
  if inp=="LIST":instruct.pop();print("\n".join(instruct))
  if inp=="RUN":
   instruct.pop()
   print(len(instruct),"bytes")
   while instruct:
    if itergal(instruct[0]):break
    instruct.pop(0)

def MAIN():
 "Main interface"
 while True:
  inp=input("C:").upper()
  if inp=="END":break
  elif inp=="ASM":GAL()
  else:print("NOT FOUND")

print("****************\n* GATARI C1900 *\n****************");MAIN()
