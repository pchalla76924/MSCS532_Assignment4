"""
This file implements a binary max-heap priority queue for task scheduling.
Higher priority values are served first.
"""

from dataclasses import dataclass


@dataclass
class Job:
    """
    Represents a scheduled job.

    priority_score:
        Higher number means more urgent.

    deadline:
        Smaller number means the job is due sooner.

    created_at:
        Used as a final tie-breaker when priority and deadline are the same.
    """
    job_code: str
    priority_score: int
    created_at: int
    deadline: int
    note: str = ""

    def __str__(self):
        return (
            f"{self.job_code} | priority={self.priority_score}, "
            f"created={self.created_at}, deadline={self.deadline}, note={self.note}"
        )


class UrgencyQueue:
    """
    Max-heap based priority queue.

    The most urgent job stays at the top of the heap.
    """

    def __init__(self):
        self._items = []
        self._where = {}

    def is_empty(self):
        """
        Checks whether the queue has no jobs.
        Time Complexity: O(1)
        """
        return len(self._items) == 0

    def size(self):
        """
        Returns number of jobs in the queue.
        Time Complexity: O(1)
        """
        return len(self._items)

    def _parent_of(self, index):
        return (index - 1) // 2

    def _left_of(self, index):
        return (2 * index) + 1

    def _right_of(self, index):
        return (2 * index) + 2

    def _comes_before(self, first, second):
        """
        Returns True if first job should be placed above second job.

        Tie-breaking rules:
        1. Higher priority_score wins.
        2. If same priority, earlier deadline wins.
        3. If same deadline, earlier created_at wins.
        """
        if first.priority_score != second.priority_score:
            return first.priority_score > second.priority_score

        if first.deadline != second.deadline:
            return first.deadline < second.deadline

        return first.created_at < second.created_at

    def _exchange(self, i, j):
        """
        Swaps two jobs and updates their index map.
        """
        self._items[i], self._items[j] = self._items[j], self._items[i]

        self._where[self._items[i].job_code] = i
        self._where[self._items[j].job_code] = j

    def _bubble_up(self, index):
        """
        Moves a job upward until the heap is valid.
        Time Complexity: O(log n)
        """
        while index > 0:
            parent = self._parent_of(index)

            if self._comes_before(self._items[index], self._items[parent]):
                self._exchange(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        """
        Moves a job downward until the heap is valid.
        Time Complexity: O(log n)
        """
        while True:
            left = self._left_of(index)
            right = self._right_of(index)
            strongest = index

            if left < len(self._items) and self._comes_before(self._items[left], self._items[strongest]):
                strongest = left

            if right < len(self._items) and self._comes_before(self._items[right], self._items[strongest]):
                strongest = right

            if strongest == index:
                break

            self._exchange(index, strongest)
            index = strongest

    def insert(self, job):
        """
        Inserts a new job into the priority queue.
        Time Complexity: O(log n)
        """
        if job.job_code in self._where:
            raise ValueError(f"Job '{job.job_code}' already exists.")

        self._items.append(job)
        new_position = len(self._items) - 1
        self._where[job.job_code] = new_position

        self._bubble_up(new_position)

    def peek_max(self):
        """
        Returns the most urgent job without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None

        return self._items[0]

    def extract_max(self):
        """
        Removes and returns the most urgent job.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None

        top_job = self._items[0]
        ending_job = self._items.pop()

        del self._where[top_job.job_code]

        if not self.is_empty():
            self._items[0] = ending_job
            self._where[ending_job.job_code] = 0
            self._bubble_down(0)

        return top_job

    def increase_key(self, job_code, new_priority):
        """
        Increases the priority of an existing job.
        Time Complexity: O(log n)
        """
        if job_code not in self._where:
            raise KeyError(f"Job '{job_code}' was not found.")

        index = self._where[job_code]
        current_priority = self._items[index].priority_score

        if new_priority < current_priority:
            raise ValueError("New priority is smaller. Use decrease_key instead.")

        self._items[index].priority_score = new_priority
        self._bubble_up(index)

    def decrease_key(self, job_code, new_priority):
        """
        Decreases the priority of an existing job.
        Time Complexity: O(log n)
        """
        if job_code not in self._where:
            raise KeyError(f"Job '{job_code}' was not found.")

        index = self._where[job_code]
        current_priority = self._items[index].priority_score

        if new_priority > current_priority:
            raise ValueError("New priority is larger. Use increase_key instead.")

        self._items[index].priority_score = new_priority
        self._bubble_down(index)

    def display_heap_order(self):
        """
        Prints the internal heap order.
        This is not sorted order, but it shows heap arrangement.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        for position, job in enumerate(self._items):
            print(f"Index {position}: {job}")


def scheduler_demo():
    """
    Demonstrates a simple priority-based scheduler.
    """
    queue = UrgencyQueue()

    incoming_jobs = [
        Job("JOB-A17", 5, 1, 10, "Prepare weekly status summary"),
        Job("JOB-B22", 9, 2, 4, "Investigate production incident"),
        Job("JOB-C05", 7, 3, 6, "Review code changes"),
        Job("JOB-D31", 3, 4, 12, "Clean old log files"),
        Job("JOB-E14", 7, 5, 5, "Validate database backup"),
        Job("JOB-F09", 9, 6, 3, "Patch urgent service issue")
    ]

    print("Adding jobs into scheduler queue...\n")

    for job in incoming_jobs:
        queue.insert(job)

    print("Heap after insertion:")
    queue.display_heap_order()

    print("\nIncreasing JOB-A17 priority from 5 to 10...\n")
    queue.increase_key("JOB-A17", 10)

    print("Heap after priority change:")
    queue.display_heap_order()

    print("\nExecution order:")
    print("-" * 60)

    step = 1
    while not queue.is_empty():
        next_job = queue.extract_max()
        print(f"Step {step}: {next_job}")
        step += 1


if __name__ == "__main__":
    scheduler_demo()