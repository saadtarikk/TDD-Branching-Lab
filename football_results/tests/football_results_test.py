import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    

    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw
    def setUp(self):
        self.final_score1 ={
            "home_score": 1, 
            "away_score": 1
        }
        self.final_score2 ={
            "home_score": 3,
            "away_score": 1
        }
        self.final_score3 ={
            "home_score": 3,
            "away_score": 5
        }


        self.final_scores = [{
            "home_score": 1, 
            "away_score": 1
        },
        {
            "home_score": 3,
            "away_score": 1
        },
        {
            "home_score": 3,
            "away_score": 5
        } 
        ]   
        
    


    # Test we get right list of result strings for a list of final score dictionaries. 

    

    def test_final_score_has_string_result_draw(self):
        self.assertEqual("Draw", get_result(self.final_score1))

    def test_final_score_has_string_result_homewin(self):
        self.assertEqual("Home win", get_result(self.final_score2))

    def test_final_score_has_string_result_Awaywin(self):
        self.assertEqual("Away win", get_result(self.final_score3))

    

    def test_has_a_list_of_final_scores(self):
        self.assertEqual(3, len(get_results(self.final_scores)))

