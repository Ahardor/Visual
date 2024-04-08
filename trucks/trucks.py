import math

class Trucks:

    limit = 40
    def spread(self, orders):
        count = math.ceil(orders / self.limit)

        result = [orders // count] * count

        i = 0
        while sum(result) < orders:
            result[i] += 1

            i = (i + 1) % len(result)

        return result