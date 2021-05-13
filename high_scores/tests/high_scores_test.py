import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0
class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.highscores = [30, 42, 53, 20, 9, 49, 12]
        self.tie = [12, 20, 20, 18, 19]
        self.lessThanThree = [28, 18]
        self.onlyOneResult = [25]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score_is_53(self):
        self.assertEqual(12, latest(self.highscores))
    # Test personal best (the highest score in the list)
    def test_best_score_in_list_is_53(self):
        self.assertEqual(53, personal_best(self.highscores))
    # Test top three from list of scores
    def test_top_three_results_are_53_49_42(self):
        self.assertEqual([53, 49, 42], personal_top_three(self.highscores))
    # Test ordered from highest tp lowest
    def test_ordered_highest_to_lowest(self):
        self.assertEqual([53, 49, 42, 30, 20, 12, 9], highest_to_lowest(self.highscores))
    # Test top three when there is a tie
    def test_top_three_has_tie(self):
        self.assertEqual([20, 20, 19], personal_top_three(self.tie))
    # Test top three when there are less than three
    def test_top_three_less_than_three_scores(self):
        self.assertEqual([28, 18], personal_top_three(self.lessThanThree))
    # Test top three when there is only one
    def test_top_three_when_only_one_result(self):
        self.assertEqual([25], personal_top_three(self.onlyOneResult))