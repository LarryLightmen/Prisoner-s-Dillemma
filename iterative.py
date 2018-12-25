import axelrod as axl
import pprint
import csv
import matplotlib.pyplot as plt

# players = [axl.Cooperator(), axl.Defector(), axl.TitForTat(), axl.Grudger()]
# tournament = axl.Tournament(players)
# results = tournament.play()

players = [axl.Cooperator(), axl.Defector(), axl.TitForTat(), axl.Grudger()]
players.append(axl.Random())
tournament = axl.Tournament(players, repetitions=1000)
results = tournament.play()
summary = results.summarise()

pprint.pprint(summary)
# results.write_summary('summary.csv')

# with open('summary.csv', 'r') as outfile:
#     csvreader = csv.reader(outfile)
#     for row in csvreader:
#         print(row)

# Visualising the results of the tournament
plot = axl.Plot(results)
# p1 = plot.boxplot()
# p1.show()

# Visualising the distributions of wins
# p2 = plot.winplot()
# p2.show()

# Passing various objects to plot
_, ax = plt.subplots()
title = ax.set_title('Payoff')
xlabel = ax.set_xlabel('Strategies')
p3 = plot.boxplot(ax=ax)
p3.show()
