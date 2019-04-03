from src import main


def test_get_song_matches():
    """
    Tests whether or not songs can be directly linked together
    """
    # Creates nodes
    main.create_song_node('A', 1.1)
    main.create_song_node('B', 3.3)
    main.create_song_node('C', 2.5)
    main.create_song_node('D', 4.7)

    # Defines their similarity
    main.define_similarity('A', 'B')
    main.define_similarity('A', 'C')
    main.define_similarity('B', 'D')
    main.define_similarity('C', 'D')

    assert main.get_song_matches('A', 1) == {'D'}
    assert main.get_song_matches('A', 2) == {'D', 'B'}
    assert main.get_song_matches('A', 4) == {'D', 'B', 'C'}
    assert main.get_song_matches('A', 0) == {}
    assert main.get_song_matches('D', 2) == {'C', 'B'}
