#  dict
class Player:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)
kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
player_kevin = Player(kevin)
print(player_kevin.name)

#  **kwargs
class Player:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
player_kevin = Player(**kevin)
print(player_kevin.name)