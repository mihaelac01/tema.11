n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
print('a) afiseaza pe ecran componentele tabloului la un interval de 5 pozitii;')
print(a[::5])
print('b) afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator;')
print(a[::-1])
print('c) sorteaza componentele tabloului in ordine descrescatoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d) afiseaza pe ecran doar componentele pare;')
pare=[]
for i in range(0,len(a)):
        if a[i]%2==0:
            y=a[i]
            pare.extend([y])
print(pare)
print('e) afişează pe ecran media aritmetică a componentelor pare;')
print(round(sum(pare)/len(pare),2))
print('f) afiseaza pe ecran doar componentele impare;')
impare=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ia=a[i]
        impare.extend([ia])
        print(impare)
print('g) afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("x="))
y=int(input("y="))
v=[]
for i in a:
    if ((i>x)and(i%y!=0)):
        u=i
        v.extend([u])
print(v)
print('h) afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
val=[]
for i in a:
    if ((i>x)and(i<y)):
        z=i
        val.extend([z])
print(val)
print('i) afiseaza pe ecran pozitiile(indicii) componentelor impare negative;')
l=[]
for i in impare:
    if i<0:
        l.extend([a.index(i)])
print(l)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
p=[]
for i in range(0,n):
    if ((a[i]>9)and(a[i]<100))or((a[i]>-100)and(a[i]<-9)):
     p.extend([i])  
print(p) 
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
r=[]
for i in range(0,len(a)):
    y=a[i]
    r.extend([y])
t=min(r)
r[0]=t
print(r)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
s=[]
for i in range(0,len(a)):
    y=a[i]
    s.extend([y])
t=min(s)
s[s.index(min(s))]=s[0]
print(s)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
z=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        z.extend([y])
print(z)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
diviz=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        diviz.extend([y])
print(diviz)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori;')
w=[]
for i in a:
    if i>0:
        n=0
        for k in range(1,i+1):
            if (i%k==0):
               n+=1
        if n<=4:
            w.extend([i])
print(w)