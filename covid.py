import requests
import json
import time

def getConfirmed():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    querystring = {"format":"undefined"}


    data = []

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "a8654270ffmsh76bc6ce4c907108p184fb2jsn32509eaa1391"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)


    JSONResp = json.loads(response.text)

    confirmed = JSONResp[0]['confirmed']
    return confirmed

def getRecovered():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    querystring = {"format":"undefined"}


    data = []

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "a8654270ffmsh76bc6ce4c907108p184fb2jsn32509eaa1391"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)


    JSONResp = json.loads(response.text)
    
    recovered = JSONResp[0]['recovered']
    return recovered

