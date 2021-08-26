from os import system
import sevebluedownloader as vd
loop = True
print("Made with <3 by 7blue")
while(loop):
    print("1. Download Single Video")
    print("2. Download Multiple Video")
    print("3. Download Single Audio")
    print("4. Download Multiple Audio")
    print("5. Download Playlist Videos")
    print("6. Exit")
    option = int(input("Choose the options : "))
    if option == 1:
        url = input("Enter Youtube URL : ")
        loc = input("Enter Location URL( or Enter D to save to downloads):  ")
        if loc == "D" or loc  == "d":
            loc = "Youtube Downloads"
        vd.downloadnow(url,loc,'v')
    elif option == 2:
        print("Enter url seprated by white space ")
        urls = [str(x) for x in input().split()]
        loc = input("Enter Location URL : ")
        for url in urls:
            vd.downloadnow(url,loc,'v')
    elif option == 3:
        url = input("Enter Youtube URL : ")
        loc = input("Enter Location URL : ")
        vd.downloadnow(url,loc,'a')
    elif option == 4:
        print("Enter url seprated by white space ")
        urls = [str(x) for x in input().split()]
        loc = input("Enter Location URL : ")
        for url in urls:
            vd.downloadnow(url,loc,'a')
    elif option == 5:
        url = input("Enter Youtube URL : ")
        loc = input("Enter Location URL : ")
        vd.playlistvid(url,loc)
    elif option == 6:
        loop = False
    else:
        continue

