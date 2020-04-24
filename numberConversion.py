from num2words import num2words as n2w
import covid

def getConfirmed():
    confirmed = n2w(covid.getConfirmed())
    return confirmed

def getRecovered():
    recovered = n2w(covid.getRecovered())
    return recovered
