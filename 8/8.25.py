rijec = input().lower()
prvo = rijec[0]
zadnje = rijec[-1]
za_sort = list(rijec[1:-1])
za_sort.sort()
sortirani = ""
for element in za_sort:
    sortirani += element
print(prvo+sortirani+zadnje)
