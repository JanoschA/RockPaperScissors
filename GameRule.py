import csv


class GameRule:
    def __init__(self, rule_type, beats, tie, lose):
        self.rule_type = rule_type
        self.beats = beats
        self.tie = tie
        self.lose = lose

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter='|')
            headers = next(reader)
            headers = [header.strip() for header in headers if header.strip() and header.strip() != 'x']

            game_rules = []
            for row in reader:
                row = [value.strip() for value in row if value.strip()]
                if not row:
                    continue

                if row[0].startswith('//'):
                    continue

                rule_type = row[0]
                beats = []
                tie = []
                lose = []

                value_to_list = {'W': beats, 'T': tie, 'L': lose}
                for i, value in enumerate(row[1:], start=1):
                    if value in value_to_list:
                        value_to_list[value].append(headers[i - 1])

                game_rules.append(cls(rule_type, beats, tie, lose))

            return game_rules

    @classmethod
    def to_dict(cls, game_rules):
        return {rule.rule_type: vars(rule) for rule in game_rules}
