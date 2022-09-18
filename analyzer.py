import history_handler
MAX_PLAYERS = 9


class Analyzer:

    def __init__(self, username, hand_history_path):
        self.username = username
        self.pathname = hand_history_path

    def wins_losses(self):
        """
        For now, I am just looking at game summaries.
        Seat 1 is always button for zoom only. Can calculate position from there
        :param sessions:
        :param username:
        :return:
        """
        games = history_handler.summarizer(history_handler.read_history(self.pathname))

        positions = {'button': {'won': 0, 'lost': 0}, 'small blind': {'won': 0, 'lost': 0}, 'big blind':
            {'won': 0, 'lost': 0}, 'UTG': {'won': 0, 'lost': 0}, 'UTG+1': {'won': 0, 'lost': 0},
                     'MP': {'won': 0, 'lost': 0}
            , 'MP+1': {'won': 0, 'lost': 0}, 'HJ': {'won': 0, 'lost': 0}, 'CO': {'won': 0, 'lost': 0}}

        for summary in games['summary']:
            players = int(summary[-1][5])
            for line in summary:
                if 'button' in line:
                    button_seat = int(line[5])
            adjusted = {str((button_seat + i - 1) % players + 1): list(positions.keys())[i] for i in range(players)}
            if players < MAX_PLAYERS:
                s = (button_seat + 2) % players
                for pos in list(positions.keys())[-1 * (players - 3):]:
                    adjusted[str(s % players + 1)] = pos
                    s += 1
            for line in summary:
                if self.username in line:
                    if 'collected' in line:
                        positions[adjusted[line[5]]]['won'] += 1
                    else:
                        positions[adjusted[line[5]]]['lost'] += 1

        return positions
