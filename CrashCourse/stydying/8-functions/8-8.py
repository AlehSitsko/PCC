# User album creation
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
# Interactive album creation
while True:
    print("\nEnter album details (or type 'q' to quit):")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    tracks_input = input("Number of tracks (press enter to skip): ")
    if tracks_input.lower() == 'q':
        break
    num_tracks = int(tracks_input) if tracks_input else None
    new_album = make_album(artist, title, num_tracks)
    print(f"\nCreated album: {new_album}")
