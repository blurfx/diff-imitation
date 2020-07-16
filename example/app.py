import sys
from diff import diff


def format_print(diff_result_list):
    added_item = [item for item in diff_result_list if item[0] == 1]
    deleted_item = [item for item in diff_result_list if item[0] == 0]

    if len(added_item) == len(diff_result_list):
        diff_range_text = f"{added_item[0][1]}a{added_item[0][2]}"
        if len(added_item) > 1:
            diff_range_text += f",{added_item[-1][2]}"
        print(diff_range_text)

        for item in added_item:
            print(f"> {item[3]}")
    elif len(deleted_item) == len(diff_result_list):
        diff_range_text = f"{deleted_item[0][1]}d{deleted_item[0][2]}"
        if len(deleted_item) > 1:
            diff_range_text += f",{deleted_item[-1][2]}"
        print(diff_range_text)

        for item in deleted_item:
            print(f"< {item[3]}")
    else:
        diff_range_text = f"{deleted_item[0][1]}"
        if len(deleted_item) > 1:
            diff_range_text += f",{deleted_item[-1][1]}"
        diff_range_text += f"c{added_item[0][2]}"
        if len(added_item) > 1:
            diff_range_text += f",{added_item[-1][2]}"
        print(diff_range_text)

        for item in deleted_item:
            print(f"< {item[3]}")
        print("---")
        for item in added_item:
            print(f"> {item[3]}")


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

                format_print(diff_item_list)
                diff_item_list.clear()
                diff_item_list.append((flag, old_line_number, new_line_number, text))

            if len(diff_item_list) > 0:
                format_print(diff_item_list)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff [file1] [file2]")
    else:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]
        main(file_path_1, file_path_2)
