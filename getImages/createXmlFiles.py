import os, json, sys

# with open('cards.json') as f:# have to have cards.json in current dir
#     JsonData=json.load(f)

with open ('xmlTemplate_minion.txt','r+') as f:# have to have xmlTemplate.txt in current dir
    count=1
    data=f.read()
    for filename in os.listdir('minion_cards'):
        path= os.path.abspath(filename)
        Id=filename.replace('.png','')
        flag=0
        # for card in JsonData:
        #     if (card['id']==Id):
        #         # only if a card has all 3 of these, will we consider it
        #         if ('attack' in card.keys()) and ('cost' in card.keys()) and ('health' in card.keys()):
        #             cost, attack, health = card['cost'], card['attack'], card['health']
        #             break
        #         else:
        #             flag=1
        #             break
                
        if(flag==0):
            with open('minionCards_labelled/{}.xml'.format(Id),'w+') as a: # have to have an empty directory called labelledCards
                a.write(data.format(filename, path))   # , cost, attack, health))
            print(count, end=", ")
            sys.stdout.flush()
            count+=1