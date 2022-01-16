class Song:
    """ Class to represent a song
    
    Attributes:
        title (str): The title of the song.
        artist (str): An artist object representing the songs creator.
        duration (int) : The duration of the song in second. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """
        Songs init method
        :param title: Initialises the 'title attribute
        :param artist: At Artist object representing the song's creator
        :param duration: Initial value for the duration attribute.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album.
        year (int): The year album was released.
        artist: (Artists): The artist responsible for the album.
        Methods:
            add_Song: used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artist"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds song to the track list

        :param song: The title of a song to add
        :param position: If specified, the song will be added to that position.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name 9str): the name of the artist.
        albums (List[Album]): a list of the albums by this artist.
            The list includes only those albums in this collection, it
             is not an exhaustive list of the artist's
    Methos:
        add_album: Use to add a new album to the artist's albums list
        """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.
        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not added again.
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collection of the albums

        This method will add the song to an album in the collection
        A new album will be created in the collection if it doesn't already exixt.

        Args:
            name (str) : the name of the album
            year (int) : teh year the album was published
            title (str) : The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_filed, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_filed, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_filed, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """Create a check flie from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
