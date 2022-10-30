from collections import OrderedDict


class BookingsHelper:
    def __init__(self, max_intersection):
        if max_intersection < 1:
            raise Exception('Max intersection count should be at least 1')

        self._timeline = OrderedDict()
        self._max_intersection = max_intersection

    def book(self, start, period) -> bool:
        # not inclusive
        end = start + period + 1

        if start not in self._timeline:
            self._timeline[start] = 0

        if end not in self._timeline:
            self._timeline[end] = 0

        self._timeline[start] += 1
        self._timeline[end] -= 1

        max_intersections_met = 0
        current_intersections = 0
        for (key, value) in self._timeline:
            current_intersections += value
            max_intersections_met = max(current_intersections, max_intersections_met)

        if max_intersections_met > self._max_intersection:
            self._timeline[start] -= 1
            self._timeline[end] += 1
            return False

        return True
