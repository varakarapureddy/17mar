n=input()
newstr=""
vowels=('a','e','i','o','u')
for a in n:
    if a not in vowels:
        newstr=newstr+a
print(newstr)
