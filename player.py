
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for datas in game_state["players"]:
            for data in datas["hole_cards"]:
                if data[0].values() == data[1].values():
                    return 100
                else:
                    return 919

    def showdown(self, game_state):
        pass

