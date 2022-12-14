# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def _snail(i: int, j: int, n: int, array: list[list]) -> list:
    if n == 1:
        if array[i]:
            return [array[i][j]]
        else:
            return [] # [[]] case
    elif n == 2:
        return array[i][j:j+n] + array[i+1][j:j+n][::-1]
    else:
        first_row = array[i][j:j + n]
        rightmost_col = [arr[j + n -1] for arr in array[i + 1:i + n -1]]
        last_row_inversed = array[i + n -1][j: j+n][::-1]
        leftmost_col_inversed = [arr[j]
                                 for arr
                                 in array[i + 1:i + n-1][::-1]]
        res = first_row + rightmost_col + last_row_inversed + leftmost_col_inversed
        return res + _snail(i + 1, j + 1, n - 2, array)


def snail(array: list[list]) -> list:
    return _snail(0, 0, len(array), array)
