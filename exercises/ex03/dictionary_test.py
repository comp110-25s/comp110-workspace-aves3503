"""Test function dictionary"""

__author__: str = "730471503"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_one() -> None:
    """Test use case for function invert"""
    usedict: dict[str, str] = {"cat": "meow", "dog": "woof", "horse": "neigh"}
    assert invert(usedict) == {"meow": "cat", "woof": "dog", "neigh": "horse"}


def test_invert_use_two() -> None:
    """Test use case again for function invert"""
    usedict2: dict[str, str] = {"avery": "matthews", "michelle": "visage", "ru": "paul"}
    assert invert(usedict2) == {"matthews": "avery", "visage": "michelle", "paul": "ru"}


def test_invert_edge() -> None:
    """Test edge case for function invert"""
    edgedict3: dict[str, str] = {"ding": "ding", "boom": "boom", "pop": "pop"}
    assert invert(edgedict3) == {"ding": "ding", "boom": "boom", "pop": "pop"}


def test_count_use_one() -> None:
    """Test use case for function count"""
    use_list1: list = ["duck", "duck", "duck", "goose"]
    assert count(use_list1) == {"duck": 3, "goose": 1}


def test_count_use_two() -> None:
    """Test different use case for function count"""
    use_list2: list = ["one", "two", "two", "three", "two"]
    assert count(use_list2) == {"one": 1, "two": 3, "three": 1}


def test_count_edge() -> None:
    """test edge case for function count"""
    edge_list: list = []
    assert count(edge_list) == {}


def test_favorite_colors_use_one() -> None:
    """test use case for favorite colors"""
    fav_colors_use: dict[str, str] = {
        "jewels": "pink",
        "lexi": "purple",
        "onya": "blue",
        "suzie": "blue",
    }
    assert favorite_color(fav_colors_use) == "blue"


def test_favorite_colors_use_two() -> None:
    """Test use case for favorite colors with a tie"""
    fav_colors_use_two: dict[str, str] = {
        "dreamy": "green",
        "avery": "green",
        "sky": "blue",
        "madison": "blue",
    }
    assert favorite_color(fav_colors_use_two) == "green"


def test_favorite_colors_edge() -> None:
    """test edge case for favorite colors"""
    fav_colors_edge: dict[str, str] = {"mama": "", "papa": "blue", "sister": ""}
    assert favorite_color(fav_colors_edge) == ""


def test_bin_len_use() -> None:
    """test use case for bin_len"""
    bin_len_test_use: list = ["snap", "crackle", "pop"]
    assert bin_len(bin_len_test_use) == {4: {"snap"}, 7: {"crackle"}, 3: {"pop"}}


def test_bin_len_use_two() -> None:
    """test use case for bin len again"""
    bin_len_test_use_two: list = ["wee", "wow", "yay", "woohoo"]
    assert bin_len(bin_len_test_use_two) == {3: {"wee", "wow", "yay"}, 6: {"woohoo"}}


def test_bin_len_edge() -> None:
    """test edge case for bin len"""
    bin_len_test_edge: list = []
    assert bin_len(bin_len_test_edge) == {}
