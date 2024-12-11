def GAL():
 while True:
  instruct=[]
  inp=input("C/GAL:")
  instruct.append(inp)
  if inp=="EXIT":break
def main():
 while True:
  inp=input("C:")
  inpl=inp.split()
  if inpl[0]=="NEW":
   with open(f'{" ".join(inpl[2:])}.{inpl[1]}', 'w') as f:...
  if inp=="ASM":GAL()
print(
"""
****************
* GATARI C1900 *
****************
"""
)
main()
