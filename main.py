import requests
from bs4 import BeautifulSoup
import urls

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

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
getSoup(urls.wr_footballer_all_val, 2)
getSoup(urls.wr_gkp_val, 2)
getSoup(urls.wr_def_val, 2)
getSoup(urls.wr_mid_val, 2)
getSoup(urls.wr_frwd_val, 2)

getSoup(urls.tr_footballer_all_val, 2)
getSoup(urls.tr_gkp_val, 2)
getSoup(urls.tr_def_val, 2)
getSoup(urls.tr_mid_val, 2)
getSoup(urls.tr_frwd_val, 2)
"""
"""
#getSoup(urls.national_team_val_url, 3)
getSoup(urls.champions, 2)
getSoup(urls.europa, 2)
getSoup(urls.superlig, 2)
getSoup(urls.premier, 2)
getSoup(urls.bundesliga, 2)
getSoup(urls.seria, 2)
getSoup(urls.laliga, 2)
"""
getSoup(urls.ligue1, 2)

