# torrent_info.py

class TorrentInfo:
    def __init__(self, save_path, lt):
        self._path = save_path
        self._lt = lt
        self._info = self._lt.torrent_info(save_path)

    def show_info(self):
        print("Torrent Information:")
        print(f"Path: {self._path}")
        print(f"Info: {self._info}")

# Example usage
if __name__ == "__main__":
    # Assuming lt is an instance of a Torrent object
    lt = Torrent()  # Create or obtain the Torrent object
    save_path = "path/to/torrent/file.torrent"
    torrent = TorrentInfo(save_path, lt)
    torrent.show_info()
