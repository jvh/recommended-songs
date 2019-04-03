from collections import deque


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
        self.name = name
        self.score = score
        self.connected = []
        # If the node has been visited, set to True
        self.visited = False


# Holds all those songs which have been added
all_songs = {}


def reset_visited():
    """
    Resets the visited state on all nodes to 0
    """
    for node in all_songs.values():
        node.visited = False


def create_song_node(song_name, metadata_score):
    """
    Given a song and it's metadata, create a node which represents this

    :param (str) song_name: The name of the song
    :param (float) metadata_score: The score of the metadata quality
    """
    if not song_name:
        raise ValueError('ERROR: Ensure that you are calling with a non-empty song name.')
    if metadata_score < 0:
        raise ValueError('ERROR: Please enter a value above 0.')
    # Song already exists, so update metadata score
    if song_name in all_songs:
        song = all_songs[song_name]
        song._score = metadata_score
    else:
        all_songs[song_name] = Song(song_name, metadata_score)


def define_similarity(song_a, song_b):
    """
    Defines a relationship between one song and another

    :param (str) song_a: The first song (name)
    :param (str) song_b: The second song
    """
    if song_a not in all_songs:
        raise Exception('{} not found in songs to connect. Please ensure that you have added the song '
                        'correctly.'.format(song_a))
    elif song_b not in all_songs:
        raise Exception('{} not found in songs to connect. Please ensure that you have added the song '
                        'correctly.'.format(song_b))
    else:
        node_a = all_songs[song_a]
        node_b = all_songs[song_b]

        if node_b in node_a.connected:
            raise Exception("{} and {} are already connected!".format(node_a, node_b))

        node_a.connected.append(node_b)
        node_b.connected.append(node_a)


def get_song_matches(name, number_matches):
    """
    Finds the best song(s) (those with the highest metadata scores) given that they are connected (directly or
     transitively)

    :param (str) name: The name of the song in which we are trying to find similar songs
    :param (int) number_matches: The number of songs which we should return
    :return ({str}): Set of the best song matches (unordered)
    """
    if name not in all_songs:
        return Exception("Song {} doesn't exist. Please ensure that you add this song first.".format(name))
    if number_matches < 0:
        raise ValueError("The number of matches must be at least 0.")
    elif number_matches == 0:
        return {}

    # Holds the metadata_score: [songs] (stack of songs with that score)
    matches = {}
    # Lowest value in matches
    minimum = -1
    root = all_songs[name]
    root.visited = True
    q = deque()
    for n in root.connected:
        n.visited = True
        q.append(n)

    while q:
        node = q.popleft()
        score = node.score
        # Check to see if value is larger than the minimum currently held in matches
        if len(matches) == number_matches:
            # Ignore if score is less than minimum held
            if score > minimum:
                # Replace worst scoring song (or one of the worst)
                matches[minimum].pop()
                if len(matches[minimum]) <= 0:
                    matches.pop(minimum)

                # Add new element
                if score in matches:
                    matches[score].append(node)
                else:
                    matches[score] = [node]

                # Find new minimum
                minimum = float('inf')
                for val in matches.keys():
                    if val < minimum:
                        minimum = val
        else:
            if score < minimum or minimum == -1:
                minimum = score
            if score in matches:
                matches[score].append(node)
            else:
                matches[score] = [node]

        for n in node.connected:
            if not n.visited:
                n.visited = True
                q.append(n)

    reset_visited()

    output = set()
    for lists in matches.values():
        for vals in lists:
            output.add(vals.name)
    return output
