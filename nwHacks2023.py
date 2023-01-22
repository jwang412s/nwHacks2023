import requests
import json

CLIENT_ID = '833b6467092e126472037b42fa9794f8'
# url = 'https://api.myanimelist.net/v2/anime?q=Bleach&limit=1'
url = 'https://api.myanimelist.net/v2/anime?q='
limit = '&limit=5'
animeNames = []

layout = [[sg.Text('Enter anime name: '), sg.Input(key='-IN-')], 
[sg.Text('Output', size=(50,10), key='-OUT-')], [sg.Button('OK'), sg.Button('EXIT')]]

window = sg.Window('Title', layout)


while True:
    
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    
    window['-OUT-'].update(values['-IN-'])

window.close()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def nameappend(obj):
    # create a list of anime from the response
    for d in obj.json()['data']:
        name = d['node']['title']
        animeNames.append(name)

# response = requests.get(url, headers={'X-MAL-CLIENT-ID': CLIENT_ID})


recommendedAnimeOne = input('Search:\n')
recommendedAnimeOneNumber = 0
response1 = requests.get(url + recommendedAnimeOne + limit, headers={'X-MAL-CLIENT-ID': CLIENT_ID})
nameappend(response1)
while recommendedAnimeOneNumber > 5 or recommendedAnimeOneNumber < 1:
    print("Please input a value between 1 and 5")
    recommendedAnimeOneNumber = int(input('1) ' + animeNames[0] + '\n'
                                '2) ' + animeNames[1] + '\n'
                                '3) ' + animeNames[2] + '\n'
                                '4) ' + animeNames[3] + '\n'
                                '5) ' + animeNames[4] + '\n'))
# recommendedAnimeTwo = input("Enter Anime Number Two:")
# response2 = requests.get(url + recommendedAnimeTwo + limit, headers={'X-MAL-CLIENT-ID': CLIENT_ID}).status_code == 400
# recommendedAnimeOne = input("1) " +  + "\n"
#                             "2) " +  + "\n"
#                             "3) " +  + "\n"
#                             "4) " +  + "\n"
#                             "5) " +  + "\n")

# jprint(response.json());


def animeListClear():
    animeNames = []
