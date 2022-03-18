from sunau import AUDIO_FILE_ENCODING_ADPCM_G723_3
import requests
from bs4 import BeautifulSoup
import urls
import info

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

playerList1 = []
playerList2 = []

def positionSelect():
    temp = input("1- Tümü\n2- Kaleciler\n3- Defanslar\n4- Orta Sahalar\n5- Forvetler\n0- Geri\nSeçiminiz: ")
    print("-"*30)

    return temp

def clubCheck(club):
    if not club:
        club = "No Club Name"
    else:
        club = club.string
        print("2")
    return club

def titleScript(param, title_param):
    if title_param == "teams":
        title = param.find("h2",{"class":"content-box-headline"}).string.strip().upper()
        print("-"*100)
        print("|" + title.rjust(60) + "|".rjust(39," "))
        print("-"*100)
    elif title_param == "players":
        title = param.find("h2",{"class":"content-box-headline"}).string.strip().upper()
        print("-"*100)
        print("|" + title.rjust(60) + "|".rjust(39," "))
        print("-"*100)
    elif title_param == "national":
        title = param.find("h2",{"class":"content-box-headline"}).string.strip().upper()
        print("-"*100)
        print("|" + title.rjust(60) + "|".rjust(39," "))
        print("-"*100)
    elif title_param == "transfers":
        title = param.find("h2",{"class":"content-box-headline"}).string.strip().upper()
        print("-"*100)
        print("|" + title.rjust(60) + "|".rjust(39," "))
        print("-"*100)

def getSoup(url, choice):
    html_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_request.content, "html.parser")
    if choice == 1:
        getListTeams(soup)
    elif choice == 2:
        getListPlayers(soup)
    elif choice == 3:
        getListNational(soup)
    elif choice == 4:
        getListTransfer(soup)

def getListTeams(soup):
    # ? MOST VALUABLE TEAMS
    list_club = soup.find("table", {"class": "items"}).find("tbody")
    no = 0
    titleScript(soup, title_param="teams")

    for temp_club in list_club.find_all("tr"):
        club = temp_club.find_all("td")[2].text.strip()
        league = temp_club.find_all("td")[3].text.strip()
        value = temp_club.find_all("td")[4].text.strip()
        no += 1
        print(str(no).rjust(2), club.ljust(50, "."), league.ljust(30), value.strip().ljust(5))

def getListPlayers(soup):
    # ? MOST VALUABLE PLAYERS
    list_footballer = soup.find("table", {"class": "items"}).find("tbody")
    no = 0
    titleScript(soup, title_param="players")

    for temp_name_value in list_footballer.find_all("td", {"class": "hauptlink"}):
        add1 = temp_name_value.find("a").text.strip()

        no += 1
        playerList1.append(add1)

    no = 1
    value_no = 1
    for name in range(0, 50, 2):
        x = True
        if x == True:
            for value in range(value_no, 50, 2):
                print(str(no).rjust(2), playerList1[name].ljust(80, "."), playerList1[value].ljust(30))
                no += 1
                x = False
                break
        value_no += 2
    print("-"*100)
    playerList1.clear()

def getListNational(soup):
    # ? NATIONAL TEAM VALUES
    nationallist = []
    valuelist = []
    list_national_team = soup.find("table", {"class": "items"}).find("tbody")
    no = 0
    titleScript(soup, title_param="national")

    for temp_national in list_national_team.find_all("tr"):
        national_name = temp_national.find_all("td")[1].text.strip()
        nationallist.append(national_name)
        valuefind = temp_national.find_all("td", {"class": "rechts"})
        no += 1
        for v in valuefind:
            value = v.find("b")
            valuelist.append(value.text)

    no = 1
    value_no = 0
    for n in range(0, 50, 2):
        x = True
        if x == True:
            for v in range(value_no, 50, 2):
                print(str(no).rjust(2), nationallist[n].ljust(80, "."), valuelist[v].ljust(30))
                no += 1
                x = False
                break
        value_no += 1
    playerList1.clear()

