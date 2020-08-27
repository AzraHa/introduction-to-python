s1 = input().lower()
s2 = input().lower()
i = 0
nalazi_se = True
for s in s2:
    nasao = False
    while i<len(s1) and not nasao:
        if s1[i] == s:
            nasao = True
        i += 1
    if not nasao:
        nalazi_se = False
if nalazi_se:
    print("Nalazi se")
else:
    print("Ne nalazi se")
