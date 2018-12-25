import axelrod as axl
import matplotlib.pyplot as plt
import random
import pprint


axl.seed(15)  # for reproducible example
players = [axl.Defector(), axl.Defector(), axl.Defector(),axl.Cooperator(), axl.Cooperator(), axl.Cooperator(),axl.TitForTat(), axl.TitForTat(), axl.TitForTat(),axl.Random()]
mp = axl.MoranProcess(players=players, turns=200)
populations = mp.play()
pprint.pprint(populations) 
for row in mp.score_history:
    print([round(element, 1) for element in row])
print("Who wins！！？？")
print(mp.winning_strategy_name)

# ax = mp.populations_plot()
# plt.show()