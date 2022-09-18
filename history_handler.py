import glob
import os


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

