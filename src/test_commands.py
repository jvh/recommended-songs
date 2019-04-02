import pytest
from src import main


def test_node_creation():
    main.create_song_node('A', 1.1)
    main.create_song_node('B', 3.3)
    main.create_song_node('C', 2.5)
    main.create_song_node('D', 4.7)

    nodeA = main.all_songs['A']
    nodeB = main.all_songs['B']
    nodeC = main.all_songs['C']
    nodeD = main.all_songs['D']

    # Ensuring that only those keys exist
    assert {'A', 'B', 'C', 'D'} == set(main.all_songs.keys())

    # Ensuring node values are correct
    assert nodeA._name == 'A' and nodeA._score == 1.1 and nodeA._connected == []
    assert nodeB._name == 'B' and nodeB._score == 3.3 and nodeB._connected == []
    assert nodeC._name == 'C' and nodeC._score == 2.5 and nodeC._connected == []
    assert nodeD._name == 'D' and nodeD._score == 4.7 and nodeD._connected == []
