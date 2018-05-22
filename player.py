
class Player:
    VERSION = "Can't handle this"

    def betRequest(self, game_state):
        for datas in game_state["players"]:
            number = datas["stack"] - datas["bet"]
            for data in datas["hole_cards"]:
<<<<<<< HEAD
                if data[0]["rank"] != data[1]["rank"]:
                    return number
=======
                if data[0]["rank"] == data[1]["rank"]:
                    return 100
>>>>>>> master
                else:
                    return 0

    def showdown(self, game_state):
        pass

