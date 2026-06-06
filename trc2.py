from trc import *
satır=0
for bilgi in bilgiler:          #BURAK ŞAHİN TARAFINDAN KODLANMIŞTIR
    satır+=1
    print(satır)
    try:
        print(bilgi["status"])
    except KeyError:
        pass