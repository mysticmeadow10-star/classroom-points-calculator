team_a = 45
team_b = 35
last_week_total = 70

total_points = team_a + team_b
average_points = total_points / 2

stars = total_points
boxes_packed = stars // 10
leftover_stars = stars % 10

beat_last_week = total_points > last_week_total

total_points += 5

print("Total Points:", total_points)
print("Average Points:", average_points)
print("Boxes Packed:", boxes_packed)
print("Leftover Stars:", leftover_stars)
print("Higher than last week:", beat_last_week)