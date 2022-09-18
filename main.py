import history_handler
import analyzer

if __name__ == '__main__':

    username = 'pastaman4'
    hand_history = '/Users/juliusahmad/Library/Application Support/PokerStarsUK/HandHistory/pastaman4'

    sessions = history_handler.read_history(hand_history)
    print(history_handler.wins_losses(sessions, username))
    analyzer = analyzer.Analyzer(username, hand_history)
    print(analyzer.wins_losses())
