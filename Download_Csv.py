import urllib.request
from urllib import request

def Download_CSV_File(csv_url):
    text = request.urlopen(csv_url)
    csv = text.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest =  r"CSV_TRIAL.csv"
    fx = open(dest,"w")
    for line in lines:
        fx.write(line + "\n" )
    fx.close()

Download_CSV_File("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv")



