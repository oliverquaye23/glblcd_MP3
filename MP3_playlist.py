import random


class MP3_playlist:
    # The constructor initialises the music attribute as an empty list to store music related data.
    def __init__(self):
        self.Music = []

    # This method opens a supposed music file in read mode,and loads the tracks into the Music array.
    def load_playlist(self, Music_file):
        try:
            with open(Music_file, "r") as file:
                self.Music = [line.strip() for line in file.readlines()]
            print(f"Loaded {len(self.Music)} tracks from {Music_file}")
        except FileNotFoundError:
            print("File not found.")

    # This method checks the content of the self.Music and if it is not empty it prints its content.
    def display_playlist(self):
        if not self.Music:
            print("playlist is empty.")
        else:
            print("Current PLaylist:")
            for index, track in enumerate(self.Music, start=1):
                print(f"{index}. {track}")

    # This method allows you to add tracks to the playlist by appending whatever track to self.Music.
    def enqueue_track(self, track):
        self.Music.append(track)
        print(f"Added '{track}' to the playlist.")

    def remove_track(self, track):
        if track in self.Music:
            self.Music.remove(track)
            print(f"Removed '{track}' from the playlist.")
        else:
            print(f"'{track}' not found in the playlist.")
    # Opens the supppose file in write mode and stores the tracks in the self.music as a txt file.

    def save_playlist(self, Music_file):
        with open(Music_file, 'w') as file:
            file.write('\n'.join(self.Music))
        print(f"Playlist saved to {Music_file}.")

    def shuffle_playlist(self):
        random.shuffle(self.Music)
        print("Playlist shuffled.")

    def count_tracks(self):
        return len(self.Music)

    def calculate_duration(self):
        # Assume each track is 2 minutes
        track_duration = 2  # in minutes
        total_duration = len(self.Music) * track_duration
        return total_duration

    def clear_playlist(self):
        self.Music = []
        print("Playlist cleared.")

    def is_empty(self):
        return len(self.Music) == 0


# Creating an instance of the MP3_playlist class
playlist = MP3_playlist()
playlist.load_playlist("playlist.txt")
playlist.display_playlist()
playlist.enqueue_track("song 1")
playlist.enqueue_track("song 2")
playlist.enqueue_track("song 3")

playlist.remove_track("song 3")
playlist.display_playlist()
playlist.clear_playlist()
playlist.display_playlist()
