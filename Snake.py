from tabulate import tabulate
import os
import sys
import random
import time
if os.name == 'nt':
    import msvcrt
def clear_screen():
    # If the system is Windows, run 'cls', otherwise run 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
def check_keyboard(current_direction):
    if os.name == 'nt' and msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        if key == '1': return 1
        if key == '2': return 2
        if key == '3': return 3
        if key == '4': return 4
    return current_direction
def mov(h,d,t,L): #h is a 2 member list that holds the position of head of snake
    ot=list(t[-1])
    if d==1: #t is the list of coordinates of every block of snake in 9x9 grid
        if h[1]==0:
            h[1]=8
        else:
            h[1]=h[1]-1
    elif d==2:
        if h[0]==0:
            h[0]=8
        else:
            h[0]=h[0]-1
    elif d==3:
        if h[1]==8:
            h[1]=0
        else:
            h[1]=h[1]+1
    elif d==4:
        if h[0]==8:
            h[0]=0
        else:
            h[0]=h[0]+1
    k=list(t[0])
    t[0]=list(h)
    for i in range(1,len(t)):
        t[i],k=k,t[i]
    L[h[0]][h[1]]="H"
    for j in range(1,len(t)):
        L[t[j][0]][t[j][1]]="." #H in grid is head of snake and body is by "."
    L[ot[0]][ot[1]]=" "
    print(tabulate(L,tablefmt="grid"))
    if h in t[1:]:
        print("GAME OVER! You bit your own tail!")
        sys.exit()
def Apple(h,d,t,ap,L):
    k=[]
    if h==ap:
        k=list(t[-1])
        if d==3: #t is the list of coordinates of every block of snake in 9x9 grid
            if k[1]==0:
                k[1]=8
            else:
                k[1]=k[1]-1
        elif d==4:
            if k[0]==0:
                k[0]=8
            else:
                k[0]=k[0]-1
        elif d==1:
            if k[1]==8:
                k[1]=0
            else:
                k[1]=k[1]+1
        elif d==2:
            if k[0]==8:
                k[0]=0
            else:
                k[0]=k[0]+1
        t.append(k)
        L[k[0]][k[1]]="."
L=[[" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "," "]]
L[4][4]="H"
h=[4,4]
d=1
t=[[4,4],]
print(tabulate(L,tablefmt="grid"))
ac = 0.0
ap = [random.randint(0, 8), random.randint(0, 8)]
while ap in t:
    ap = [random.randint(0, 8), random.randint(0, 8)]
L[ap[0]][ap[1]] = "A"
while True:
    clear_screen()
    print("🎮 TAP [1=Left, 2=Up, 3=Right, 4=Down] - Snake moves automatically!")
    d = check_keyboard(d)
    mov(h,d,t,L)
    time.sleep(1)
    ac+=1
    if h == ap or ac >= 20.0:
        # Clear old apple location frame back to empty space
        L[ap[0]][ap[1]] = " "
        Apple(h, d, t, ap, L)
        ap = [random.randint(0, 8), random.randint(0, 8)]
        while ap in t:
            ap = [random.randint(0, 8), random.randint(0, 8)]
        L[ap[0]][ap[1]] = "A"
        ac = 0.0
