import requests
import csv
from datetime import datetime

url = "https://meltonpool.herokuapp.com/games/1/results"
s = requests.session()
now = datetime.now().time()
rowsran = 0
rowsremain = 26827 - rowsran
filename = "results.csv"


def postresult(winner_id, loser_id):
    payload='utf8=%E2%9C%93&authenticity_token=zr9GT7%2FXNXZrdSwJ59uXQzJuL31H4SMrz4hk90jshz%2F9oUmcP6l0rXQCT69pqS59EtTOeeOzjnbClhL85%2BXEFg%3D%3D&result%5Bteams%5D%5B0%5D%5Bplayers%5D=' + winner_id + '&result%5Bteams%5D%5B0%5D%5Brelation%5D=defeats&result%5Bteams%5D%5B1%5D%5Bplayers%5D= ' + loser_id + '&commit=Save%2BResult'
    headers = {
    'Authorization': 'Basic ZnJlZDpmcmVka2FrYQ==',
    'Cookie': '_elovation_session=dGtBTllLa0VxTkNTQjJZOWdTcjlyR2RPVEhuUVk5b0hLWm04dTZpelpHQ2pDa2FsaHJNbjQ4SUhtb0VyY3Jmb01BKzV3NU5xamp3U1pKL3V4N3ZqcWhPUVRLeW5Ic1dkT3hDQVNLY201WGUxWHZSZldJMmtRSkVUTEZTRkd3STRuaWNvR3BMQTFLRFZaV3JjVnpVdFR0a1hFR2xFTWhJaVdCN0pnT1FNeVI0Q2FCeXEvcXpuNHRnSURNL05XYjBGLS1LLytrZ25NWnU3cXpMVENsQ2hZRmhnPT0%3D--a5f8400e1901cdd5a5d34061e78c998de2602de8',
    'Origin': 'https://meltonpool.herokuapp.com',
    'Referer': 'https://meltonpool.herokuapp.com/games/1/results/new',
    }
    response = s.request("POST", url, headers=headers, data=payload)

filename = "results.csv"


with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        now = datetime.now().time()
        rowsran += 1
        rowsremain -=1
        print("Posting result to app: " + row[0] + " defeats " + row[1] + ", results ran:" + str(rowsran) + ", results remaining:" + str(rowsremain) + ", time:" + str(now))
        postresult(row[0],row[1])

