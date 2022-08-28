#Ethan Saddler - Text based blackjack game
#imported modules

import random
import time

#function

def card_name(card):
    name = ""
    if card > 109:
        if card < 120:
            name += "The Jack"
        if card > 119 and card < 130:
            name += "The Queen"
        if card > 129 and card < 140:
            name += "The King"
    elif card < 19:
        name += "The Ace"
    else:
        name += "The " + str(card//10)

    if card - (card//10)*10 == 1:
        name += " of Clubs"
    if card - (card//10)*10 == 2:
        name += " of Spades"
    if card - (card//10)*10 == 3:
        name += " of Hearts"
    if card - (card//10)*10 == 4:
        name += " of Diamonds"
    return name

def card_name_value(card):
    name = ""
    if card > 109:
        if card < 120:
            name += "The Jack"
        if card > 119 and card < 130:
            name += "The Queen"
        if card > 129 and card < 140:
            name += "The King"
    elif card < 19:
        name += "The Ace"
    else:
        name += "The " + str(card//10)
    return name

def card_value(card):
    if card < 20:
        total = 11
    elif card < 110:
        total = card//10
    elif card > 110:
        total = 10
    return total


    if card < 20:
        total = 1
    elif card < 110:
        total = card//10
    elif card > 110:
        total = 10
    return total

# def current_score()

#returns whether or not the player has lost. based off of the total points.
def loss(total, hand):
    if total < 22:
        loss = 0 
    else:
        loss = 1
    return loss 

continue_input = "c"
pass1 = 0
house_score = 0
player_score = 0

#main

#opening of game
while pass1 < 1:
    ready_query = input("are you ready? (yes/no) \n")
    if ready_query == "yes" or ready_query == "y":
        pass1 = 1
    elif ready_query == "no" or ready_query == "n":
        print("ok, take a few seconds to prepare")
        time.sleep(3)
    else:
        print("I cannot understand that. Please try again.\n\n")
        time.sleep(1)


while continue_input == "continue" or continue_input == "c":
    
    deck = []
    value = []
    suit = []
    player_hand = []
    house_hand = []
    player_hand_value_str = []
    house_hand_value_str = []
    player_hand_suit_str = []
    house_hand_suit_str = []
    player_total = 0
    house_total = 0 

    #creating the deck
    value.extend(range(10, 140, 10))
    suit.extend(range(1,5))

    for x in value:
        for y in suit:
            deck.extend([x + y])
    random.shuffle(deck)

    print("\n")

    time.sleep(1)

    print("\nOkay, hands are being dealt!\n\n")

    time.sleep(1)

    player_hand.append(deck[0])
    player_hand.append(deck[1])
    house_hand.append(deck[-1])
    house_hand.append(deck[-2])

    #print hands
    print("The House's Hand is...\n")
    print(card_name(house_hand[0]))

    time.sleep(1)

    print("\nYour Hand is...\n")
    print(card_name(player_hand[0]))
    print("and")
    print(card_name(player_hand[1]))

    player_hand_suit_str.append(card_name_value(player_hand[0]))
    player_hand_suit_str.append(card_name_value(player_hand[1]))
    house_hand_suit_str.append(card_name_value(house_hand[0]))
    house_hand_suit_str.append(card_name_value(house_hand[1]))

    player_total = card_value(player_hand[0]) + card_value(player_hand[1])

    #player turn
    pass1 = 0
    g = 2
    ace_count_player = player_hand_suit_str.count("The Ace")
    round_player_status = 0
    while round_player_status == 0:
        while pass1 == 0:
            turn = input("\nWould you like to hit or stay? \n")
            if turn == "hit" or turn == "h":
                player_hand.append(deck[g])
                g = g + 1
                player_total += card_value(player_hand[-1])
                player_hand_suit_str.append(card_name_value(player_hand[-1]))
                print("\nDrawing...")
                time.sleep(1)
                print("\nYou got:\n")
                print(card_name(player_hand[-1]))
                ace_count_player = player_hand_suit_str.count("The Ace")
                if loss(player_total, player_hand) == 0:
                    pass
                else:
                    if ace_count_player == 0:
                        print("\nYou busted!")
                        round_player_status = 1
                        pass1 = 1
                    elif ace_count_player == 1:
                        player_total -= 10
                        ace_count_player = 0
                    elif ace_count_player == 2:
                        player_total -= 10
                        ace_count_player = 1
                    elif ace_count_player == 3:
                        player_total -= 10
                        ace_count_player = 2
                    elif ace_count_player == 4: 
                        player_total -= 10 
                        ace_count_player = 3
                    else:
                        print("\nYou busted!")
                        round_player_status = 1
                        pass1 = 1
            elif turn == "stay" or turn == "s":
                round_player_status = 1
                pass1 = 1
            else:
                print("I cannot understand that. Please try again.")

    #house turn
    f = -1
    ace_count_house = house_hand_suit_str.count("The Ace")
    house_total = card_value(house_hand[0]) + card_value(house_hand[1])
    time.sleep(1)
    print("\nThe House's Second Card is {}".format(card_name(house_hand[1])))
    time.sleep(1)
    round_house_status = 0
    while round_house_status == 0:
        time.sleep(1)
        if house_total <= 16:
            house_hand.append(deck[f])
            f = f - 1
            house_total += card_value(house_hand[-1])
            house_hand_suit_str.append(card_name_value(house_hand[-1]))
            print("\nThe House hits")
            time.sleep(0.5)
            print("\nDrawing...")
            time.sleep(1)
            print("\nThe House got:\n")
            print(card_name(house_hand[-1]))
            ace_count_house = house_hand_suit_str.count("The Ace")
            if loss(house_total, house_hand) == 0:
                pass
            else:
                if ace_count_house == 0:
                    print("\nThe House busted!")
                    round_house_status = 1
                elif ace_count_house == 1:
                    house_total -= 10
                    ace_count_house = 0
                elif ace_count_house == 2:
                    house_total -= 10
                    ace_count_house = 1
                elif ace_count_house == 3:
                    house_total -= 10
                    ace_count_house = 2
                elif ace_count_house == 4: 
                    house_total -= 10 
                    ace_count_house = 3
                else:
                    print("\nThe House busted!")
                    round_house_status = 1
        else:
            print("\nThe House stands.")
            round_house_status = 1

    #finding the winner
    if player_total > 21:
        if house_total > 21:
            print("\nIt is a tie!")
        else:
            print("\nThe House Wins!")
            house_score += 1 
    elif house_total > 21:
        print("\nYou Win!")
    else:
        if player_total > house_total:
            print("\nYou Win!")
            player_score += 1
        elif player_total < house_total:
            print("\nThe House Wins!")
            house_score += 1
        else:
            print("It is a tie!")

    time.sleep(2)
    print("\n")
    pass1 = 0
    while pass1 == 0:
        continue_input = input("Do you want to continue or quit? \n")
        if continue_input == "q" or continue_input == "quit":
            print("The final score is...\n")
            print("House: {}".format(house_score))
            time.sleep(0.2)
            print("Player: {}".format(player_score))
            if house_score > player_score:
                print("\nThe House Wins!")
            elif player_score > house_score:
                print("\nYou Win!")
            else:
                print("\nIt is a tie!")
            pass1 = 1 
        elif continue_input == "continue" or continue_input == "c":
            print("The current score is...\n")
            print("House: {}".format(house_score))
            time.sleep(0.2)
            print("Player: {}\n".format(player_score))
            pass1 = 1
        else:
            print("I cannot understand that. Please try again.")
