from cs2.cs2 import gamestate

class PayloadParser:
    def parse_payload(self, payload, gamestate):
        for item in payload:
            for i in payload[item]:
                try:
                    setattr(getattr(gamestate, item), i, payload[item][i])
                except:
                    pass
