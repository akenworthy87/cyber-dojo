from wordwrap import wordwrap, find_breakpoints
import unittest


class TestFindBreakpoints(unittest.TestCase):
    
    def setUp(self):
        self.test_string = "The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries."
 
    def test_find_breakpoints_returns_correct_positions_width_80(self):
        self.assertEqual([80, 158], find_breakpoints(self.test_string, 80))
    
    def test_find_breakpoints_returns_correct_positions_width_60(self):
        self.assertEqual([53, 113, 173], find_breakpoints(self.test_string, 60))
        
    def test_find_breakpoints_returns_correct_positions_width_40(self):
        self.assertEqual([36, 74, 113, 151], find_breakpoints(self.test_string, 40))
    
    def test_find_breakpoints_returns_correct_positions_width_100(self):
        self.assertEqual([100], find_breakpoints(self.test_string, 100))
    
    def test_find_breakpoints_returns_correct_positions_width_300(self):
        self.assertEqual([], find_breakpoints(self.test_string, 300))


class TestWordwrap(unittest.TestCase):
    
    def setUp(self):
        self.test_string = "The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries."
 
    def test_wordwrap_returns_formatted_string_width_80(self):
        expected_string = (
            "The function returns the string, but with line breaks inserted at just the right\n"
            "places to make sure that no line is longer than the column number. You try to\n"
            "break lines at word boundaries."
        )
        self.assertEqual(expected_string, wordwrap(self.test_string, 80))

    def test_wordwrap_returns_formatted_string_width_60(self):
        expected_string = (
            "The function returns the string, but with line breaks\n"
            "inserted at just the right places to make sure that no line\n"
            "is longer than the column number. You try to break lines at\n"
            "word boundaries."
        )
        self.assertEqual(expected_string, wordwrap(self.test_string, 60))
        
    def test_wordwrap_returns_formatted_string_width_40(self):
        expected_string = (
            "The function returns the string, but\n"
            "with line breaks inserted at just the\n"
            "right places to make sure that no line\n"
            "is longer than the column number. You\n"
            "try to break lines at word boundaries."
        )
        self.assertEqual(expected_string, wordwrap(self.test_string, 40))

    def test_wordwrap_returns_formatted_string_width_100(self):
        expected_string = (
            "The function returns the string, but with line breaks inserted at just the right places to make sure\n"
            "that no line is longer than the column number. You try to break lines at word boundaries."
        )
        self.assertEqual(expected_string, wordwrap(self.test_string, 100))

    def test_wordwrap_returns_formatted_string_width_300(self):
        expected_string = "The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries."
        self.assertEqual(expected_string, wordwrap(self.test_string, 300))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
