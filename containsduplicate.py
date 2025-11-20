a = [1,3,5,1,4,3,2,4,5,1,2,4,3,5,1]



b  = set(a)

if len(a) != len(b):
    print("Duplicates found")
else:
    print("No duplicates")