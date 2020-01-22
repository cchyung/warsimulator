import random

WAR_SIZE = 3
class Game:
    def __init__(self):
        self.player_a = []
        self.player_b = []
        self.deck = [j + 1 for i in range(4) for j in range(13)]
        self.turns = 0
        self.num_wars = 0
        random.shuffle(self.deck)
    
    # deal cards to players
    # deal with wars until a certain amount ends
    def deal_cards(self):
        # todo: random shuffle deck
        turn = 'a'
        for card in self.deck:
            if turn == 'a':
                self.player_a.insert(0, card)
                turn = 'b'            
            else:
                self.player_b.insert(0, card)
                turn = 'a'
                
    def compare_and_exchange(self, player_a_stack = [], player_b_stack = []):
        if(self.player_a and self.player_b):
            # remove top card from each deck (front)
            top_card_a = self.player_a[0]
            top_card_b = self.player_b[0]
            
            self.player_a = self.player_a[1:]
            self.player_b = self.player_b[1:]

            player_a_stack.append(top_card_a)
            player_b_stack.append(top_card_b)

            if(top_card_a != top_card_b):
                if(top_card_a > top_card_b):
                    self.player_a.extend(player_a_stack)
                    self.player_a.extend(player_b_stack)
                else:
                    # append in opposite order for some reason lol
                    self.player_b.extend(player_b_stack)
                    self.player_b.extend(player_a_stack)
            else:
                # war
                self.num_wars += 1

                # add top 3 cards to winnings
                player_a_stack.extend(self.player_a[:min(len(self.player_a), WAR_SIZE)])
                player_b_stack.extend(self.player_b[:min(len(self.player_b), WAR_SIZE)])

                # remove those cards from the deck
                self.player_a = self.player_a[min(len(self.player_a), WAR_SIZE):]
                self.player_b = self.player_b[min(len(self.player_b), WAR_SIZE):]
                self.compare_and_exchange(player_a_stack, player_b_stack)

    def run_game(self):
        self.deal_cards()
        self.turns = 0
        
        while(self.player_a and self.player_b):
            self.turns += 1
            self.compare_and_exchange([], [])
        return self.turns
    

def main():
    with open("results.txt", "w") as f:
        for i in range(10000):
            g = Game()
            f.write("%i\n" % g.run_game())

if __name__ == "__main__":
    main()



