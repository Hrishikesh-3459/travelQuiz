
from tkinter import *
import csv


DETAILS = ['name', 'natural', 'food', 'intent', 'man_made', 'dress', 'drink', 'climate', 'activity']


class Cities:

    def __init__(self, name, natural, man_made, intent, food, dress, drink, climate, activity, message):
        self.details= {}
        self.details[DETAILS[0]] = name
        self.details[DETAILS[1]] = natural
        self.details[DETAILS[2]] = food
        self.details[DETAILS[3]] = intent
        self.details[DETAILS[4]] = man_made
        self.details[DETAILS[5]] = dress
        self.details[DETAILS[6]] = drink
        self.details[DETAILS[7]] = climate
        self.details[DETAILS[8]] = activity
        self.message = message
        self.vote = 0


    def inc_vote(self, view):
        self.vote += 1
        # la = Label(root, text = self.details[DETAILS[0]]).pack()
        view.pack_forget()
        button = Button(root, text = "Next")
        askQue()


class Questions:
    
    def __init__(self, question_str, options):
        self.question_str = question_str
        self.options = options
    
    
    def get_frame(self, root):
        frame = Frame(root)
        Label(frame, text = self.question_str).pack()
        
        if(len(ques[index].options) == 4):
            but1 = Button(frame, text = ques[index].options[0].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[0].inc_vote(frame)).pack()
            but2 = Button(frame, text = ques[index].options[1].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[1].inc_vote(frame)).pack()
            but3 = Button(frame, text = ques[index].options[2].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[2].inc_vote(frame)).pack()
            but4 = Button(frame, text = ques[index].options[3].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[3].inc_vote(frame)).pack()
        elif(len(ques[index].options) == 10):
            but1 = Button(frame, text = ques[index].options[0].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[0].inc_vote(frame)).pack()
            but2 = Button(frame, text = ques[index].options[1].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[1].inc_vote(frame)).pack()
            but3 = Button(frame, text = ques[index].options[2].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[2].inc_vote(frame)).pack()
            but4 = Button(frame, text = ques[index].options[3].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[3].inc_vote(frame)).pack()
            but5 = Button(frame, text = ques[index].options[4].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[4].inc_vote(frame)).pack()
            but6 = Button(frame, text = ques[index].options[5].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[5].inc_vote(frame)).pack()
            but7 = Button(frame, text = ques[index].options[6].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[6].inc_vote(frame)).pack()
            but8 = Button(frame, text = ques[index].options[7].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[7].inc_vote(frame)).pack()
            but9 = Button(frame, text = ques[index].options[8].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[8].inc_vote(frame)).pack()
            but10 = Button(frame, text = ques[index].options[9].details[DETAILS[index+1]], width=25, command = lambda *args: ques[index].options[9].inc_vote(frame)).pack()
        return frame


def askQue():
    global q,frame, index, button
    if(len(ques) == index + 1):
        la = Label(root, text = "The End").pack()
        answer()
        return
    button.pack_forget()
    index += 1
    ques[index].get_frame(root).pack()


def answer():
    votes = []
    for i in city:
        votes.append(i.vote)
    x = max(votes)
    i = votes.index(x)
    Label(root, text = "Your Dream Destination is : " + city[i].details[DETAILS[0]] + "!!!").pack()
    te = city[i].message
    frame = Frame(root)
    Message(frame, text = te).pack(side = LEFT)
    fin = "Not sure where to start? Why not check out these deals on www.makemytrip.com/daily-deals/"
    Message(frame, text = fin).pack(side = LEFT)
    frame.pack()


root = Tk()
 
filename = './cities.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        text = list(reader)
except FileNotFoundError:
    print("input csv file not found!")

city = []
for i, row in enumerate(text):
    city.append(Cities(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9] )) 

q = ["Where would you rather visit?", "What would you rather eat?", "Pick a word to describe your ideal vacation?", "What would you like to see?", "What would you rather wear?", "What would you rather drink?", "Pick your favourite season to travel", "Pick an activity"]
ques = []
ques.append(Questions(q[0], [city[0], city[3], city[5], city[9]]))
ques.append(Questions(q[1], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] )) 
ques.append(Questions(q[2], [city[0], city[2], city[5], city[9]]))
ques.append(Questions(q[3], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] ))
ques.append(Questions(q[4], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] ))
ques.append(Questions(q[5], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] )) 
ques.append(Questions(q[6], [city[4], city[8], city[2], city[5]]))
ques.append(Questions(q[7], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] ))

index = -1
button = Button(root, text="Start", width = 25 , height = "3", fg = "green", command= askQue)
button.pack()
  

    
root.title('GUI Travel Quiz')
root.geometry('500x500') 
root.mainloop()
