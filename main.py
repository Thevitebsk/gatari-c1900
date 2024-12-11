def GAL():
 while True:
  instruct=[]
  inp=input("C/GAL:")
  instruct.append(inp)
  if inp=="EXIT":instruct.clear();break
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
