import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

club_value_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstemannschaften/marktwertetop"
footballer_value_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop"

playerList = []

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
        list_footballer = soup.find("table",{"class":"items"}).find("tbody")
        count = 0

        #TODO title gelecek

        for j in list_footballer.find_all("tr",{"class":"odd"}):
            name = j.find_all("td")[3].text.strip()
            position = j.find_all("td")[4].text.strip()
            age = j.find_all("td")[5].text.strip()
            value = j.find_all("td")[8].text.strip()
            count +=1

            #print(name)
            #print(position)
            #print(age)
            #print(value)

            playerList.append(name)

            #print(str(count).rjust(2), name.ljust(70,"."), age.ljust(30), value.strip().ljust(5))
        
        for a in playerList:
            print(a)


#getSoup(club_value_url, 1)
getSoup(footballer_value_url, 2)
