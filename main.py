import pdb
import os
import pandas as pd
import matplotlib.pyplot as plt
def lineChart():
    # pdb.set_trace()
    data = pd.read_csv(os.getcwd() + "\\data\\election_results_senate.csv")
    #Only Albama state because of large data
    Georgia = data[data['state'].str.contains("Alabama")]
    #Filtering out blanks where candidates are not present
    Filtered_candidate = Georgia[Georgia['candidate_name'].notnull()]
    x = Filtered_candidate["cycle"]
    y = Filtered_candidate["votes"]
    plt.title("Election results. Votes in year")

    plt.plot(x, y)
    plt.show() 
lineChart()

def barchart():
    data = pd.read_csv(os.getcwd() + "\\data\\election_results_senate.csv")
    Alabama = data[data['state'].str.contains("Alabama")]
    Filtered_candidate = Alabama[Alabama['candidate_name'].notnull()]
    x = Filtered_candidate["candidate_name"]
    y = Filtered_candidate["votes"]
    plt.title("Election results. Candidate votes")

    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.show()
    # pdb.set_trace()
barchart()

def piechart():
    data = pd.read_csv(os.getcwd() + "\\data\\election_results_senate.csv")
    Alabama = data[data['state'].str.contains("Alabama")]
    Filtered_candidate = Alabama[Alabama['candidate_name'].notnull()]
    y = Filtered_candidate["votes"]
    x = Filtered_candidate["candidate_name"]
    plt.title("Election results. Candidate votes")

    plt.pie(y, labels=x)
    plt.show()
piechart()