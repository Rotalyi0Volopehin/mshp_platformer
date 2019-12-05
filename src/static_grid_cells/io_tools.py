import sys


class IO_Tools:
    def sep_slash():
        return '/' if sys.platform == "linux" else '\\'
