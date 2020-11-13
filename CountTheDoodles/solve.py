from requests import get
from json import loads,dumps

counter=0

for year in range(2015,2020):
    for month in range(1,13):
        url = f"https://www.google.com/doodles/json/{year}/{month}?full=1"
        r=get(url=url).text
        d=loads(r)
        for i in reversed(d):
            if "Algeria" in i["countries"]:
                counter+=1
                print("It had been made visible in {}  Counter = {}".format(i["run_date_array"],counter))

print("The number of Google Doodles that had been made visible in Algeria in the period (01-01-2015 - 01-01-2020) is {}".format(counter))

