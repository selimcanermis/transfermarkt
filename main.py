import requests
from bs4 import BeautifulSoup
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

club_value_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstemannschaften/marktwertetop"
wr_footballer_all_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop"
wr_gkp_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Torwart&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=0&kontinent_id=0&yt0=G%C3%B6ster"
wr_def_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Abwehr&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=0&kontinent_id=0&yt0=G%C3%B6ster"
wr_mid_val_url ="https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Mittelfeld&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=0&kontinent_id=0&yt0=G%C3%B6ster"
wr_frwd_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Sturm&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=0&kontinent_id=0&yt0=G%C3%B6ster"

tr_footballer_all_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=174&kontinent_id=0&yt0=G%C3%B6ster"
tr_gkp_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Torwart&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=174&kontinent_id=0&yt0=G%C3%B6ster"
tr_def_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Abwehr&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=174&kontinent_id=0&yt0=G%C3%B6ster"
tr_mid_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Mittelfeld&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=174&kontinent_id=0&yt0=G%C3%B6ster"
tr_frwd_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=Sturm&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=174&kontinent_id=0&yt0=G%C3%B6ster"


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

def getSoup(url, choice):
    html_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_request.content, "html.parser")
    getList(soup, choice)

def getList(soup, choice):
    if choice == 1:
        list_club = soup.find("table",{"class":"items"}).find("tbody")
        no = 0

        #TODO title gelecek

        for i in list_club.find_all("tr"):
            club = i.find_all("td")[2].text.strip()
            league = i.find_all("td")[3].text.strip()
            value = i.find_all("td")[4].text.strip()
            no +=1

            
            print(str(no).rjust(2), club.ljust(70,"."), league.ljust(30), value.strip().ljust(5))

    if choice == 2:
        global x
        list_footballer = soup.find("table",{"class":"items"}).find("tbody")
        no = 0

        #TODO title gelecek

        for temp_name_value in list_footballer.find_all("td",{"class":"hauptlink"}):
            add1 = temp_name_value.find("a").text.strip()

            no +=1
            playerList1.append(add1)

        
        no = 1
        value_no = 1
        for name in range(0,50,2):
            x = True
            if x == True:
                for value in range(value_no,50,2):
                    print(str(no).rjust(2), playerList1[name].ljust(70,"."), playerList1[value].ljust(30))
                    no += 1
                    x = False
                    break
            value_no += 2
        print("-"*100)
        playerList1.clear()


#getSoup(club_value_url, 1)
getSoup(wr_footballer_all_val_url, 2)
getSoup(wr_gkp_val_url, 2)
getSoup(wr_def_val_url, 2)
getSoup(wr_mid_val_url, 2)
getSoup(wr_frwd_val_url, 2)

getSoup(tr_footballer_all_val_url, 2)
getSoup(tr_gkp_val_url, 2)
getSoup(tr_def_val_url, 2)
getSoup(tr_mid_val_url, 2)
getSoup(tr_frwd_val_url, 2)