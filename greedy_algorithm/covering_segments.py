# Uses python3
import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):

    segments = sorted(segments, key=lambda x: x.end)
    index = 0
    points = []
    while index < len(segments):
        min_end = segments[index].end
        points.append(min_end)

        while index < len(segments) - 1 and min_end in range(segments[index + 1].start, segments[index + 1].end + 1):
            index += 1
    
        index += 1

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
