import glob
import os
MAX_PLAYERS = 9


def read_history(pathname):
    """
    Reads hand histories and stores each session into a list.
    :param pathname: directory path of where your hand histories are stored
    :return: List of lists each a session played. Each session broken line by line
    """

    sessions = []
    ses_files = glob.glob(r'' + pathname + '/*.txt')

    for ses in ses_files:
        with open(os.path.join(pathname, ses)) as f:
            sessions.append(f.readlines())  # This will make txt be a list of lists with each list being each session
        f.close()
    return sessions


def summarizer(sessions):
    games = {'summary': [], 'cards': []}

    for ses in sessions:
        for i in range(0, len(ses)):
            if ses[i] == '*** SUMMARY ***\n':
                game = []
                j = i
                while ses[j] != '\n':
                    game.append(ses[j][:-1])
                    j += 1
                games['summary'].append(game)
            elif ses[i] == '*** HOLE CARDS ***\n':
                games['cards'].append(ses[i + 1][-8:-1])

    return games


def wins_losses(sessions, username):
    """
    For now, I am just looking at game summaries.
    Seat 1 is always button for zoom only. Can calculate position from there
    :return:
    """
    games = summarizer(sessions)

    positions = {'button': {'won': 0, 'lost': 0}, 'small blind': {'won': 0, 'lost': 0}, 'big blind':
        {'won': 0, 'lost': 0}, 'UTG': {'won': 0, 'lost': 0}, 'UTG+1': {'won': 0, 'lost': 0}, 'MP': {'won': 0, 'lost': 0}
        , 'MP+1': {'won': 0, 'lost': 0}, 'HJ': {'won': 0, 'lost': 0}, 'CO': {'won': 0, 'lost': 0}}

    for summary in games['summary']:
        players = int(summary[-1][5])
        for line in summary:
            if 'button' in line:
                button_seat = int(line[5])
        adjusted = {str((button_seat + i - 1) % players + 1): list(positions.keys())[i] for i in range(players)}
        if players < MAX_PLAYERS:
            s = (button_seat + 2) % players
            for pos in list(positions.keys())[-1 * (players-3):]:
                adjusted[str(s % players + 1)] = pos
                s += 1
        for line in summary:
            if username in line:
                if 'collected' in line:
                    positions[adjusted[line[5]]]['won'] += 1
                else:
                    positions[adjusted[line[5]]]['lost'] += 1

    print(positions)

