
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for datas in game_state["players"]:
            number = datas["stack"] - datas["bet"]
            for data in datas["hole_cards"]:
                if data[0]["rank"] != data[1]["rank"]:
                    return number
                else:
                    return 0

    def showdown(self, game_state):
        pass

