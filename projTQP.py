import csv

class Questions:
    def __init__(self, question_str, options):
        self.question_str = question_str
        self.options = options
    
    def get_option(self):
        print(self.question_str)
        print(self.options[0])
        print(self.options[1])
        ans = input()
        return ans

class Cities:
    def __init__(self, name, natural, man_made, intent, food, dress, drink, climate, activities):
        self.name = name
        self.natural = natural
        self.man_made = man_made
        self.intent = intent
        self.food = food
        self.dress = dress
        self.drink = drink
        self.climate = climate
        self.activities = activities 
        self.vote = 0
    
    def inc_vote(self):
        self.vote += 1

filename = './cities.csv'

with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    text = list(reader)

city = []
for i, row in enumerate(text):
    city.append(Cities(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    #print(city[i].name)

q = ["Where would you rather visit?", "What would you rather eat?", "What would you rather wear?", "What would you rather enjoy doing?","What would you rather like to see?","Which of these activities sound the most exciting?", "Which climate are you most comfortable with?", "What would you rather drink?"]
ques = []
ques.append(Questions(q[0], [city[0].natural, city[1].natural] ))
ques.append(Questions(q[1], [city[0].food, city[1].food] ))
ans = ques[0].get_option()
city[int(ans) - 1].inc_vote()
ans = ques[1].get_option()
city[int(ans) - 1].inc_vote()
#print(city[0].vote)
#print(city[1].vote)
votes = []
for i in city:
    votes.append(i.vote)
x = max(votes)
i = votes.index(x)
print(city[i].name)
# print(max(votes))

# ques.append(Questions(q[1], [city[1].natural, city[7].natural,city[7].natural]))
# ques.append(Questions(q[2], city[7].natural))
# ques.append(Questions(q[3], city[7].natural))
#     ans = []
#     ans.append(city)
#     print(que)
#     print(city[0].natural)
#     print(city[1].natural)
#     # print(city[2].natural)
#     # print(city[3].natural)
#     ans = input()
#     if(ans == ):

