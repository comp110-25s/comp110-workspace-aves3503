"""doc string"""

__author__: str = "730471503"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Swap keys with their values"""
    swapped_dict: dict[str, str] = {}
    new_key: str = ""
    for key in input:
        print(key, "", input[key])
        new_key = input[key]
        if new_key in swapped_dict:
            errstr: str = "Key duplicate found in dictionary:" + new_key
            raise KeyError(errstr)
        else:
            swapped_dict[new_key] = key
    return swapped_dict


def count(initial_list: list[str]) -> dict[str, int]:
    """Count number of times a value appears in given list"""
    count_keys: dict[str, int] = {}
    key: str = ""
    idx: int = 0
    while idx < len(initial_list):
        key = initial_list[idx]
        if key in count_keys:
            count_keys[key] += 1
        else:
            count_keys[key] = 1
        idx += 1
    return count_keys


def favorite_color(colors: dict[str, str]) -> str:
    """Determine most popular favorite color of a group"""
    fav_colors: list[str] = []
    current_fav: str = ""
    for key in colors:
        fav_colors.append(colors[key])
    color_count: dict[str, int] = count(initial_list=fav_colors)
    current_fav = fav_colors[0]
    for key in color_count:
        if color_count[current_fav] <= color_count[key]:
            current_fav = key
    return current_fav


def bin_len(input_words: list[str]) -> dict[int, set[str]]:
    """Sort words by length"""
    idx: int = 0
    word_sort: dict[int, set[str]] = {}
    temp_set: set[str] = set()
    while idx < len(input_words):
        if len(input_words[idx]) in word_sort:
            temp_set = word_sort[len(input_words[idx])]
            temp_set.add(input_words[idx])
            word_sort[len(input_words[idx])] = temp_set
        else:
            temp_set = {input_words[idx]}
            word_sort[len(input_words[idx])] = temp_set
        idx += 1
    return word_sort
