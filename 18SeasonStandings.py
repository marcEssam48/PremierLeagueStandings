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
WinsPerTeamPerSeason = {}
DrawsPerTeamPerSeason = {}
LosePerTeamPerSeason = {}

TeamPoints = {}
TeamGoals = {}
TeamRecievedGoals= {}
TeamMatchesplayed={}
TeamDifferenceGoals={}
TeamWins = {}
TeamDraws = {}
TeamLoses = {}


TeamsList = []
GoalList = []
GoalsRecievedList = []
MatchesList = []
DifferenceGoals = []
Wins = []
Draws = []
Loses = []


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
        TeamWins  = clean.GetNumberOfWins(Season, Team, SeasonCategorizedDataFrame,"W")
        TeamDraws = clean.GetNumberOfWins(Season, Team, SeasonCategorizedDataFrame,"D")
        TeamLoses = clean.GetNumberOfWins(Season, Team, SeasonCategorizedDataFrame,"L")

        TeamsList.append(TeamPoints)
        GoalList.append(TeamGoals)
        GoalsRecievedList.append(TeamRecievedGoals)
        MatchesList.append(TeamMatchesplayed)
        DifferenceGoals.append(TeamDifferenceGoals)
        Wins.append(TeamWins)
        Draws.append(TeamDraws)
        Loses.append(TeamLoses)

    PointsPerTeamPerSeason[Season] = TeamsList
    GoalsPerTeamPerSeason[Season] = GoalList
    RecievedGoalsPerTeamPerSeason[Season] = GoalsRecievedList
    MatchesPlayedPerTeamPerSeason[Season] = MatchesList
    DifferenceGoalsPerTeamPerSeason[Season] = DifferenceGoals
    WinsPerTeamPerSeason[Season] = Wins
    DrawsPerTeamPerSeason[Season] = Draws
    LosePerTeamPerSeason[Season] = Loses
    break



DataFrameOfTeams = clean.DictionaryToDataFrame(PointsPerTeamPerSeason)
DataFrameOfMatchesPlayed = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,MatchesPlayedPerTeamPerSeason,"Matches Played")
DataFrameOfNumberOfWins = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,WinsPerTeamPerSeason,"Win")
DataFrameOfNumberOfDraws = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,DrawsPerTeamPerSeason,"Draw")
DataFrameOfNumberOfLoses = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,DrawsPerTeamPerSeason,"Lose")
DataFrameOfGoals =  clean.DictionaryToDataFrameGoals(DataFrameOfTeams,GoalsPerTeamPerSeason,"Goals Scored")
DataFrameOfGoalsRecieved = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,RecievedGoalsPerTeamPerSeason,"Goals Received")
DataFrameOfDifferenceGoals = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,DifferenceGoalsPerTeamPerSeason,"Difference Goals")
DataFrameOfPoints = clean.DictionaryToDataFrameGoals(DataFrameOfTeams,PointsPerTeamPerSeason,"Points")

print(DataFrameOfPoints)








