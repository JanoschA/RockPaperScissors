import unittest
from GameRule import GameRule


class TestGameRule(unittest.TestCase):
    def setUp(self):
        self.rule_type = 'rock'
        self.beats = ['scissors']
        self.tie = ['rock']
        self.lose = ['paper', 'fountain']
        self.game_rule = GameRule(self.rule_type, self.beats, self.tie, self.lose)

    def test_init(self):
        self.assertEqual(self.game_rule.rule_type, self.rule_type)
        self.assertEqual(self.game_rule.beats, self.beats)
        self.assertEqual(self.game_rule.tie, self.tie)
        self.assertEqual(self.game_rule.lose, self.lose)

    def test_from_file(self):
        game_rules = GameRule.from_file('gameRules.txt')
        self.assertIsInstance(game_rules, list)
        self.assertIsInstance(game_rules[0], GameRule)

    def test_to_dict(self):
        game_rules = GameRule.from_file('gameRules.txt')
        game_rules_dict = GameRule.to_dict(game_rules)
        print(game_rules_dict)  # Debug line
        self.assertIsInstance(game_rules_dict, dict)
        self.assertEqual(game_rules_dict[self.rule_type], vars(self.game_rule))


if __name__ == '__main__':
    unittest.main()
