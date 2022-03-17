import requests
from bs4 import BeautifulSoup
import urls
import info

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
        playerList1.clear()

def menu():
    info.infoScript()
    start = False
    loop = True
    while loop == True:
        if start == False:
            print("-"*30)
            print("TRANSFERMARKT VERILERI".rjust(25))
            print("-"*30)
            first_choice = input("1- En değerli kulüpler\n2- En değerli futbolcular \n3- En değerli milli takımlar \n0- Çıkış\nSeçiminiz?: ")
            print("-"*30)

            if first_choice == "0":
                loop = False
                break
            else:
                start = True
    
        if start == True:
            if first_choice == "1":
                choice = input("1- Genel en değerli kulüpler\n2- Türkiye\n3- İngiltere\n4- İspanya\n5- Almanya\n6- İtalya\n7- Fransa\n8- Portekiz\n9- Hollanda\n10- Belçika\n0- Geri\nYour Choice?: ")
                print("-"*30)
                if choice == "0":
                    start = False
                else:
                    if choice=="1":
                        getSoup(urls.wr_club_val, 1) #! GENEL
                    elif choice=="2":
                        getSoup(urls.tr_club_val, 1) #! TÜRKİYE
                    elif choice=="3":
                        getSoup(urls.eng_club_val, 1) #! İNGİLTERE
                    elif choice=="4":
                        getSoup(urls.esp_club_val, 1) #! İSPANYA
                    elif choice=="5":
                        getSoup(urls.ger_club_val, 1) #! ALMANYA
                    elif choice=="6":
                        getSoup(urls.ita_club_val, 1) #! İTALYA
                    elif choice=="7":
                        getSoup(urls.fra_club_val, 1) #! FRANSA
                    elif choice=="8":
                        getSoup(urls.por_club_val, 1) #! PORTEKİZ
                    elif choice=="9":
                        getSoup(urls.net_club_val, 1) #! HOLLANDA
                    elif choice=="10":
                        getSoup(urls.bel_club_val, 1) #! BELÇİKA

            elif first_choice == "2":
                choice = input("1- Genel en değerli futbolcular\n2- Mevkilerine göre en değerli futbolcular\n0- Geri\nYour Choice?: ")
                print("-"*30)
                if choice == "0":
                    start = False
                else:
                    if choice=="1":
                        getSoup(urls.wr_footballer_all_val, 2) #! GENEL
                    elif choice=="2":
                        position_choice = input("1- Kaleciler\n2- Defanslar\n3- Orta Sahalar\n4- Forvetler\n0- Geri\nYour Choice?: ")
                        print("-"*30)
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.wr_gkp_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.wr_def_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.wr_mid_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.wr_frwd_val, 2)

            elif first_choice == "3":
                getSoup(urls.national_team_val, 3)
            
            start = False

menu()


#getSoup(wr_club_val, 1)

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
#getSoup(urls.ligue1, 2)

