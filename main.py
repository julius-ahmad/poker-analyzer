import history_handler

if __name__ == '__main__':

    username = 'pastaman4'
    hand_history = '/Users/juliusahmad/Library/Application Support/PokerStarsUK/HandHistory/pastaman4'

    sessions = history_handler.read_history(hand_history)
    history_handler.wins_losses(sessions, username)
