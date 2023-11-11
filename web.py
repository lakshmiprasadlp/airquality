import os
import time
import requests
import sys

def scrapp_html():
    for year in range(2013, 2020):
        for mounth in range(1, 13):
            if mounth < 10:
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(mounth, year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(mounth, year)

            texts = requests.get(url)
            text_utf = texts.text.encode('utf-8')

            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year, mounth), "wb") as output:
                output.write(text_utf)

            sys.stdout.flush()

if __name__ == "__main__":
    start_time = time.time()
    scrapp_html()
    stop_time = time.time()
    print("Time taken {}".format(stop_time - start_time))
