a=10
b=5
if a > b:
    print("if loop")
elif a < b:
    print("else loop")
print("A") if (a>b) else print("B")

print("A > B") if(a>b) else print("A==B") if(a==b) else print("A<B")

c=1

if a>b and a>c:
    print("a >b and a>c")
elif a<b and a<c:
    print("else block")

i=0
while i<6:
    print(i)
    i+=1;

j=0;
while j<10:
    print(j)
    if j==5:
        break;
    j+=1;

print("continue")

j=0;
while j<10:
    j+=1
    if j==5:
        continue;
    print(j)
