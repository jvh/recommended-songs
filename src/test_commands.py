from src import main


def create_nodes():
    """
    Creates some nodes
    """
    main.create_song_node('A', 1.1)
    main.create_song_node('B', 3.3)
    main.create_song_node('C', 2.5)
    main.create_song_node('D', 4.7)

    nodeA = main.all_songs['A']
    nodeB = main.all_songs['B']
    nodeC = main.all_songs['C']
    nodeD = main.all_songs['D']

    return nodeA, nodeB, nodeC, nodeD


class TestMain:

    def test_node_creation(self):
        """
        Tests that song nodes are created properly
        """
        nodeA, nodeB, nodeC, nodeD = create_nodes()

        # Ensuring that only those keys exist
        assert {'A', 'B', 'C', 'D'} == set(main.all_songs.keys())

        # Ensuring node values are correct
        assert nodeA._name == 'A' and nodeA._score == 1.1 and nodeA._connected == []
        assert nodeB._name == 'B' and nodeB._score == 3.3 and nodeB._connected == []
        assert nodeC._name == 'C' and nodeC._score == 2.5 and nodeC._connected == []
        assert nodeD._name == 'D' and nodeD._score == 4.7 and nodeD._connected == []


    def test_node_updating(self):
        """
        Nodes should have the ability to change the value of the metadata (given a song name which already exists)
        """
        create_nodes()

        song_to_test = main.all_songs['A']
        song_to_test._connected.append('testing')

        # Instead of creating a new node, it should just alter the metadata score
        main.create_song_node('A', 5.82)

        assert song_to_test._name == 'A' and song_to_test._score == 5.82 and song_to_test._connected == ['testing']


    def test_defining_similarity(self):
        """
        Tests whether or not songs can be directly linked together
        """
        create_nodes()

        songA = main.all_songs['A']
        songB = main.all_songs['B']

        songA._connected.append('testing')
        main.define_similarity('A', 'B')

        assert set(songA._connected) == {'testing', songB}
        assert songB._connected == [songA]







