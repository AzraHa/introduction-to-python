n = input()
nalazi_se = False
while(n!=""):
    n = int(n)
    if n == 2:
        nalazi_se = True
    n= input()
if nalazi_se:
    print("Nalazi se")
else:
    print("Ne nalazi se")
