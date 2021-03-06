class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []
        self.trick = []
        self.bet = 0
        self.score = 0
        self.round_score = 0

    def set_bet(self,bet):
        self.bet = bet
        print(chr(27) + "[2J")
    
    def reset(self):
        self.trick = []
        self.hand = []
        self.round_score = 0
        self.bet = 0

    def print_hands(self):
        cards_symbol = {"heart" : chr(3), "diamond" : chr(4), "club" : chr(5), "spade" : chr(6)}
        index = 1
        for card in self.hand:
            print(f"{index} : {cards_symbol[card[0]]} {card[1]}")
            index += 1
        print("")

    def __str__(self):
        result = f"Player Id {self.id}\nPlayer Name {self.name}"
        return result

    def calculate_score(self):
        total_trick = len(self.trick)
        if total_trick < self.bet:
            self.round_score = self.bet*-10
        else:
            self.round_score = self.bet*10 + (total_trick - self.bet)
        self.score += self.round_score

    def add_to_trick(self,trick):
        self.trick.append(trick)