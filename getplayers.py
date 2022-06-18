import json

from sleeper_wrapper import League, User, Stats, Players

players = Players()
print('fetching all players')
all_players = players.get_all_players()
print('writing to players file')

with open('./data/players.json', 'w') as fp:
    json.dump(all_players, fp)

print('done')