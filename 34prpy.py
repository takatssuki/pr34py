
#1
a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')

#2
a = 0
while a<=100:
  a = int (input())
  if a > 100:
    break
  if a<10:
    continue
  print(a)

 #3
data = int(input())
res = 0
while data != 0:
    res += data
    data = int(input())
print (res)
    
#4
a = int(input())
b = int(input())
res = a
while res % b != 0:
    res += a
print(res)

#5
a = int(input())
b = int(input())
s = 0
c = 0
for j in range (a,b+1):
    if j%3 == 0:
        s = s+j #42
        c = c+1
    j+=1
print(s/c)

#6
a =  input()
s1 = a.upper().count('c'.upper())
s2 = a.upper().count('g'.upper())
S=s1+s2
print(S/len(a)*100)

#6
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)

#7
s = [ int(i) for i in input().split()]
summ = 0 
l = len(s)-1
for i in range(0,l+1):
    summ = summ + s[i]
print(summ)

#8
s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1

#9
s = [ int(i) for i in input().split()]
t = []
s.sort()
l = len(s)-1
k = 100000
if len(s)!=1:
    for i in range(0,l):
        if s[i]==s[i+1] and s[i]!=k:
            t.append(s[i])
            k=s[i]
    for j in range(l,l+1):
        if s[-1]==s[-2] and s[j]!=k:
            t.append(s[j])
n = len(t)
for g in range(0,n):
    print(t[g],end=' ')

#10
a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)

#11
a=int(input())
m=[]
for i in range(a):
    j=0
    while j<i+1:
        m.append(i+1)
        j+=1
    if len(m)>a: break
m=m[0:a]
for i in m:
    print(i, end=" ")

#12
s = [ int(i) for i in input().split()]
n = int(input())
t = []
l = len(s)-1
if n in s:
    for i in range(0,l+1):
        if s[i]==n:
            t.append(i)
    g = len(t)-1
    for j in range(0,g+1):
        print(t[j],end=' ')
else:
    print('Отсутствует')

#13
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()]) 
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()

#14
def zm(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        arr[x][y] = i
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+dx, y+dy
    for x in list(zip(*arr)):
        print(*x)
 
zm(int(input()))
