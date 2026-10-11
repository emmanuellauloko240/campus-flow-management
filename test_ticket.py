import unittest
from ticket import calculate_priority,ticket

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
    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            ticket("T001", "   ", "Hardware", "high", 5)
    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            ticket("T001", "Wi-Fi down", "Banana", "high", 5)

    def test_invalid_urgency_is_rejected(self):
        with self.assertRaises(ValueError):
            ticket("T001", "Wi-Fi down", "Network", "urgent", 5)

    def test_zero_users_is_rejected(self):
        with self.assertRaises(ValueError):
            ticket("T001", "Wi-Fi down", "Network", "high", 0)

    def test_decimal_users_is_rejected(self):
        with self.assertRaises(ValueError):
            ticket("T001", "Wi-Fi down", "Network", "high", 2.5)

    def test_case_is_normalized(self):
        t = ticket("T001", "Wi-Fi down", "network", "HIGH", 5)
        self.assertEqual(t["category"], "Network")
        self.assertEqual(t["urgency"], "high")

if __name__ == "__main__":
    unittest.main()