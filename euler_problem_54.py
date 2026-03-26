import requests
import itertools
import requests

# (short) Problem description at: https://projecteuler.net/problem=54

card_value = {'T':9, 'J': 10, 'Q':11, 'K':12, 'A':13}

for i in range(2,10):
    card_value[str(i)] = i - 1

hand_value = {'HighCard': 100, 'OnePair': 200, 'TwoPairs': 300,
    'ThreeKind': 400, 'Straight': 500, 'Flush': 600, 'House': 700,
    'FourKind': 800, 'StraightFlush': 900, 'RoyalFlush': 1000}

# Royal flush - 5 unique, high ace, chain, color | to compare: highest
# Straight flush - 5 unique, chain, color | to compare: highest
# FourKind - 2 unique 4/1 | to compare: four value -> pair value
# House - 2 uniques 3/2 | to compare: three value -> two value
# Flush - color | to compare: highest -> 2nd highest -> ...
# Straight - 5 unique, chain | to compare: highest
# ThreeKind - 3 unqique - 3/1/1 | to compare: three -> highest -> 2nd highest
# Two pairs - 3 unqiues  - 2/2/1 | to compare: -> pair -> pair  -> highest
# One pair - 4 uniques | to compare: pair -> highest -> 2nd highest -> ...

# Sufficient information for precisely identyfing a hand type: 
# 1) Color / No color
# 2) Chain / no chain
# 3) Number of uniques 
# 4) Uniques distribution 


adres = 'https://projecteuler.net/resources/documents/0054_poker.txt'
response = requests.get(adres, stream=True)

rounds = [] 

if response.status_code == 200:
    for line in response.iter_lines(decode_unicode=True):
        a = line.split() 
        first = a[:5]
        second = a[5:]
        first_hand = ([x[0] for x in first],[x[1] for x in first])
        second_hand = ([y[0] for y in second],[y[1] for y in second])
        rounds.append((first_hand, second_hand))
        # Round format: (([][])([][])), (([ <- round/player/hand

# Get the information sufficient for evaluating the result of two hands playing vs each other (out = win / lose)
def check_hand(hand):
    color = False
    chain = False 
    no_uniques = 5
    high_card = 0
    distribution = {}
    distribution_irrelevant_order = None
    
    if len(set(hand[1])) == 1:
        color = True 
        
    vals = sorted([card_value[x] for x in hand[0]])
    if len(set(vals)) == 5 and vals[-1] - vals[0] == 4:
        chain = True
        
    for card in set(hand[0]):
        summa = hand[0].count(card)
        distribution[card] = summa
   
    distribution_sorted = sorted(distribution.items(), key = lambda x: x[1], reverse = True)
    distribution_irrelevant_order = list(itertools.permutations(distribution.values()))
    
    no_uniques = len(distribution)
    high_card = max([card_value[x] for x in hand[0]])

# Each draw is evaluated: prio 1 -> prio 2 -> ... -> highest card -> 2nd highest card -> ... 
# So we define priorities for each hand, and then sorted cards in terms of value from the highest

    if all([color, chain, high_card == 13 ]):
        return 'RoyalFlush', 13
    if all([color, chain, high_card != 13 ]):
        return 'StraightFlush', high_card
    if all([no_uniques == 2, (4,1) in distribution_irrelevant_order]):
        return 'FourKind', distribution_sorted[0][0], distribution_sorted[1][0]
    if all([no_uniques == 2, (3,2) in distribution_irrelevant_order]):
        return 'House', distribution_sorted[0][0], distribution_sorted[1][0]
    if all([color, not chain]):
        return 'Flush', sorted([card_value[x] for x in hand[0]], reverse=True)
    if all([chain, not color]):
        return 'Straight', high_card
    if all([no_uniques == 3, (3,1,1) in distribution_irrelevant_order]):
        return 'ThreeKind', distribution_sorted[0][0], sorted([card_value[x] for x in hand[0]], reverse=True)
    if all([no_uniques == 3, (2,2,1) in distribution_irrelevant_order]):
        return 'TwoPairs', max(card_value[distribution_sorted[0][0]], card_value[distribution_sorted[1][0]]), min(card_value[distribution_sorted[0][0]], card_value[distribution_sorted[1][0]]), distribution_sorted[2][0]
    if all([no_uniques == 4]):
        return 'OnePair', distribution_sorted[0][0], sorted([card_value[x] for x in hand[0]], reverse=True)
    else:
        return 'HighCard', sorted([card_value[x] for x in hand[0]], reverse=True)


player1_won_rounds = 0

# Logic for card comparison  
def compare_hands(hand1_result, hand2_result):
    if hand_value[hand1_result[0]] > hand_value[hand2_result[0]]:
        return 1
    elif hand_value[hand1_result[0]] < hand_value[hand2_result[0]]:
        return 2
    else:
        for i in range(1, len(hand1_result)):
            if i < len(hand2_result):
                val1 = card_value[hand1_result[i]] if isinstance(hand1_result[i], str) else hand1_result[i]
                val2 = card_value[hand2_result[i]] if isinstance(hand2_result[i], str) else hand2_result[i]
                if val1 > val2:
                    return 1
                elif val1 < val2:
                    return 2
        return 0

# Count Player 1 wins 
for r in rounds:
    result_first = check_hand(r[0])
    result_second = check_hand(r[1])
    winner = compare_hands(result_first, result_second)
    if winner == 1:
        player1_won_rounds += 1

print(player1_won_rounds) # Asnwer
