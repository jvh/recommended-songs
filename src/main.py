class Song:
    """
    Represents a 'song' as a node
    """
    def __init__(self, name, score):
        """
        Given a song's name and it's metadata score, create node

        :param (str) name: The name of the song
        :param (float) score: The score of the metadata quality
        """
        self._name = name
        self._score = score
        self._connected = []


# Holds all those songs which have been added
all_songs = {}


def create_song_node(song_name, metadata_score):
    """
    Given a song and it's metadata, create a node which represents this

    :param (str) song_name: The name of the song
    :param (float) metadata_score: The score of the metadata quality
    """
    if song_name in all_songs:
        # Update that song listing's metadata score
        song = all_songs[song_name]
        song._score = metadata_score
        return
    all_songs[song_name] = Song(song_name, metadata_score)


def define_similarity(song_a, song_b):
    """
    Defines a relationship between one song and another

    :param (str) song_a: The first song (name)
    :param (str) song_b: The second song
    """
    if song_a not in all_songs:
        return Exception('{} not found in songs to connect. Please ensure that you have added the song '
                         'correctly.'.format(song_a))
    elif song_b not in all_songs:
        return Exception('{} not found in songs to connect. Please ensure that you have added the song '
                         'correctly.'.format(song_b))
    else:
        nodeA = all_songs[song_a]
        nodeB = all_songs[song_b]

        if nodeB in nodeA._connected:
            return Exception("{} and {} are already connected!".format(nodeA, nodeB))

        nodeA._connected.append(nodeB)
        nodeB._connected.append(nodeA)


if __name__ == '__main__':
    print('hello')