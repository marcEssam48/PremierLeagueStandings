from selenium import webdriver
import time
import  pandas as pd
import tqdm
browser = webdriver.Firefox()
DataFrameStandings = pd.DataFrame()

with pd.ExcelWriter('PremierLeagueTeamsSortedReal.xlsx') as writer:
    for i in range(1,19):
        ClubRank = []
        ClubNames = []
        ClubMatches = []
        ClubWins = []
        ClubDraws = []
        ClubLoses = []
        ClubGoalsScored = []
        ClubGoalsRecieved = []
        ClubGoalsDifference = []
        ClubPoints = []
        # wiki = browser.get('https://www.wikipedia.org/')
        Season = "Season " + str(i)
        if int(i/10) == 0:
            page = browser.get('https://www.google.com/search?client=firefox-b-d&q=premier+league+standings+200'+str(i))

        else:
            page = browser.get('https://www.google.com/search?client=firefox-b-d&q=premier+league+standings+20' + str(i))
        HTML = browser.page_source
        try:
            EnglishOption = browser.find_element_by_link_text("Change to English").click()
        except:
            print("Changed To English")
        new_HTML = browser.page_source
        SeeMore = browser.find_element_by_class_name("mtqGb").click()
        StandingTables = browser.page_source
        # StandingsTable = browser.find_element_by_class_name("Jzru1c")
        # print(StandingsTable)
        browser.refresh()
        x= browser.find_elements_by_xpath('//table[@class="Jzru1c"]/tbody/tr/td')
        counter = 1
        for r in x:
            if r.text != "":
                if   counter / 1 ==1:
                    ClubRank.append(r.text)
                    # print(r.text)
                elif counter / 1 ==2:
                    ClubNames.append(r.text)
                elif counter / 1 ==3:
                    ClubMatches.append(r.text)
                elif counter / 1 ==4:
                    ClubWins.append(r.text)
                elif counter / 1 ==5:
                    ClubDraws.append(r.text)
                elif counter / 1 ==6:
                    ClubLoses.append(r.text)
                elif counter / 1 ==7:
                    ClubGoalsScored.append(r.text)
                elif counter / 1 ==8:
                    ClubGoalsRecieved.append(r.text)
                elif counter / 1 ==9:
                    ClubGoalsDifference.append(r.text)
                elif counter / 1 ==10:
                    ClubPoints.append(r.text)
                    counter = 0
                counter+=1
        try:
            DataFrameStandings["Rank"] = ClubRank
            DataFrameStandings["Club Name"] = ClubNames
            DataFrameStandings["Matches Played"] = ClubMatches
            DataFrameStandings["Win"] = ClubWins
            DataFrameStandings["Draw"] = ClubDraws
            DataFrameStandings["Lose"] = ClubLoses
            DataFrameStandings["Goals Scored"] = ClubGoalsScored
            DataFrameStandings["Goals Received"] = ClubGoalsRecieved
            DataFrameStandings["Goals Difference"] = ClubGoalsDifference
            DataFrameStandings["Points"] = ClubPoints
            time.sleep(10)

        except Exception as e:
            print(e)
            print(Season)

        # print(DataFrameStandings)

        DataFrameStandings.to_excel(writer, sheet_name=Season, index=False)
browser.close()

