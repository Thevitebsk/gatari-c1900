inp=""
def itergal(code:str):
 code=code.split();print(code)
def GAL():
 instruct=[]
 while True:
  inp=input("C/GAL:")
  instruct.append(inp)
  if inp=="END":instruct.clear();break
  if inp=="RUN":
   instruct.pop()
   while len(instruct)>0:itergal(instruct[0]);instruct.pop(0)
def main():
 while True:
  inp=input("C:")
  inpl=inp.split()
  if inpl[0]=="NEW":
   with open(f'{" ".join(inpl[2:])}.{inpl[1]}', 'w') as f:...
  elif inp=="END":break
  elif inp=="ASM":GAL()
print(
"""
****************
* GATARI C1900 *
****************
"""
)
main()
