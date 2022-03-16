import requests
from bs4 import BeautifulSoup
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

club_value_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstemannschaften/marktwertetop"
footballer_value_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop"

playerList1 = []
playerList2 = []
x = 0

def clubCheck(club):
    print("buraya da girdim")
    if not club:
        club = "No Club Name"
    else:
        club = club.string
        print("2")
    return club

def getSoup(url, select):
    html_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_request.content, "html.parser")
    getList(soup, select)

def getList(soup, select):
    if select == 1:
        list_club = soup.find("table",{"class":"items"}).find("tbody")
        count = 0

        #TODO title gelecek

        for i in list_club.find_all("tr"):
            club = i.find_all("td")[2].text.strip()
            league = i.find_all("td")[3].text.strip()
            value = i.find_all("td")[4].text.strip()
            count +=1

            
            print(str(count).rjust(2), club.ljust(70,"."), league.ljust(30), value.strip().ljust(5))

    if select == 2:
        global x
        list_footballer = soup.find("table",{"class":"items"}).find("tbody")
        count = 0

        #TODO title gelecek

        for temp_name_value in list_footballer.find_all("td",{"class":"hauptlink"}):
            add1 = temp_name_value.find("a").text.strip()

            count +=1
            playerList1.append(add1)

        count = 0
        print(count)

        for temp_age in list_footballer.find_all("tbody"):
            add2 = temp_age.find_all("tr")[1].text.strip()
            #add2 = temp_age.find("td")[3]
            print(add2)


            count +=1
            playerList2.append(add2)

        for name in range(0,50,2):
            print(playerList1[name])

        for value in range(1,50,2):
            print(playerList1[value])

        """
        for age in range(0,50):
            print(playerList2[age])
        """
            


#getSoup(club_value_url, 1)
getSoup(footballer_value_url, 2)
