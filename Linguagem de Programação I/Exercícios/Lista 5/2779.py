N = int(input()) 
M = int(input()) 
purchased_cards = set()  

for _ in range(M):
    card = int(input())  
    purchased_cards.add(card)  

missing_cards = N - len(purchased_cards)  

print(missing_cards)  