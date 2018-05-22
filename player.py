
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for datas in game_state["players"]:
            for data in datas["hole_cards"]:
                if data[0] == data[1]:
                    return 1000
                else:
                    return 0

    def showdown(self, game_state):
        pass

