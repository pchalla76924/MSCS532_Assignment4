# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications


## Abstract

This report discusses the implementation, analysis, and application of heap data structures using Python. The assignment focuses on two main parts: Heapsort and a priority queue scheduler. The Heapsort implementation uses a custom class named `HeapSorter`, which builds a max-heap and then sorts the input list in ascending order. The priority queue implementation uses a custom binary max-heap named `UrgencyQueue`, along with a `Job` class to represent scheduled tasks. The project also compares Heapsort with Merge Sort and Quicksort using sorted, reverse-sorted, and random input data. The results show that Heapsort maintains predictable `O(n log n)` performance across different input distributions. The priority queue portion demonstrates how heaps can be used in real-world scheduling systems where the most urgent job should be processed first. Overall, this project shows that heap data structures are efficient, practical, and useful for both sorting and priority-based task management.

-
## Introduction

A heap is a specialized tree-based data structure that is usually implemented using an array or list. Even though heaps are often explained as binary trees, they do not require separate tree node objects in code. Instead, parent and child positions can be calculated directly from indexes. In a zero-based list, the left child of an element at index `i` is located at `2i + 1`, the right child is located at `2i + 2`, and the parent is located at `(i - 1) // 2`. This makes heaps simple to store and efficient to manipulate.

This assignment focuses on two common applications of heaps. The first application is Heapsort, which uses a max-heap to sort values. The second application is a priority queue, which uses a heap to always access the highest-priority item first. Priority queues are important in real systems such as operating system scheduling, emergency task handling, simulation systems, network processing, and pathfinding algorithms.

For this project, I implemented the heap logic manually instead of depending on Python’s built-in heap library. This helped me understand how heap operations actually work internally. The implementation includes building a heap, pushing values down, inserting jobs, extracting the highest-priority job, and updating priorities. According to Miller and Ranum (2025), binary heaps are commonly used for priority queues because they allow efficient enqueue and dequeue behavior while still being represented with a simple list structure. Similarly, Microsoft Learn (2026) explains that a heap can be maintained in an array-like structure where parent and child relationships are based on index positions.



## Heapsort Implementation Design

The Heapsort implementation is stored in the file `heap_sort_lab.py`. The main class used in this file is `HeapSorter`. I chose a class-based design because it keeps the sorting data and heap operations grouped together in one place. This makes the code easier to read, test, and explain.

The main parts of the `HeapSorter` class are:

- `__init__(self, numbers)`
- `_push_down(self, root_index, active_size)`
- `_create_max_heap(self)`
- `sort(self)`

The `__init__` method receives the original list and creates a copy of it. I made this design choice so the original input list is not changed. This is helpful during testing because the same input list can be reused for different sorting algorithms.

The `_push_down` method is responsible for restoring the max-heap property. In a max-heap, the parent value should be greater than or equal to its child values. If one of the child values is larger than the parent, the method swaps the parent with the larger child. This continues until the value reaches a correct position or has no larger child below it.

The `_create_max_heap` method converts the list into a max-heap. It starts from the last parent node and moves backward toward the root. Each parent node is checked and pushed downward if needed. After this process, the largest value in the list is located at the root position, which is index `0`.

The `sort` method performs the final Heapsort process. First, it builds a max-heap. Then it repeatedly swaps the root value with the last value in the active heap area. After each swap, the active heap size is reduced by one, and `_push_down` is called again to restore the heap property. This process continues until the list is fully sorted.

This implementation is unique because it uses a custom class named `HeapSorter` instead of only writing one standalone function. The method names are also written in a simple way so the program is easier to follow. The implementation avoids using built-in sorting functions for the actual algorithm, which makes it suitable for demonstrating the heap logic required in this assignment.

---

## Heapsort Algorithm Steps

The Heapsort process used in this project follows these steps:

1. Copy the original list so the input is not directly modified.
2. Build a max-heap from the copied list.
3. Swap the largest value at the root with the last value in the active heap.
4. Reduce the active heap size by one.
5. Restore the heap property by pushing the new root downward.
6. Repeat the process until only one item remains in the active heap.

For example, if the input list is:

```text
[31, 4, 71, 9, 18, 52, 6, 40]


The algorithm first rearranges the values into a max-heap. Then the largest value is moved to the end of the list. After all extraction steps are completed, the final sorted output is:

[4, 6, 9, 18, 31, 40, 52, 71]
```

