class TorrentInfo:
    def __init__(self, path, libtorrent):
        self._path = save_path
        self._lt = libtorrent
        self._info = self._lt.torrent_info(self._path)

    def show_info(self):
        # Implement the logic to display torrent information here
        print("Torrent Information:")
        print(f"Path: {self._path}")
        # Add more attributes as needed

    def create_torrent_info(self):
        self._info = self._lt.torrent_info(self._path)
        return self._info
    
    def __str__(self):
        # Implement the logic to return a string representation of the object
        return f"TorrentInfo: Path={self._path}, Info={self._info}"
        
    def __repr__(self):
        # Implement the logic to return a string representation of the object for debugging
        return f"TorrentInfo({self._path}, {self._lt})"

    def call(self):
        return self.create_torrent_info()
