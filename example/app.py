import sys
from typing import List

from diff import diff, DiffResult
from formatter import Added, Deleted, Updated


def print_diff(diff_result_list: List[DiffResult]):
    added_items = [item for item in diff_result_list if item[0] == 1]
    deleted_items = [item for item in diff_result_list if item[0] == 0]

    if len(added_items) == len(diff_result_list):
        formatter = Added(added_items)
    elif len(deleted_items) == len(diff_result_list):
        formatter = Deleted(deleted_items)
    else:
        formatter = Updated(added_items, deleted_items)

    print(formatter.get_range())
    print(formatter.format())


def main(first_file_path: str, second_file_path: str):
    with open(first_file_path, "r") as fa:
        with open(second_file_path, "r") as fb:
            first_file_lines = [line.strip() for line in fa.readlines()]
            second_file_lines = [line.strip() for line in fb.readlines()]

            diff_list = diff(first_file_lines, second_file_lines)

            diff_item_list = []
            for flag, old_line_number, new_line_number, text in diff_list:
                if len(diff_item_list) == 0 or (
                    abs(old_line_number - diff_item_list[-1][1]) <= 1
                    and abs(new_line_number - diff_item_list[-1][2]) <= 1
                ):
                    diff_item_list.append(
                        (flag, old_line_number, new_line_number, text)
                    )
                    continue

                print_diff(diff_item_list)
                diff_item_list.clear()
                diff_item_list.append((flag, old_line_number, new_line_number, text))

            if len(diff_item_list) > 0:
                print_diff(diff_item_list)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff [file1] [file2]")
    else:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]
        main(file_path_1, file_path_2)