This step-by-step process shows why Heapsort is predictable. It does not rely on the original order of the list in the same way some other sorting algorithms do. Whether the list is already sorted, reverse sorted, or random, Heapsort still builds a heap and repeatedly extracts the maximum value.

Time Complexity Analysis of Heapsort
Heapsort has two main phases: heap construction and repeated extraction.

The heap construction phase takes O(n) time. At first, it may seem like building the heap should take O(n log n) because a push-down operation can take O(log n) time. However, not every node moves down the full height of the heap. Many nodes are already near the bottom and require little or no movement. Because of this, the total work for building the heap is O(n).

The extraction phase takes O(n log n) time. After the max-heap is built, the algorithm removes the largest element one at a time. There are approximately n removals, and each removal may require a push-down operation. Since the height of a binary heap is O(log n), each push-down operation takes O(log n) time in the worst case.

The total time complexity can be written as:

```
O(n) + O(n log n) = O(n log n)
Therefore, the overall time complexity of Heapsort is:
O(n log n)
```
This complexity applies in the best case, average case, and worst case. Even if the input is already sorted, the algorithm still builds a heap and performs the extraction process. This is why Heapsort does not improve to O(n) for already sorted input.
The PowerPoint material used for this assignment also explains that Heapsort has O(n log n) running time and uses a heap-building phase followed by repeated extraction of the largest element (BITS Pilani WILP Division, 2026).

Space Complexity of Heapsort
In theory, Heapsort can be implemented with O(1) additional space because it can sort the list in place. However, my implementation creates a copy of the original list before sorting. I made this choice to protect the original input from being changed.

Because of this copy, my version uses:
``
O(n)
``


If the copy were removed, the algorithm could sort the original list directly and use only constant extra space. However, keeping the original list unchanged makes the implementation safer for testing and easier to compare with other algorithms.

The main additional memory in this project comes from:

- Copying the input list in Heapsort

- Temporary lists in Merge Sort

- Temporary lists in Quicksort

- The heap list and dictionary in the priority queue

The heap itself is still efficient because it does not require separate tree nodes or pointer connections.

---

`Empirical Comparison With Other Sorting Algorithms`

The project compares Heapsort with Merge Sort and Quicksort. The comparison uses three input distributions:

- Sorted input
- Reverse-sorted input
- Random input
- The program tests the following input sizes:
```
100, 1000, and 3000
```
Each algorithm is timed using Python’s `time.perf_counter()` function. The output of each sorting algorithm is also validated against Python’s built-in sorted() function to make sure the result is correct.

A sample benchmark run is shown below. The exact timing may change depending on the computer, Python version, memory, processor speed, and background processes.

```table
Input Size	Input Type	Algorithm	Sample Runtime in Seconds
100	        Sorted	    Heap Sort	0.000115
100	        Sorted	    Merge Sort	0.000153
100	        Sorted	    Quick Sort	0.000095
100	        Reverse	    Heap Sort	0.000135
100	        Reverse	    Merge Sort	0.000159
100	        Reverse	    Quick Sort	0.000075
100	        Random	    Heap Sort	0.000109
100	        Random	    Merge Sort	0.000192
100	        Random	    Quick Sort	0.000094
1000	    Sorted	    Heap Sort	0.002008
1000	    Sorted	    Merge Sort	0.001920
1000	    Sorted	    Quick Sort	0.001267
1000	    Reverse	    Heap Sort	0.001950
1000	    Reverse	    Merge Sort	0.001993
1000	    Reverse	    Quick Sort	0.000836
1000	    Random	    Heap Sort	0.001880
1000	    Random	    Merge Sort	0.002549
1000	    Random	    Quick Sort	0.001231
3000	    Sorted	    Heap Sort	0.007564
3000	    Sorted	    Merge Sort	0.005829
3000	    Sorted	    Quick Sort	0.003009
3000	    Reverse	    Heap Sort	0.006410
3000	    Reverse	    Merge Sort	0.006073
3000	    Reverse	    Quick Sort	0.003149
3000	    Random	    Heap Sort	0.007120
3000	    Random	    Merge Sort	0.008931
3000	    Random	    Quick Sort	0.004553
```


The results show that all three sorting algorithms work correctly for the tested inputs. Quicksort appears faster in this sample run because the implementation uses the middle element as the pivot. This helps avoid poor behavior for already sorted and reverse-sorted input. Merge Sort also performs consistently, but it uses extra memory because it creates new lists during the merge process. Heapsort is sometimes slightly slower in the sample timing, but it is still very consistent and keeps the same `O(n log n)` time complexity across input types.

