from cricket import Cricket

if __name__ == '__main__':
    print("\n== Welcome to the Cricket Game ==\n")
    
    while True:
        overs = input('How many overs of match (5/10/20)? ')
        try:
            overs = int(overs)
            break
        except:
            print("Invalid number...")
            continue
    print()
    
    player = Cricket(overs=overs)
    while True:
        print("RULE: '1' to Hit and '0' to Quit the Game")
        hit = input("-> Enter (either '1' or '0'): ")
        if hit == "0":
            print('\nClosing...')
            break
        elif hit != "1":
            print("\nEither '1' or '0'...\n")
            continue
        
        my_score = player.scorecard()
        print('\n-------------------------')
        print(f"{my_score}")
        print('-------------------------\n')

        if player.match_over():
            break
    
    player.end_game()