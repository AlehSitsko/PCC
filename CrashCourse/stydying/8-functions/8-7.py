# Album
def make_album(artist_name, album_title, num_tracks=None):
    """Create a dictionary representing a music album."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if num_tracks:
        album['tracks'] = num_tracks
    return album
# Creating album dictionaries
album1 = make_album("pink floyd", "the dark side of the moon")
album2 = make_album("radiohead", "ok computer", 12)
album3 = make_album("beyoncé", "lemonade", 12)
# Displaying the album dictionaries
print(album1)
print(album2)
print(album3)