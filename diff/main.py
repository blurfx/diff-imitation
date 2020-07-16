from typing import List, Tuple

DiffResult = Tuple[int, int, int, str]


def _lcs(old_list: List[str], new_list: List[str]) -> List[List[int]]:
    """
    Find longest common subsequence of given two list of string

    :param old_list: List of original strings to be compared
    :param new_list: List of modified strings to be compared
    :return: len(old_list) X len(new_list) size dynamic programming matrix of lcs
    """
    old_len = len(old_list)
    new_len = len(new_list)

    dp = [[0] * (new_len + 1) for _ in range(old_len + 1)]

    for i in range(1, old_len + 1):
        for j in range(1, new_len + 1):
            if old_list[i - 1] == new_list[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def _backtrack(
    lcs_table: List[List[int]], old_list: List[str], new_list: List[str], i: int, j: int
) -> List[DiffResult]:
    """
    Backtrack changed subsequence using

    :param lcs_table: len(old_list) X len(new_list) sized dynamic programming matrix of lcs
    :param old_list: List of original strings to be compared
    :param new_list: List of modified strings to be compared
    :param i: Index of the old_list element
    :param j: Index of the new_list element
    :return: List of Tuple[flag, old line number, new line number, text] of changed lines.
             if flag is 1, it means text is added.
             if flag is 0, it means text is deleted.
    """
    if i > 0 and j > 0 and old_list[i - 1] == new_list[j - 1]:
        return _backtrack(lcs_table, old_list, new_list, i - 1, j - 1)
    else:
        if j > 0 and (i == 0 or lcs_table[i][j - 1] >= lcs_table[i - 1][j]):
            return _backtrack(lcs_table, old_list, new_list, i, j - 1) + [
                (1, i, j, new_list[j - 1])
            ]
        elif i > 0 and (j == 0 or lcs_table[i][j - 1] < lcs_table[i - 1][j]):
            return _backtrack(lcs_table, old_list, new_list, i - 1, j) + [
                (0, i, j, old_list[i - 1])
            ]
    return []


def diff(old_list: List[str], new_list: List[str]) -> List[DiffResult]:
    """
    Get differences of given two list of strings

    :param old_list: List of original strings to be compared
    :param new_list: List of modified strings to be compared
    :return: List of Tuple[flag, old line number, new line number, text] of changed lines.
             if flag is 1, it means text is added.
             if flag is 0, it means text is deleted.
    """
    lcs_table = _lcs(old_list, new_list)
    old_len = len(old_list)
    new_len = len(new_list)

    return _backtrack(lcs_table, old_list, new_list, old_len, new_len)
