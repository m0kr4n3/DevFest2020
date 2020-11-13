from requests import get
from json import loads,dumps
from re import match, IGNORECASE

counter=0

for year in range(2015,2020):
    for month in range(1,13):
        url = f"https://www.google.com/doodles/json/{year}/{month}"
        r=get(url=url).text
        d=loads(r)
        for i in reversed(d):
            
            if (match("algeri",i["name"],IGNORECASE) is not None) or (match("الجزائر",i["name"],IGNORECASE) is not None):
                counter+=1
                print("It had been made visible in {}".format(i["run_date_array"]))

print("The number of Google Doodles that had been made visible in Algeria in the period (01-01-2015 - 01-01-2020) is {}".format(counter))

