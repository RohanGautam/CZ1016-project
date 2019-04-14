import json, requests
import shutil, sys

url='https://art.hearthstonejson.com/v1/render/latest/enUS/256x/{}.png'

# id='AT_012'

with open('cards.json') as f:
    data=json.load(f)
    count=0; controller=0 # change controller to pause and resume from any download stage
    print('downloading cards: ')
    for card in data:
        count+=1
        print(count, end=", ")
        sys.stdout.flush()

        id=card['id']
        if count>=controller and 'type' in list(card.keys()) and card['type']=='MINION':
            response = requests.get(url.format(id), stream=True)
            with open('minion_cards/{}.png'.format(id), 'wb') as out_file: # have to create this folder
                shutil.copyfileobj(response.raw, out_file)
            del response

