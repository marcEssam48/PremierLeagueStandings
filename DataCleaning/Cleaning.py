import pandas as pd

path = "//DataSet/final_dataset.xlsx"
DataFrame = pd.read_excel(path,sheet_name="premierleague")
counter = 0
for index,row in DataFrame.iterrows():
    if str(row["MW"]).strip() == "38":
        counter+=1

counter = int(counter/10)
# print(counter)
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
print(DataFrame["Season"])
# print(len(Season_list))

