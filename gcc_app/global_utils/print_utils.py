import sys


def test_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    print('!!! TEST !!! --- ', *args, sep=sep, end=end, file=file, flush=flush)

