from tkinter import *
import csv

class Cities:
    def __init__(self, name, natural, man_made, intent, food, dress, drink, climate, activity):
        self.name = name
        self.natural = natural
        self.man_made = man_made
        self.intent = intent
        self.food = food
        self.dress = dress
        self.drink = drink
        self.climate = climate
        self.activity = activity 
        self.vote = 0
    


class Questions:
    def __init__(self, question_str, options):
        self.question_str = question_str
        self.options = options
        self.vote = 0
    
    def get_option(self):
        frame = Frame(root).pack()
        label = Label(frame, text = self.question_str)
        label.pack()
        for i in range(0,len(self.options)):
            button = Button(frame, text = self.options[i], command = lambda *args: self.inc_vote).pack()
        
      
    def inc_vote(self):
        self.vote += 1
        print("dramu")


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
ques.append(Questions(q[0], [city[0].natural, city[2].natural, city[4].natural, city[9].natural] ))
ques.append(Questions(q[1], [city[0].food, city[1].food, city[2].food, city[3].food, city[4].food, city[5].food, city[6].food, city[7].food, city[8].food, city[9].food] ))
ques.append(Questions(q[2], [city[0].dress, city[1].dress, city[2].dress, city[3].dress, city[4].dress, city[5].dress, city[6].dress, city[7].dress, city[8].dress, city[9].dress] ))
# ques.append(Questions(q[3], [city[0].intent, city[2].intent, city[5].intent, city[9].intent] ))
# ques.append(Questions(q[4], [city[0].man_made, city[1].man_made, city[2].man_made, city[3].man_made, city[4].man_made, city[5].man_made, city[6].man_made, city[7].man_made, city[8].man_made, city[9].man_made] ))
# ques.append(Questions(q[5], [city[0].activity, city[1].activity, city[2].activity, city[3].activity, city[4].activity, city[5].activity, city[6].activity, city[7].activity, city[8].activity, city[9].activity] )) 
# ques.append(Questions(q[6], [city[0].climate, city[1].climate, city[2].climate, city[3].climate, city[4].climate, city[5].climate, city[6].climate, city[7].climate, city[8].climate, city[9].climate] ))
# ques.append(Questions(q[7], [city[0].drink, city[1].drink, city[2].drink, city[3].drink, city[4].drink, city[5].drink, city[6].drink, city[7].drink, city[8].drink, city[9].drink] )) 
for k in range(0,len(ques)):
    ques[k].get_option()
    

votes = []
for i in city:
    votes.append(i.vote)
x = max(votes)
i = votes.index(x)
print(city[i].name)
root.mainloop()