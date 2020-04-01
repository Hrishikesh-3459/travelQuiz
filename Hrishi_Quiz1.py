
goa=0
delhi=0
jaipur=0
c=[goa,delhi,jaipur]

def attraction(c):
    a=int(input("Where do you enjoy the most? 1-Beach, 2- City, 3-Monuments\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def food(c):
    a=int(input("What is your favorite dish? 1-Fish, 2-Paratha, 3-Dal-Bhati\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def travel(c):
    a=int(input("How do you like to travel? 1-Boat,2-Metro.3-Auto\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def animals(c):
    a=int(input("Which is your favourite animal? 1-Dolphin, 2-Monkey, 3-camel\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def drink(c):
    a=int(input("What is your favourite drink? 1-Beer, 2- Lassi, 3-Rabdi\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def activity(c):
    a=int(input("How do you like to spend your time? 1-Party, 2- Shopping, 3- safari\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def stay(c):
    a=int(input("Where would you like to stay? 1-Resort, 2-Hotel, 3-Mahal(Fort)\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def dance(c):
    a=int(input("Which is your favourite dance form? 1-Fugdi, 2-Western, 3-Ghoomar\n"))
    if(a==1):
        c[0]+=1
    if(a==2):
        c[1]+=1
    if(a==3):
        c[2]+=1

def calc(c):
    print("Your Dream Destination is...")
    if(max(c)==c[1]):
        print("Delhi!")
    if(max(c)==c[0]):
        print("Goa!")
    elif(max(c)==c[2]):
        print("Jaipur!")
    

#This is not working
def im():
    from IPython.display import Image
    Image("/Users/hrishikesh/Desktop/Testing.jpeg")

attraction(c)
im()
food(c)
travel(c)
drink(c)
animals(c)
activity(c)
stay(c)
dance(c)
calc(c)