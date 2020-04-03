
from tkinter import *
import csv
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
        frame.pack_forget()
        butto_1 = Button(root, text = self.details[DETAILS[0]]).pack()


class Questions:
    def __init__(self, question_str, options):
        self.question_str = question_str
        self.options = options


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
# ques.append(Questions(q[3], [city[0], city[2], city[5], city[9]]))
# ques.append(Questions(q[4], [city[0].man_made, city[1].man_made, city[2].man_made, city[3].man_made, city[4].man_made, city[5].man_made, city[6].man_made, city[7].man_made, city[8].man_made, city[9].man_made] ))
# ques.append(Questions(q[5], [city[0].activity, city[1].activity, city[2].activity, city[3].activity, city[4].activity, city[5].activity, city[6].activity, city[7].activity, city[8].activity, city[9].activity] )) 
# ques.append(Questions(q[6], [city[0].climate, city[1].climate, city[2].climate, city[3].climate, city[4].climate, city[5].climate, city[6].climate, city[7].climate, city[8].climate, city[9].climate] ))
# ques.append(Questions(q[7], [city[0].drink, city[1].drink, city[2].drink, city[3].drink, city[4].drink, city[5].drink, city[6].drink, city[7].drink, city[8].drink, city[9].drink] )) 
for i, q in enumerate(ques):
    frame = Frame(root)
    label = Label(frame, text = q.question_str)
    label.pack()
    for opt in q.options:
        but = Button(frame, text = opt.details[DETAILS[i+1]], command = opt.inc_vote).pack()
    frame.pack()

# votes = []
# for i in city:
#     votes.append(i.vote)
# x = max(votes)
# i = votes.index(x)
# # print(city[i].name)
root.mainloop()