
class Player:
    VERSION = "Can't handle this"

    def betRequest(self, game_state):
        for datas in game_state["players"]:
            for data in datas["hole_cards"]:
                number = data["stack"] - data["bet"]
                if data[0]["rank"] != data[1]["rank"]:
                    return number
                else:
                    return 0

    def showdown(self, game_state):
        pass

