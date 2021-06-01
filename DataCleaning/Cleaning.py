import pandas as pd



def ReadExcel():
    path = "/Users/markessam/PycharmProjects/PremierLeagueStandings/DataSet/final_dataset.xlsx"
    DataFrame = pd.read_excel(path, sheet_name="premierleague")
    return DataFrame


def GetNumberOfSeasons(DataFrame):
    counter = 0
    for index, row in DataFrame.iterrows():
        if str(row["MW"]).strip() == "38":
            counter += 1

    counter = int(counter / 10)
    return counter

def AddingSeason(DataFrame,counter):
    Season_list = []
    for i in range(0,counter):
        for index,row in DataFrame.iterrows():
            if int(int(row["#"])/381) == i:
                # print(str(row["#"]) + " Season " + str(i+1))
                # row["Season"] = "Season " + str(i+1)
                Season_list.append("Season " + str(i+1))

            else:
                continue
    DataFrame["Season"] = Season_list
    return DataFrame

def GetUniqueSeasons(DataFrame):
    UniquesSeasons = []
    for season in DataFrame["Season"]:
        if season not in UniquesSeasons:
            UniquesSeasons.append(season)
        else:
            continue
    return UniquesSeasons

def GetTeamsOfEachSeason(season,DataFrame):
    TeamsList = []
    for index , row in DataFrame.iterrows():
        if season == str(row["Season"]).strip() and str(row["HomeTeam"]) not in TeamsList:
            TeamsList.append(str(row["HomeTeam"]))
        else:
            continue
    return TeamsList
def GetTeamPointsPerSeason(season,team,DataFrame):
    Homepoints = 0
    AwayPoints = 0
    DrawPoints = 0
    TotalPoints = 0
    TeamsPoints = {}
    for index , row in DataFrame.iterrows():
        if str(row["HomeTeam"]) == team and str(row["Season"]) == season:
            if int(row["FTHG"]) > int(row["FTAG"]) :
                Homepoints+=3
            if int(row["FTHG"]) < int(row["FTAG"]) :
                AwayPoints+=0
            if int(row["FTHG"]) == int(row["FTAG"]):
                DrawPoints+=1
        elif str(row["AwayTeam"]) == team and str(row["Season"]) == season:
            if int(row["FTHG"]) > int(row["FTAG"]) :
                Homepoints+=0
            if int(row["FTHG"]) < int(row["FTAG"]) :
                AwayPoints+=3
    TotalPoints = Homepoints + AwayPoints + DrawPoints
    TeamsPoints[team] = TotalPoints
    return TeamsPoints

def TeamGoalScored(season,team,DataFrame):
    HomeGoals = 0
    AwayGoals = 0
    TotalGoals = 0
    TeamGoals = {}
    for index , row in DataFrame.iterrows():
        if str(row["HomeTeam"]) == team and str(row["Season"]) == season:
            HomeGoals+= int(row["FTHG"])
        elif str(row["AwayTeam"]) == team and str(row["Season"]) == season:
            AwayGoals+=int(row["FTAG"])
    TotalGoals = HomeGoals + AwayGoals
    TeamGoals[team] = TotalGoals
    return TeamGoals



def DictionaryToDataFrame(Dictionary):
    DataFrame = pd.DataFrame()
    season_list = []
    Teams_list = []
    Points_list = []
    Matches_played = []
    for season in Dictionary.keys():
        for Teamdict in Dictionary[season]:
            for Team in Teamdict.keys():
                # print(Team)
                points = Teamdict[Team]
                season_list.append(season)
                Teams_list.append(Team)
                Points_list.append(points)
                Matches_played.append("38")

                # DataFrame["Season"] = season
                # DataFrame["Team"] = Team
                # DataFrame["Points"] = points
    DataFrame["Season"] = season_list
    DataFrame["Team"] = Teams_list
    DataFrame["Points"] = Points_list
    return DataFrame

def DictionaryToDataFrameGoals(DataFrameOfPoints,TeamGoals,Column):

    Points_list = []
    for season in TeamGoals.keys():
        for Teamdict in TeamGoals[season]:
            for Team in Teamdict.keys():
                # print(Team)
                points = Teamdict[Team]
                Points_list.append(points)

    DataFrameOfPoints[Column] = Points_list
    return DataFrameOfPoints

def TeamGoalRecieved(Season,Team,SeasonCategorizedDataFrame):
    HomeGoals = 0
    AwayGoals = 0
    TotalGoals = 0
    TeamGoals = {}
    for index, row in SeasonCategorizedDataFrame.iterrows():
        if str(row["HomeTeam"]) == Team and str(row["Season"]) == Season:
            HomeGoals += int(row["FTAG"])
        elif str(row["AwayTeam"]) == Team and str(row["Season"]) == Season:
            AwayGoals += int(row["FTHG"])
    TotalGoals = HomeGoals + AwayGoals
    TeamGoals[Team] = TotalGoals
    return TeamGoals

def NumberOfMatchesPlayed(Season,Team,SeasonCategorizedDataFrame):
    MatchesPlayed = 0
    TeamMatches = {}
    for index,row in SeasonCategorizedDataFrame.iterrows():
        if (str(row["HomeTeam"]) == Team and str(row["Season"]) == Season) or (str(row["AwayTeam"]) == Team and str(row["Season"]) == Season):
            MatchesPlayed+=1
        else:
            continue
    TeamMatches[Team] = MatchesPlayed
    return TeamMatches











