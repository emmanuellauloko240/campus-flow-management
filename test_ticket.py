import unittest
from ticket import calculate_priority

class TestPriority(unittest.TestCase):
    def test_low_urgency_2_users_is_low(self):
        answer = calculate_priority("low",2)
        self.assertEqual(answer,"low")
    def test_high_urgency_exactly_10_is_critical(self):
        answer = calculate_priority("high",10)
        self.assertEqual(answer,"critical")
    def test_low_urgency_3_users_is_medium(self):
        answer = calculate_priority("low",3)
        self.assertEqual(answer,"medium")
    def test_medium_urgency_few_users_is_medium(self):
        answer = calculate_priority("medium", 1)
        self.assertEqual(answer, "medium")
    def test_low_urgency_exactly_10_is_high(self):
        answer = calculate_priority("low", 10)
        self.assertEqual(answer,"high")
    def test_low_urgency_12_users(self):
        answer = calculate_priority("low", 12)
        self.assertEqual(answer, "high")
    def test_high_urgency_few_users_is_high(self):
        answer = calculate_priority("high", 4)
        self.assertEqual(answer, "high")

    def test_critical(self):
        answer = calculate_priority("high", 17)
        self.assertEqual(answer, "critical")

if __name__ == "__main__":
    unittest.main()