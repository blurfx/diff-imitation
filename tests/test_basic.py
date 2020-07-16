import unittest
from diff import diff


class BasicTest(unittest.TestCase):
    def test_same_text(self):
        original_list = ["aaaaa"]
        modified_list = ["aaaaa"]

        expected_result = []
        actual_result = diff(original_list, modified_list)

        assert expected_result == actual_result

    def test_single_line_diff(self):
        original_list = ["aaaaa"]
        modified_list = ["bbbbb"]

        expected_result = [
            (-1, "aaaaa"),
            (1, "bbbbb"),
        ]
        actual_result = diff(original_list, modified_list)

        assert expected_result == actual_result
