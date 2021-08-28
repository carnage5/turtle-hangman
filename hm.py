#hangman
import turtle
import random
def draw(x):
    if x==1: #h
        t.circle(60)
    elif x==2: #a
        t.right(90)
        t.right(30)
        t.forward(100)
        t.backward(100)
    elif x==3: #n
        t.left(60)
        t.forward(100)
        t.backward(100)
        t.right(30)
    elif x==4: #g
        t.forward(100)
    elif x==5: #m
        t.right(30)
        t.forward(100)
        t.backward(100)
    elif x==6: #a
        t.left(60)
        t.forward(100)
        t.up()
        t.home()
    elif x==7: #n
        t.goto(0,120)
        t.down()
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(400)
vowels=['a','e','i','o','u']
def show(movie,letter=[]):
    for i in movie:
                if i !=' ':
                    if i in letter:
                        print(i,end=' ')
                    elif i in vowels:
                        print(i,end=' ')
                    else:
                        print("_",end=' ')
                else:
                    print(i,end=' ')
        
f=open('movie.txt','r')    
mc=1
r=random.randint(1,50)
#print(r)
while mc<=50:
    st=f.readline().strip()
    lstr=st.split(',')
    #print(lstr)
    if lstr[0]==str(r):
        m=lstr[1].lower()
        break
    mc+=1
f.close()    
print("Guess the movie \n")    
show(m)
s1=set()
for i in m:
    if i!=' ':
        if i not in vowels:
            s1.add(i)
l=[]
g=[]
hm="hangman"
hmc=0
s=turtle.getscreen()
t=turtle.Turtle()
while(len(l)!=7):
        c=input("\nguess letter ")
        if c in vowels:
            print("vowels already shown ")
            continue
        if c in m:
            g.append(c)
            print("\nright guess \n")
            show(m,g)
        else:
            print("\nwrong guess \n")
            l.append(hm[hmc])
            hmc+=1
            draw(len(l))
        s2=set(g)
        if len(s2)==len(s1):
            print("\ncongrats, you have won")
            break
        #print(l)
if len(l)>=7:
    print("sorry you have lost \n game over")

   
    
                    
                    
