# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    nums = []
    for i, ch in enumerate(text):
        if ch in "([{":
            stack.append(ch)
            nums.append(i)
        if ch in ")]}":
            if not stack:
                return(i + 1)
            top = stack.pop()
            _ = nums.pop()
            if not are_matching(top, ch):
                return(i + 1)
    if stack:
        return nums[-1] + 1
    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch >= 0:
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
