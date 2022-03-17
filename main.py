import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

national_team_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstenationalmannschaften/marktwertetop"

wr_club_val_url = "https://www.transfermarkt.com.tr/spieler-statistik/wertvollstemannschaften/marktwertetop"
tr_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=174&kontinent_id=0&yt0=G%C3%B6ster"
eng_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=189&kontinent_id=0&yt0=G%C3%B6ster"
ita_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=75&kontinent_id=0&yt0=G%C3%B6ster"
esp_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=157&kontinent_id=0&yt0=G%C3%B6ster"
fra_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=50&kontinent_id=0&yt0=G%C3%B6ster"
ger_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=40&kontinent_id=0&yt0=G%C3%B6ster"
bel_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=19&kontinent_id=0&yt0=G%C3%B6ster"
net_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=122&kontinent_id=0&yt0=G%C3%B6ster"
por_club_val_url = "https://www.transfermarkt.com.tr/vereins-statistik/wertvollstemannschaften/marktwertetop/plus/0/galerie/0?land_id=136&kontinent_id=0&yt0=G%C3%B6ster"

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


champions_url = "https://www.transfermarkt.com.tr/uefa-champions-league/marktwerte/pokalwettbewerb/CL"
europa_url = "https://www.transfermarkt.com.tr/europa-league/marktwerte/pokalwettbewerb/EL"
superlig_url = "https://www.transfermarkt.com.tr/super-lig/marktwerte/wettbewerb/TR1"
premier_url = "https://www.transfermarkt.com.tr/premier-league/marktwerte/wettbewerb/GB1"
bundesliga_url = "https://www.transfermarkt.com.tr/1-bundesliga/marktwerte/wettbewerb/L1"
ligue1_url = "https://www.transfermarkt.com.tr/ligue-1/marktwerte/wettbewerb/FR1"
laliga_url = "https://www.transfermarkt.com.tr/primera-division/marktwerte/wettbewerb/ES1"
seria_url = "https://www.transfermarkt.com.tr/serie-a/marktwerte/wettbewerb/IT1"



playerList1 = []
playerList2 = []

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
    #? MOST VALUABLE TEAMS
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

    #? MOST VALUABLE PLAYERS
    elif choice == 2:
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

    #? NATIONAL TEAM VALUES
    elif choice == 3:
        nationallist = []
        valuelist = []
        list_national_team = soup.find("table",{"class":"items"}).find("tbody")
        no = 0

        for j in list_national_team.find_all("tr"):
            national_name = j.find_all("td")[1].text.strip()
            nationallist.append(national_name)
            valuefind= j.find_all("td",{"class":"rechts"})
            no += 1
            for v in valuefind:
                value = v.find("b")
                valuelist.append(value.text)

        no = 1
        value_no = 0
        for n in range(0,50,2):
            x = True
            if x == True:
                for v in range(value_no,50,2):
                    print(str(no).rjust(2), nationallist[n].ljust(70,"."), valuelist[v].ljust(30))
                    no += 1
                    x = False
                    break
            value_no += 1
        print("-"*100)
        playerList1.clear()

    


#getSoup(wr_club_val_url, 1)

"""
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
"""

#getSoup(national_team_val_url, 3)
getSoup(champions_url, 2)
getSoup(europa_url, 2)
getSoup(superlig_url, 2)
getSoup(premier_url, 2)
getSoup(bundesliga_url, 2)
getSoup(seria_url, 2)
getSoup(laliga_url, 2)
getSoup(ligue1_url, 2)

