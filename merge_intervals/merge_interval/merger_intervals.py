# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
#
# Example 1:
#
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5].
from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


def merge_interval(intervals):
    if len(intervals) < 2:
        return intervals

    merged = []
    intervals = sorted(intervals, key=lambda ele: ele.start)
    start = intervals[0].start
    end = intervals[0].end
    for interval in intervals:
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged


def main():
    for i in merge_interval([Interval(2, 5), Interval(1, 4), Interval(7, 9)]):
        print(i)


if __name__ == "__main__":
    main()