The most important observation is that theoretical complexity and actual runtime are related, but they are not always exactly the same in practice. Constant factors, recursion overhead, memory allocation, and implementation style can affect the timing. Larkin, Sen, and Tarjan (2014) also discuss that workload patterns and implementation choices can influence the observed performance of priority queue structures.

---

`Priority Queue Implementation Design`

The priority queue implementation is stored in the file priority_queue_scheduler.py. The main goal of this part is to simulate a scheduler that always processes the most urgent job first.

The implementation uses two custom classes:


Job

UrgencyQueue

The Job class represents one scheduled task. It stores:

- job_code
- priority_score
- created_at
- deadline
- note

The UrgencyQueue class stores jobs in a binary max-heap. I chose a max-heap because the scheduler should always remove the job with the highest priority first. This matches real-world scheduling behavior, where urgent tasks should be handled before less important tasks.

The priority queue stores jobs in a Python list named _items. It also uses a dictionary named _where. The _where dictionary maps each job code to its current index in the heap. This helps with priority updates because the program can find a job directly instead of scanning through the full heap.

This implementation is more realistic than a simple priority queue that only stores numbers. In real systems, tasks often include identifiers, deadlines, arrival times, and descriptions. The Job class supports this by storing multiple fields for each task.

---

`Priority Ordering Rules`

The priority queue does not decide order based only on the priority score. Instead, it uses three comparison rules:

The job with the higher priority_score comes first.
If two jobs have the same priority, the job with the earlier deadline comes first.
If the priority and deadline are both equal, the job with the earlier created_at value comes first.
This tie-breaking logic makes the scheduler more practical. For example, two jobs may both have a priority score of 9, but if one job has an earlier deadline, it should be completed first. If both jobs also have the same deadline, then the older job should be processed first to keep the scheduling behavior fair.

This design avoids random ordering when two jobs have the same priority. It also makes the scheduler output predictable and easier to test.

Priority Queue Operations and Complexity
Insert Operation
The insert(job) method adds a new job to the priority queue. The new job is first placed at the end of the heap list. Then _bubble_up() is called to move the job upward until the max-heap property is restored.

```
The time complexity is:
O(log n)
```

This is because the job may move from a leaf position up toward the root, and the height of a binary heap is logarithmic.

---

`Extract Max Operation`

The extract_max() method removes and returns the most urgent job. Since this is a max-heap, the most urgent job is always stored at index 0.

After removing the root job, the last job in the heap is moved to the root position. Then _bubble_down() is used to restore the heap property.
```
The time complexity is:
O(log n)
```
This is because the replacement job may need to move downward through the height of the heap.

--- 

`Increase Key Operation`

The increase_key(job_code, new_priority) method increases the priority of an existing job. The queue first uses the _where dictionary to locate the job in constant time. After the priority is updated, the job may need to move upward because it has become more urgent.
```
The time complexity is:
O(log n)
```

Without the dictionary, locating the job would require a linear search. With the dictionary, locating the job is efficient, and the main cost is restoring heap order.

---

`Decrease Key Operation`

The decrease_key(job_code, new_priority) method lowers the priority of an existing job. After the priority decreases, the job may need to move downward because other jobs may now have higher priority.
```
The time complexity is:
O(log n)
```
--- 

`Peek Max Operation`

The peek_max() method returns the highest-priority job without removing it. Since the highest-priority job is always at the root, this operation takes:
`O(1)`

---

`Is Empty Operation`
The is_empty() method checks whether the priority queue has any jobs. It only checks the length of the list, so the time complexity is:
`O(1)`

---

`Priority Queue Complexity Summary`
```
Operation	    Description	                            Time Complexity
insert(job)	    Adds a new job and restores heap order	O(log n)
extract_max()	Removes and returns the most urgent job	O(log n)
increase_key()	Raises priority and moves job upward	O(log n)
decrease_key()	Lowers priority and moves job downward	O(log n)
peek_max()	    Reads the highest-priority job	        O(1)
is_empty()	    Checks whether the queue is empty	    O(1)
size()	        Returns the number of jobs	            O(1)
```

Microsoft Learn (2026) explains that priority queues commonly support operations such as enqueue, dequeue, peek, and priority changes. This matches the structure of my implementation, although my version is written in Python and customized for task scheduling.

---

`Scheduler Simulation`

