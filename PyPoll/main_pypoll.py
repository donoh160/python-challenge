
import pandas as pd
from pathlib import Path
import os.path


f = open("analysis/election_results.txt", "w")
print("Election Results \n -------------------------", file=f)

poll_data = os.path.join('Resources', 'election_data.csv')
poll_data = pd.read_csv(poll_data)
poll_df = pd.DataFrame(poll_data)

# The total number of votes cast
total_votes = len(poll_df["Ballot ID"])
print(f"Total Votes: {total_votes} \n -------------------------", file=f)

# A complete list of candidates who received votes
can_df = pd.DataFrame(poll_df['Candidate'].value_counts())
# print("can_df", can_df, "\n")
candidates = poll_df["Candidate"].value_counts().index.tolist()
# print("candidates", candidates, "\n")
for i in range(0, len(candidates)):
    vote = can_df.iloc[i, 0]
    print(f"{candidates[i]}: Percentage: {100*vote/total_votes: .2f}% ({vote})", file=f)

print("-------------------------", file=f)

# The winner of the election
# Works since candidates list is sorted from most to least votes
print(f"Winner: {candidates[0]}", file=f)

print("-------------------------", file=f)

f.close()
