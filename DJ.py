from tkinter import *
from time import sleep
import csv


# def d(view):
#         view.pack_forget()



DETAILS = ['name', 'natural', 'food', 'intent', 'man_made', 'dress', 'drink', 'climate', 'activity']
class Cities:
    def __init__(self, name, natural, man_made, intent, food, dress, drink, climate, activity):
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
        # self.name = name
        # self.natural = natural
        # self.man_made = man_made
        # self.intent = intent
        # self.food = food
        # self.dress = dress
        # self.drink = drink
        # self.climate = climate
        # self.activity = activity 
        self.vote = 0

    
    def inc_vote(self):
        self.vote += 1
        la = Label(root, text = self.details[DETAILS[0]]).pack()
         #frame.pack_forget()
        
        askQue()
        #frame.after(1000, lambda *args: frame.pack_forget())
        # frame.pack_forget()
        # butto_1 = Button(root, text = self.details[DETAILS[0]]).pack()
   
    # def unpackFrame(self, frame):
    #     frame.pack_forget()
    #     askQue()

class Questions:
    def __init__(self, question_str, options):
        self.question_str = question_str
        self.options = options
    

    def get_frame(self, root):
        frame = Frame(root)
        # idea - make 2 frames?
        # view = Frame(frame)
        Label(frame, text = self.question_str).pack()
        #print(len(ques[index].options))
        for opt in ques[index].options:
            but = Button(frame, text = opt.details[DETAILS[index+1]], command = opt.inc_vote).pack()         
            #but = Button(frame, text = opt.details[DETAILS[index+1]]).bind("<Button-1>", opt.inc_vote(frame))
        # butt = Button(view, text = "Next", command = lambda *args: d(view)).pack()
        return frame


    # def unpackFrame(self, frame):
    #     frame.pack_forget()
    #     askQue()

def askQue():
    global q,frame, index, button
    if(len(ques) == index + 1):
    # if(index == 2):
        la = Label(root, text = "The End").pack()
        answer()
        return
    #button.pack_forget()
    index += 1
    ques[index].get_frame(root).pack()

    # for i, q in enumerate(ques):
    # frame = Frame(root)
    # label = Label(frame, text = q.question_str)
    # label.pack()
    # for opt in q.options:
    #     but = Button(frame, text = opt.details[DETAILS[i+1]], command = opt.inc_vote).pack()
    # frame.pack()


def answer():
    votes = []
    for i in city:
        votes.append(i.vote)
    x = max(votes)
    i = votes.index(x)
    Label(root, text = "Your Dream Destination is : " + city[i].details[DETAILS[0]]).pack()


root = Tk()
filename = './cities.csv'

with open(filename) as f:
    reader = csv.reader(f)
    text = list(reader)

city = []
for i, row in enumerate(text):
    city.append(Cities(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    #print(city[i].name)

q = ["Where would you rather visit?", "What would you rather eat?", "What would you rather wear?", "What would you rather enjoy doing?","What would you rather like to see?","Which of these activities sound the most exciting?", "Which climate are you most comfortable with?", "What would you rather drink?"]
ques = []
ques.append(Questions(q[0], [city[0], city[2], city[4], city[9]]))
ques.append(Questions(q[1], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]]))
ques.append(Questions(q[3], [city[0], city[2], city[5], city[9]]))
ques.append(Questions(q[4], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] ))
ques.append(Questions(q[5], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] )) 
ques.append(Questions(q[6], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] ))
ques.append(Questions(q[7], [city[0], city[1], city[2], city[3], city[4], city[5], city[6], city[7], city[8], city[9]] )) 
# for i, q in enumerate(ques):
#     frame = Frame(root)
#     label = Label(frame, text = q.question_str)
#     label.pack()
#     for opt in q.options:
#         but = Button(frame, text = opt.details[DETAILS[i+1]], command = opt.inc_vote).pack()
#     frame.pack()
index = -1
button = Button(root, text="Start", command=askQue).pack()

# votes = []
# for i in city:
#     votes.append(i.vote)
# x = max(votes)
# i = votes.index(x)
# print(city[i].details[DETAILS[0]])
root.mainloop()