The scheduler simulation creates several sample jobs and inserts them into the priority queue. Example tasks include production incident handling, code review, database backup validation, documentation work, and urgent service patching.

After inserting the jobs, the program increases the priority of one job. This tests whether the heap can correctly adjust after a priority update. Once the update is complete, the scheduler repeatedly calls extract_max() until the queue becomes empty.

Each extracted job represents the next job that should be executed. Since the queue is a max-heap, the most urgent job is always selected first. If two jobs have the same priority, the deadline and creation time rules decide the order.

This simulation shows how a heap-based priority queue can be used in a real scheduling situation. For example, a production issue should normally be handled before a documentation update. If two issues have the same urgency, the one with the closer deadline should be handled first.

---

`Edge Case Handling`

The implementation includes several edge-case checks to make the program more reliable.

First, the priority queue checks for duplicate job codes before inserting a new job. This prevents two jobs with the same identifier from being stored in the queue.

Second, the extract_max() method returns None if the queue is empty. This prevents the program from crashing when there is no job to remove.

Third, the priority update methods check whether the job exists before changing its priority. If the job code is not found, the program raises a clear error message.

Fourth, the increase_key() and decrease_key() methods check whether the new priority value is valid for the operation. For example, increase_key() should not be used to lower a priority.

The Heapsort code also handles small input lists naturally. If the list is empty or has only one item, the heap-building and sorting loops complete without unnecessary work.

These edge cases are important because they help the program behave correctly in more situations.

---

### `Discussion of Results`

The Heapsort implementation worked correctly for sorted, reverse-sorted, and random input. The program validates each result by comparing it with Python’s built-in sorted() function. This validation step is useful because it confirms that the custom sorting logic is producing correct output.

The empirical comparison showed that Heapsort performed consistently across the different input patterns. It did not become extremely slow for already sorted or reverse-sorted input. This supports the theoretical analysis that Heapsort runs in O(n log n) time in the best, average, and worst cases.

Merge Sort also showed stable behavior, but it uses extra memory because it creates temporary lists during the merge process. Quicksort was fast in the sample run, but its performance depends more on pivot selection. Since this implementation uses the middle value as the pivot, it performed well on the tested inputs.

The priority queue simulation also behaved as expected. Jobs with higher priority were extracted first. When jobs had equal priority, the scheduler used deadline and creation time to decide which job should come first. The priority update operation also worked correctly because the heap adjusted after the job priority changed.

Overall, the implementation and testing show that heaps are useful for both sorting and scheduling. They offer a strong balance between performance, simple storage, and practical use.

---

### `Real-World Applications`

Heap data structures are useful in many real-world systems. In operating systems, a priority queue can help decide which process should run next. In customer support systems, urgent tickets can be handled before routine requests. In network systems, packets may be processed based on priority. In simulation systems, future events can be stored based on when they should occur.

Heaps are also useful in graph algorithms. For example, shortest path algorithms often use priority queues to select the next most promising node. This shows that heaps are not only useful for academic exercises but also for practical software systems.

The scheduler in this project is a small example of this idea. Each job has a priority score, deadline, creation time, and note. The queue uses this information to decide which job should be handled next. This is similar to real-world systems where urgent tasks must be prioritized fairly and efficiently.

## Conclusion

This assignment helped me understand heap data structures more clearly by implementing them manually in Python. The Heapsort implementation showed how a max-heap can be used to sort a list in predictable O(n log n) time. The priority queue implementation showed how heaps can be used for scheduling tasks based on urgency.

The class-based design made the project easier to organize. The HeapSorter class handled sorting, while the UrgencyQueue and Job classes handled priority-based scheduling. The use of a dictionary in the priority queue made priority updates more efficient because jobs could be found quickly by their job code.

From the analysis and testing, heaps are practical because they support efficient insertion, extraction, and priority updates. They are also easier to store than pointer-based tree structures because they can be represented with a simple list. Overall, this project showed that heaps are important not only as a data structure concept but also as a useful tool for solving real programming problems.

References
BITS Pilani WILP Division. (2026). Data structures and algorithms: Heap sort and priority queues [PowerPoint slides]. Microsoft SharePoint.

Larkin, D., Sen, S., & Tarjan, R. E. (2014). A back-to-basics empirical study of priority queues. Microsoft Research. 

Microsoft Learn. (2026). .NET implementation of a priority queue (aka heap). Microsoft. 

Miller, B., & Ranum, D. (2025). Problem solving with algorithms and data structures using Python (2nd ed.). Microsoft SharePoint.