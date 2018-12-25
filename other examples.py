
#example 1
# import axelrod as axl
# axl.seed(4)  # for reproducible example
# players = [axl.Cooperator(), axl.Defector(),axl.TitForTat(), axl.Grudger()]
# mp = axl.MoranProcess(players, mutation_rate=0.1)
# for _ in mp:
#      if len(mp.population_distribution()) == 1:
#         break
# print(mp.population_distribution())


# example 2
# import axelrod as axl
# axl.seed(689)
# players = (axl.Cooperator(), axl.Defector(), axl.Defector(), axl.Defector())
# w = 0.95
# fitness_transformation = lambda score: 1 - w + w * score
# mp = axl.MoranProcess(players, turns=10, fitness_transformation=fitness_transformation)
# populations = mp.play()
# print(mp.winning_strategy_name)
