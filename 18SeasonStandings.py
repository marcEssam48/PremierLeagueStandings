import DataCleaning.Cleaning as clean
from progress.bar import Bar
import time
import sys
import time
from tqdm import tqdm


MatchesDataFrame = clean.ReadExcel()
NumberOfSeasons = clean.GetNumberOfSeasons(MatchesDataFrame)
SeasonCategorizedDataFrame = clean.AddingSeason(MatchesDataFrame,NumberOfSeasons)
UniqueSeasons = clean.GetUniqueSeasons(SeasonCategorizedDataFrame)

TeamsPerSeasonDictionary = {}
PointsPerTeamPerSeason = {}
GoalsPerTeamPerSeason = {}
TeamPoints = {}
TeamGoals = {}
TeamsList = []
GoalList = []
GoalsRecievedList = []
RecievedGoalsPerTeamPerSeason = {}
MatchesPlayedPerTeamPerSeason = {}
MatchesList = []

toolbar_width = len(UniqueSeasons)

for Season in UniqueSeasons:
    Teams = clean.GetTeamsOfEachSeason(Season,SeasonCategorizedDataFrame)
    TeamsPerSeasonDictionary[Season] = Teams

print("Calculating Points and Goals for Every Team per Season ... ")

for Season in tqdm(TeamsPerSeasonDictionary.keys()):
    time.sleep(2)
    for Team in TeamsPerSeasonDictionary[Season]:
        TeamPoints = clean.GetTeamPointsPerSeason(Season,Team, SeasonCategorizedDataFrame)
        TeamGoals = clean.TeamGoalScored(Season,Team,SeasonCategorizedDataFrame)
        TeamRecievedGoals = clean.TeamGoalRecieved(Season,Team,SeasonCategorizedDataFrame)
        MatchesList = clean.NumberOfMatchesPlayed(Season,Team,SeasonCategorizedDataFrame)

        TeamsList.append(TeamPoints)
        GoalList.append(TeamGoals)
        GoalsRecievedList.append(TeamRecievedGoals)

    PointsPerTeamPerSeason[Season] = TeamsList
    GoalsPerTeamPerSeason[Season] = GoalList
    RecievedGoalsPerTeamPerSeason[Season] = GoalsRecievedList
    MatchesPlayedPerTeamPerSeason[Season] = MatchesList


DataFrameOfPoints = clean.DictionaryToDataFrame(PointsPerTeamPerSeason)
DataFrameOfGoals =  clean.DictionaryToDataFrameGoals(DataFrameOfPoints,GoalsPerTeamPerSeason,"Goals Scored")
DataFrameOfGoalsRecieved = clean.DictionaryToDataFrameGoals(DataFrameOfPoints,RecievedGoalsPerTeamPerSeason,"Goals Received")
DataFrameOfMatchesPlayed = clean.DictionaryToDataFrameGoals(DataFrameOfPoints,MatchesPlayedPerTeamPerSeason,"Matches Played")





