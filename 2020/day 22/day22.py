from collections import deque
from copy import deepcopy

def get_data():
    with open('data.in', 'r') as f:
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
        else:
            #player 2 wins round
            #print('player 2 wins')
            deck2.append(d2c)
            deck2.append(d1c)
        return play_p1(deck1, deck2, r+1)


#print(calculate_score(deck1))
def part_1():
    deck1, deck2 = get_data()
    return play_p1(deck1, deck2, 1)


#True if d1 wins
def play_p2(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        D = (tuple(deck1), tuple(deck2))
        if D in seen:
            return calculate_score(deck1), True
        seen.add(D)
        #if no one has won, conitnue playing
        d1c = deck1.popleft()
        d2c = deck2.popleft()
        if len(deck1) >= int(d1c) and len(deck2) >= int(d2c):
            newd1 = deque(deck1[i] for i in range(int(d1c)))
            newd2 = deque(deck2[i] for i in range(int(d2c)))
            p1_wins = play_p2(deepcopy(newd1), deepcopy(newd2))[1]
        else:
            p1_wins = int(d1c) > int(d2c)
        if p1_wins:
            deck1.append(d1c)
            deck1.append(d2c)
        else:
            deck2.append(d2c)
            deck2.append(d1c)
    if deck1:
        return calculate_score(deck1), True
    else:
        return calculate_score(deck2), False


def part_2():
    deck1, deck2 = get_data()
    winner_score = play_p2(deck1, deck2)[0]
    return winner_score


print(part_1())
print(part_2())

