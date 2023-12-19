class TorrentInfo:
    def __init__(self, save_path, lt):
        self._path = save_path
        self._lt = lt
        self._info = self._lt.torrent_info(save_path)

    def show_info(self):
        print("Torrent Information:")
        print(f"Path: {self._path}")

    def create_torrent_info(self):
        self._info = self._lt.torrent_info(self._path)
        return self._info

    def __str__(self):
        return f"TorrentInfo: Path={self._path}, Info={self._info}"

    def __repr__(self):
        return f"TorrentInfo({self._path}, {self._lt})"
