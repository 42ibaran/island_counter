from src.count_islands import load_file, count_islands

MAP_FILES = [
    ("tests/maps/small0.txt", 0),
    ("tests/maps/small1.txt", 1),
    ("tests/maps/easy.txt", 4),
    ("tests/maps/medium.txt", 120),
    ("tests/maps/large.txt", 3109),
    ("tests/maps/mega.txt", 47334),
]

def test_all_maps():
    for filename, expected_result in MAP_FILES:
        matrix = load_file(filename)
        count = count_islands(matrix)
        assert count == expected_result
