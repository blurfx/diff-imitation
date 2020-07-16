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
            (0, 1, 0, "aaaaa"),
            (1, 1, 1, "bbbbb"),
        ]
        actual_result = diff(original_list, modified_list)

        assert expected_result == actual_result

    def test_changed_text(self):
        original_list = ["line 1", "line 2"]
        head_modified_list = ["line1", "line 2"]
        tail_modified_list = ["line 1", "line2"]

        expected_result = [
            (0, 1, 0, "line 1"),
            (1, 1, 1, "line1"),
        ]
        actual_result = diff(original_list, head_modified_list)
        assert expected_result == actual_result

        expected_result = [
            (0, 2, 1, "line 2"),
            (1, 2, 2, "line2"),
        ]
        actual_result = diff(original_list, tail_modified_list)
        assert expected_result == actual_result

    def test_deleted_text(self):
        original_list = ["line 1", "line 2"]
        head_modified_list = ["line 2"]
        tail_modified_list = ["line 1"]

        expected_result = [(0, 1, 0, "line 1")]
        actual_result = diff(original_list, head_modified_list)
        assert expected_result == actual_result

        expected_result = [(0, 2, 1, "line 2")]
        actual_result = diff(original_list, tail_modified_list)
        assert expected_result == actual_result

    def test_with_dummy_file(self):
        with open("tests/data_a.txt", "r") as fa:
            with open("tests/data_b.txt", "r") as fb:
                file_a_lines = [line.strip() for line in fa.readlines()]
                file_b_lines = [line.strip() for line in fb.readlines()]

                expected_result = [
                    (0, 1, 0, "Lorem ipsum dolor sit amet"),
                    (0, 3, 1, "Integer at tortor"),
                    (0, 4, 1, "auctor, eleifend magna et,"),
                    (1, 4, 2, "Integer tortor"),
                    (1, 5, 4, ""),
                    (1, 5, 5, "Nullam dapibus libero"),
                ]
                actual_result = diff(file_a_lines, file_b_lines)
                assert expected_result == actual_result
