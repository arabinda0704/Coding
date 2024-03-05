# List of players
players = [
    {"name": "MS Dhoni", "age": 25, "sports_type": "Basketball", "team_name": "Bulls"},
    {"name": "Sachin Tendulkar", "age": 28, "sports_type": "Football", "team_name": "Packers"},
    {"name": "Messi", "age": 23, "sports_type": "Soccer", "team_name": "Barcelona"},
    {"name": "Ronaldo", "age": 30, "sports_type": "Tennis", "team_name": "None"},
    {"name": "Virat Kohli", "age": 26, "sports_type": "Golf", "team_name": "None"},
    {"name": "Suresh Raina", "age": 22, "sports_type": "Cricket", "team_name": "CSK"},
    {"name": "Rohit Sharma", "age": 27, "sports_type": "Cricket", "team_name": "Mumbai Indians"},
    {"name": "Mbappe", "age": 29, "sports_type": "football", "team_name": "France"},
    {"name": "Yuvraj Singh", "age": 24, "sports_type": "Rugby", "team_name": "Kings XI Punjab"},
    {"name": "Pele", "age": 32, "sports_type": "Football", "team_name": "Brazil"}
]

# Calculate the total sum of ages
total_age = sum(a["age"] for a in players)
print("total sum age of the players:", total_age)

# Calculate the average age
average_age = total_age / len(players)

print("Average age of the players:", average_age)


players_above_30 = [player for player in players if player["age"] >= 30]

for player in players_above_30:
    print(player["name"])