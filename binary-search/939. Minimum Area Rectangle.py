from collections import defaultdict
import bisect

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Collect all y coordinates per x coordinate into a list (and vice versa).
        x_to_y = defaultdict(list)
        y_to_x = defaultdict(list)
        for x, y in points:
            x_to_y[x].append(y)
            y_to_x[y].append(x)

        # Sort all lists.
        for x, y_list in x_to_y.items():
            y_list.sort()

        for y, x_list in y_to_x.items():
            x_list.sort()

        # For each x1, y1 in points, 
        points = set([tuple(point) for point in points])
        smallest = float('inf')
        for x1, y1 in points:
            # Get all y2 coordinates for this x1 (and vice versa).
            y_list = x_to_y[x1]
            x_list = y_to_x[y1]

            # But only consider the y2 coordinates that are greater than y1.
            # Meaning, lets only consider rectangles from lower left to upper right.
            y_idx = bisect.bisect_right(y_list, y1)
            x_idx = bisect.bisect_right(x_list, x1)
            ys_above = y_list[y_idx:]
            xs_right = x_list[x_idx:]
            for x2 in xs_right:
                for y2 in ys_above:
                    # Here, we know (x1, y2) and (y1, x2) are points because they were 
                    # in x_to_y and y_to_x.  If (x2, y2) is a point, we have a rectangle.
                    if (x2, y2) in points:
                        smallest = min(smallest, (x2 - x1) * (y2 - y1))
                        # Key to efficiency: Because the lists were sorted, we have found
                        # the smallest rectangle for this (x2, y2). Move to next x2.
                        break
                    if smallest <= (x2 - x1) * (y2 - y1):
                        break
        return smallest if smallest != float('inf') else 0