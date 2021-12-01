from collections import deque

def get_data():
    with open('test.in', 'r') as f:
        L = [l.strip() for l in f]
    deck1 = deque(L[1:L.index('')])
    deck2 = deque(L[L.index('')+2:])
    #top card = at leftmost index
    return deck1, deck2

def calculate_score(d):
    score = [(n+1)*int(i) for n, i in enumerate(reversed(d))]
    return sum(score)


def play_p1(deck1, deck2, r):
    #print(f'round {r}')
    #print(f'player 1s deck {deck1}')
    #print(f'player 2s deck {deck2}')
    if len(deck2) == 0:
        #if deck 1 has won
        score = calculate_score(deck1)
        return score
    elif len(deck1) == 0:
        #deck 2 has won
        score = calculate_score(deck2)
        return score 
    else:
        #if no one has won, conitnue playing
        d1c = deck1.popleft()
        d2c = deck2.popleft()
        #print(f'player 1 plays {d1c}')
        #print(f'player 2 plays {d2c}')
        if int(d1c) > int(d2c):
            #player 1 wins round
            #players card appended before opponents
            deck1.append(d1c)
            deck1.append(d2c)
            #print('player 1 wins')
        elif int(d2c) > int(d1c):
            #player 2 wins round
            #print('player 2 wins')
            deck2.append(d2c)
            deck2.append(d1c)
        else:#both cards have same value
            raise ValueError
        return play_p1(deck1, deck2, r+1)

#print(calculate_score(deck1))
def part_1():
    deck1, deck2 = get_data()
    return play(deck1, deck2, 1)

def play_p2(prev, deck1, deck2):
    #Before either player deals a card, if there was a previous round in this 
    #game that had exactly the same cards in the same order in the same players'
    #decks, the game instantly ends in a win for player 1.
    print(deck1, deck2)
    if len(prev) != 0:
        for i in prev:
            if i[0] == deck1 and i[1] == deck2:
                score = calculate_score(deck1)
                return score, 'd1'
    # the players begin the round by each drawing the top card of their deck as normal.
    d1c = int(deck1.popleft())
    d2c = int(deck2.popleft())
    # If both players have at least as many cards remaining in their deck as the
    #value of the card they just drew, the winner of the round is determined by playing
    #a new game of Recursive Combat
    
    #To play a sub-game of Recursive Combat, each player creates a new deck by 
    #making a copy of the next cards in their deck (the quantity of cards copied is 
    #equal to the number on the card they drew to trigger the sub-game)
    if len(deck1) >= d1c and len(deck2) >= d2c:
        nd1 = copy(deck1[:d1c+1]) #if index error, make d1c and d2c not +1
        nd2 = copy(deck2[:d2c+1])
        winner = play_p2([], nd1, nd2)[1]
        if winner == 'd1':
            deck1.append(d1c)
            deck1.append(d2c)
        elif winner == 'd2':
            deck2.append(d2c)
            deck2.append(d1c)

    else:    
        if len(deck2) == 0:
            #if deck 1 has won
            score = calculate_score(deck1)
            return score, 'd1'
        elif len(deck1) == 0:
            #deck 2 has won
            score = calculate_score(deck2)
            return score, 'd2'
        else:
            #Otherwise, the winner of the round is the player with the higher-value card.
            if int(d1c) > int(d2c):
                #player 1 wins round
                #players card appended before opponents
                deck1.append(d1c)
                deck1.append(d2c)
                #print('player 1 wins')
            elif int(d2c) > int(d1c):
                #player 2 wins round
                #print('player 2 wins')
                deck2.append(d2c)
                deck2.append(d1c)
            else:#both cards have same value
                raise ValueError
            decks = (deck1, deck2)
            prev.append(decks)
            return play_p2(prev, deck1, deck2)

deck1, deck2 = get_data()
print(play_p2([], deck1, deck2))

#9353 too low
