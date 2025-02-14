import re


def is_haiku(commit_message: str) -> bool:
    """Check if a given text follows the 5-7-5 haiku pattern."""
    lines = commit_message.split('-')
    counts = [count_syllables_in_line(line) for line in lines]
    return counts == [5, 7, 5]


def count_syllables_in_line(line: str) -> int:
    words = line.strip().split(' ')
    return sum([count_syllables(word) for word in words])


def count_syllables(word: str) -> int:
    """Count vowel groups in a word. Remove silent e unless word ends with le"""
    word = word.lower()
    if word.endswith('e') and not word.endswith('le'):
        word = word[:-1]
    syllables = len(re.findall(r'[aeiouy]+', word))
    return max(1, syllables)
