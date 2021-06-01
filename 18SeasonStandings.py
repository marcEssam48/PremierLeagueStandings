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
RecievedGoalsPerTeamPerSeason = {}
MatchesPlayedPerTeamPerSeason = {}
DifferenceGoalsPerTeamPerSeason = {}

TeamPoints = {}
TeamGoals = {}
TeamRecievedGoals= {}
TeamMatchesplayed={}
TeamDifferenceGoals={}

TeamsList = []
GoalList = []
GoalsRecievedList = []
MatchesList = []
DifferenceGoals = []


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
        TeamMatchesplayed = clean.NumberOfMatchesPlayed(Season,Team,SeasonCategorizedDataFrame)
        TeamDifferenceGoals = clean.DifferenceGoals(Season,Team,SeasonCategorizedDataFrame)

        TeamsList.append(TeamPoints)
        GoalList.append(TeamGoals)
        GoalsRecievedList.append(TeamRecievedGoals)
        MatchesList.append(TeamMatchesplayed)
        DifferenceGoals.append(TeamDifferenceGoals)

    PointsPerTeamPerSeason[Season] = TeamsList
    GoalsPerTeamPerSeason[Season] = GoalList
    RecievedGoalsPerTeamPerSeason[Season] = GoalsRecievedList
    MatchesPlayedPerTeamPerSeason[Season] = MatchesList
    DifferenceGoalsPerTeamPerSeason[Season] = DifferenceGoals
    break


DataFrameOfTeams = clean.DictionaryToDataFrame(PointsPerTeamPerSeason)
DataFrameOfMatchesPlayed = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,MatchesPlayedPerTeamPerSeason,"Matches Played")
DataFrameOfGoals =  clean.DictionaryToDataFrameGoals(DataFrameOfTeams,GoalsPerTeamPerSeason,"Goals Scored")
DataFrameOfGoalsRecieved = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,RecievedGoalsPerTeamPerSeason,"Goals Received")
DataFrameOfDifferenceGoals = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,DifferenceGoalsPerTeamPerSeason,"Difference Goals")
DataFrameOfPoints = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,PointsPerTeamPerSeason,"Points")
print(DataFrameOfPoints)