def getListTransfer(soup):
    # ? MOST VALUABLE TRANSFERS
    list_transfer = soup.find("table", {"class": "items"}).find("tbody")
    no = 0
    titleScript(soup, title_param="transfers")

    for temp_name_value in list_transfer.find_all("td", {"class": "hauptlink"}):
        add2 = temp_name_value.find("a").text.strip()
        no += 1
        playerList1.append(add2)

    no = 1
    club_name = 1
    value_no = 2
    for name in range(0, 75, 3):
        x = True
        if x == True:
            for club in range(club_name, 75, 3):
                for value in range(value_no, 75, 3):
                    print(str(no).rjust(2), playerList1[name].ljust(50, "."), playerList1[club].ljust(30), playerList1[value].strip().ljust(5))
                    no += 1
                    value_no += 3
                    club_name += 3
                    x = False
                    break
                break
    print("-"*100)
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
            first_choice = input("1- En değerli kulüpler\n2- En değerli futbolcular \n3- En değerli milli takımlar\n4- En pahalı transferler\n0- Çıkış\nSeçiminiz?: ")
            print("-"*30)

            if first_choice == "0":
                loop = False
                break
            else:
                start = True

        if start == True:
            if first_choice == "1":
                choice = input("1- Genel en değerli kulüpler\n2- Türkiye\n3- İngiltere\n4- İspanya\n5- Almanya\n6- İtalya\n7- Fransa\n8- Portekiz\n9- Hollanda\n10- Belçika\n0- Geri\nSeçiminiz: ")
                print("-"*30)
                if choice == "0":
                    start = False
                else:
                    if choice == "1":
                        getSoup(urls.wr_club_val, 1)  # ! GENEL
                    elif choice == "2":
                        getSoup(urls.tr_club_val, 1)  # ! TÜRKİYE
                    elif choice == "3":
                        getSoup(urls.eng_club_val, 1)  # ! İNGİLTERE
                    elif choice == "4":
                        getSoup(urls.esp_club_val, 1)  # ! İSPANYA
                    elif choice == "5":
                        getSoup(urls.ger_club_val, 1)  # ! ALMANYA
                    elif choice == "6":
                        getSoup(urls.ita_club_val, 1)  # ! İTALYA
                    elif choice == "7":
                        getSoup(urls.fra_club_val, 1)  # ! FRANSA
                    elif choice == "8":
                        getSoup(urls.por_club_val, 1)  # ! PORTEKİZ
                    elif choice == "9":
                        getSoup(urls.net_club_val, 1)  # ! HOLLANDA
                    elif choice == "10":
                        getSoup(urls.bel_club_val, 1)  # ! BELÇİKA

            elif first_choice == "2":
                choice = input("1- Genel en değerli futbolcular\n2- Türkiye\n3- İngiltere\n4- İspanya\n5- Almanya\n6- İtalya\n7- Fransa\n8- Portekiz\n9- Arjantin\n10- Brezilya\n0- Geri\nSeçiminiz: ")
                print("-"*30)
                if choice == "0":
                    start = False
                else:
                    if choice == "1": # ! GENEL
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.wr_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.wr_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.wr_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.wr_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.wr_frwd_val, 2)
                    elif choice == "2": # ! TÜRKİYE
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.tr_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.tr_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.tr_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.tr_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.tr_frwd_val, 2)
                    elif choice == "3": # ! İNGİLTERE
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.eng_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.eng_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.eng_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.eng_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.eng_frwd_val, 2)
                    elif choice == "4": # ! İSPANYA
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.esp_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.esp_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.esp_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.esp_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.esp_frwd_val, 2)
                    elif choice == "5": # ! ALMANYA
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.ger_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.ger_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.ger_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.ger_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.ger_frwd_val, 2)
                    elif choice == "6": # ! İTALYA
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.ita_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.ita_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.ita_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.ita_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.ita_frwd_val, 2)
                    elif choice == "7": # ! FRANSA
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.fra_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.fra_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.fra_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.fra_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.fra_frwd_val, 2)
                    elif choice == "8": # ! PORTEKİZ
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.por_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.por_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.por_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.por_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.por_frwd_val, 2)
                    elif choice == "9": # ! ARJANTİN
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.arg_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.arg_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.arg_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.arg_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.arg_frwd_val, 2)
                    elif choice == "10": # ! BREZİLYA
                        position_choice = positionSelect()
                        if position_choice == "0":
                            break
                        elif position_choice == "1":
                            getSoup(urls.bre_footballer_all_val, 2)
                        elif position_choice == "2":
                            getSoup(urls.bre_gkp_val, 2)
                        elif position_choice == "3":
                            getSoup(urls.bre_def_val, 2)
                        elif position_choice == "4":
                            getSoup(urls.bre_mid_val, 2)
                        elif position_choice == "5":
                            getSoup(urls.bre_frwd_val, 2)
            
            elif first_choice == "3": 
                getSoup(urls.national_team_val, 3)

            elif first_choice == "4":
                choice = input("1- Genel en pahalı transferler\n2- Uyruklarına göre en pahalı transferler\n3- Sezonlara göre en pahalı transferler\n0- Geri\nSeçiminiz: ")
                print("-"*30)
                if choice == "0":
                    start = False
                else:
                    if choice == "1": # ! GENEL
                        getSoup(urls.wr_transfer_all, 4)
                    elif choice == "2":
                        nat_choice = input("1- Türkiye\n2- İngiltere\n3- İspanya\n4- Almanya\n5- İtalya\n6- Fransa\n7- Hollanda\n8- Portekiz\n9- Arjantin\n10- Brezilya\n0- Geri\nSeçiminiz: ")
                        print("-"*30)
                        if nat_choice == "0":
                            break
                        elif nat_choice == "1": # ! TÜRKİYE
                            getSoup(urls.tr_transfer_all, 4)
                        elif nat_choice == "2": # ! İNGİLTERE
                            getSoup(urls.eng_transfer_all, 4)
                        elif nat_choice == "3": # ! İSPANYA
                            getSoup(urls.esp_transfer_all, 4)
                        elif nat_choice == "4": # ! ALMANYA
                            getSoup(urls.ger_transfer_all, 4)
                        elif nat_choice == "5": # ! İTALYA
                            getSoup(urls.ita_transfer_all, 4)
                        elif nat_choice == "6": # ! FRANSA
                            getSoup(urls.fra_transfer_all, 4)
                        elif nat_choice == "7": # ! HOLLANDA
                            getSoup(urls.net_transfer_all, 4)
                        elif nat_choice == "8": # ! PORTEKİZ
                            getSoup(urls.por_transfer_all, 4)
                        elif nat_choice == "9": # ! ARJANTİN
                            getSoup(urls.arg_transfer_all, 4)
                        elif nat_choice == "10": # ! BREZİLYA
                            getSoup(urls.bre_transfer_all, 4)
                    elif choice == "3":
                        season_choice = input("1-  2022/2023\n2-  2021/2022\n3-  2020/2021\n4-  2019/2020\n5-  2018/2019\n6-  2017/2018\n7-  2016/2017\n8-  2015/2016\n9-  2014/2015\n10- 2013/2014\n11- 2012/2013\n12- 2011/2012\n13- 2010/2011\n14- 2009/2010\n15- 2008/2009\n16- 2010/2008\n17- 2006/2007\n18- 2005/2006\n19- 2004/2005\n20- 2003/2004\n21- 2002/2003\n22- 2001/2002\n23- 2000/2001\n0- Geri\nSeçiminiz: ")
                        print("-"*30)
                        if season_choice == "0":
                            break
                        elif season_choice == "1": 
                            getSoup(urls.wr_transfer_22_23, 4)
                        elif season_choice == "2": 
                            getSoup(urls.wr_transfer_21_22, 4)
                        elif season_choice == "3": 
                            getSoup(urls.wr_transfer_20_21, 4)
                        elif season_choice == "4": 
                            getSoup(urls.wr_transfer_19_20, 4)
                        elif season_choice == "5": 
                            getSoup(urls.wr_transfer_18_19, 4)
                        elif season_choice == "6": 
                            getSoup(urls.wr_transfer_17_18, 4)
                        elif season_choice == "7": 
                            getSoup(urls.wr_transfer_16_17, 4)
                        elif season_choice == "8": 
                            getSoup(urls.wr_transfer_15_16, 4)
                        elif season_choice == "9": 
                            getSoup(urls.wr_transfer_14_15, 4)
                        elif season_choice == "10": 
                            getSoup(urls.wr_transfer_13_14, 4)
                        elif season_choice == "11": 
                            getSoup(urls.wr_transfer_12_13, 4)
                        elif season_choice == "12": 
                            getSoup(urls.wr_transfer_11_12, 4)
                        elif season_choice == "13": 
                            getSoup(urls.wr_transfer_10_11, 4)
                        elif season_choice == "14": 
                            getSoup(urls.wr_transfer_09_10, 4)
                        elif season_choice == "15": 
                            getSoup(urls.wr_transfer_08_09, 4)
                        elif season_choice == "16": 
                            getSoup(urls.wr_transfer_07_08, 4)
                        elif season_choice == "17": 
                            getSoup(urls.wr_transfer_06_07, 4)
                        elif season_choice == "18": 
                            getSoup(urls.wr_transfer_05_06, 4)
                        elif season_choice == "19": 
                            getSoup(urls.wr_transfer_04_05, 4)
                        elif season_choice == "20": 
                            getSoup(urls.wr_transfer_03_04, 4)
                        elif season_choice == "21": 
                            getSoup(urls.wr_transfer_02_03, 4)
                        elif season_choice == "22": 
                            getSoup(urls.wr_transfer_01_02, 4)
                        elif season_choice == "23": 
                            getSoup(urls.wr_transfer_00_01, 4)


            start = False



menu()
#jgetSoup(urls.most_transfer, 2)