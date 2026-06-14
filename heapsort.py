import random
import time


class HeapSorter:
    """
    A small class that performs Heap Sort using max-heap logic.
    """

    def __init__(self, numbers):
        self.data = numbers[:]

    def _push_down(self, root_index, active_size):
        """
        Moves the value at root_index down until the max-heap rule is restored.
        """
        current = root_index

        while True:
            left = (2 * current) + 1
            right = left + 1
            bigger = current

            if left < active_size and self.data[left] > self.data[bigger]:
                bigger = left

            if right < active_size and self.data[right] > self.data[bigger]:
                bigger = right

            if bigger == current:
                break

            self.data[current], self.data[bigger] = self.data[bigger], self.data[current]
            current = bigger

    def _create_max_heap(self):
        """
        Converts the list into a max-heap.
        """
        last_parent = (len(self.data) // 2) - 1

        for index in range(last_parent, -1, -1):
            self._push_down(index, len(self.data))

    def sort(self):
        """
        Returns the sorted list in ascending order.
        """
        self._create_max_heap()

        for last_index in range(len(self.data) - 1, 0, -1):
            self.data[0], self.data[last_index] = self.data[last_index], self.data[0]
            self._push_down(0, last_index)

        return self.data


def heap_sort(numbers):
    sorter = HeapSorter(numbers)
    return sorter.sort()


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    center = len(numbers) // 2
    left_side = merge_sort(numbers[:center])
    right_side = merge_sort(numbers[center:])

    result = []
    i, j = 0, 0

    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            result.append(left_side[i])
            i += 1
        else:
            result.append(right_side[j])
            j += 1

    result.extend(left_side[i:])
    result.extend(right_side[j:])

    return result


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[len(numbers) // 2]

    lower, equal, higher = [], [], []

    for value in numbers:
        if value < pivot:
            lower.append(value)
        elif value > pivot:
            higher.append(value)
        else:
            equal.append(value)

    return quick_sort(lower) + equal + quick_sort(higher)


def make_dataset(size, style):
    if style == "sorted":
        return list(range(size))

    if style == "reverse":
        return list(range(size, 0, -1))

    if style == "random":
        return [random.randint(1, size * 10) for _ in range(size)]

    raise ValueError("Invalid dataset style.")


def clock_algorithm(sort_method, values):
    start = time.perf_counter()
    output = sort_method(values)
    end = time.perf_counter()

    if output != sorted(values):
        raise ValueError(f"{sort_method.__name__} failed sorting validation.")

    return end - start


def compare_sorts():
    sizes = [100, 1000, 3000]
    patterns = ["sorted", "reverse", "random"]

    methods = {
        "Heap Sort": heap_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    print("\nSorting Runtime Comparison")
    print("=" * 70)
    print(f"{'Size':<10}{'Pattern':<12}{'Algorithm':<15}{'Seconds':<12}")
    print("=" * 70)

    for size in sizes:
        for pattern in patterns:
            sample = make_dataset(size, pattern)

            for name, method in methods.items():
                runtime = clock_algorithm(method, sample)
                print(f"{size:<10}{pattern:<12}{name:<15}{runtime:<12.6f}")

    print("=" * 70)


if __name__ == "__main__":
    sample_numbers = [31, 4, 71, 9, 18, 52, 6, 40]

    print("Original:", sample_numbers)
    print("Heap Sorted:", heap_sort(sample_numbers))

    compare_sorts()