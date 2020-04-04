import pandas as pd
data = pd.read_csv('cities.csv', sep=r'\s*,\s*',
                   header=0, encoding='ascii', engine='python')
df = pd.DataFrame(data)
df["votes"] = 0
q = ["Where would you rather visit?", "What would you rather eat?", "What would you rather wear?", "What would you rather enjoy doing?",
     "What would you rather like to see?", "Which of these activities sound the most exciting?", "Which climate are you most comfortable with?", "What would you rather drink?"]
col = ["Name", "TOC", "Monuments", "Activities",
       "Food", "Clothes", "Drinl", "Climate", "Famous"]
def iv(df, key, val):
    l = []
    for i in df["votes"]:
        l.append(i)
    for i, k in enumerate(df[key]):
        if k == val:
            l[i] = l[i] + 1
    df["votes"] = l
    return df


k = 1
for ques in q:
    print(ques)
    key = col[k]
    l = [x for x in df[key]]
    l1 = list(set(l))
    print(l1)
    c = int(input('Enter choice')) - 1
    ch = l[c]
    df = iv(df, key, ch)
    k += 1
p = df[df.votes == df.votes.max()]
print(p[["Name", "votes"]])