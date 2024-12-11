inp="";instruct=[];reg={}
def itergal(code:str):
 code=code.split();print(code)
 if code[0]=="REG":reg[code[1]]=code[2]
def GAL():
 while True:
  inp=input("C/GAL:").upper()
  instruct.append(inp)
  if inp=="END":instruct.clear();reg.clear();break
  if inp=="RUN":
   instruct.pop()
   while len(instruct)>0:itergal(instruct[0]);instruct.pop(0)
def main():
 while True:
  inp=input("C:").upper()
  inpl=inp.split()
  if inpl[0]=="NEW":
   if len(inpl)>2:
    with open(f'{" ".join(inpl[2:]).upper()}.{inpl[1].lower()}', 'a') as f:...
   else:print("NOT ENOUGH DATA")
  elif inp=="END":break
  elif inp=="ASM":GAL()
  else:print("NOT FOUND")
print(
"""
****************
* GATARI C1900 *
****************
"""
)
main()
