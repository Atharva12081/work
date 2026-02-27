#!/usr/bin/env python3
"""
File: algorithms.py
Description: Implementation of common algorithms and data structures
Author: Atharva
Date: 2025-01-25
"""

from typing import List, Dict, Any, Optional, Tuple
import random


class SortingAlgorithms:
    """Collection of sorting algorithms"""
    
    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """Bubble sort implementation"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """Quick sort implementation"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)
    
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """Merge sort implementation"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms.merge(left, right)
    
    @staticmethod
    def merge(left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        """Insertion sort implementation"""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr


class SearchAlgorithms:
    """Collection of search algorithms"""
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """Binary search implementation"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def linear_search(arr: List[int], target: int) -> int:
        """Linear search implementation"""
        for i, value in enumerate(arr):
            if value == target:
                return i
        return -1
    
    @staticmethod
    def interpolation_search(arr: List[int], target: int) -> int:
        """Interpolation search for uniformly distributed data"""
        low, high = 0, len(arr) - 1
        
        while low <= high and target >= arr[low] and target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1
            
            pos = low + ((target - arr[low]) * (high - low) // 
                        (arr[high] - arr[low]))
            
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        
        return -1


class DataStructures:
    """Implementation of common data structures"""
    
    class Stack:
        """Stack data structure"""
        
        def __init__(self):
            self.items = []
        
        def push(self, item: Any) -> None:
            self.items.append(item)
        
        def pop(self) -> Any:
            if self.is_empty():
                raise IndexError("Pop from empty stack")
            return self.items.pop()
        
        def peek(self) -> Any:
            if self.is_empty():
                raise IndexError("Peek from empty stack")
            return self.items[-1]
        
        def is_empty(self) -> bool:
            return len(self.items) == 0
        
        def size(self) -> int:
            return len(self.items)
    
    class Queue:
        """Queue data structure"""
        
        def __init__(self):
            self.items = []
        
        def enqueue(self, item: Any) -> None:
            self.items.append(item)
        
        def dequeue(self) -> Any:
            if self.is_empty():
                raise IndexError("Dequeue from empty queue")
            return self.items.pop(0)
        
        def front(self) -> Any:
            if self.is_empty():
                raise IndexError("Front of empty queue")
            return self.items[0]
        
        def is_empty(self) -> bool:
            return len(self.items) == 0
        
        def size(self) -> int:
            return len(self.items)
    
    class LinkedList:
        """Linked list implementation"""
        
        class Node:
            def __init__(self, data: Any):
                self.data = data
                self.next = None
        
        def __init__(self):
            self.head = None
        
        def append(self, data: Any) -> None:
            new_node = self.Node(data)
            
            if not self.head:
                self.head = new_node
                return
            
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        def prepend(self, data: Any) -> None:
            new_node = self.Node(data)
            new_node.next = self.head
            self.head = new_node
        
        def delete(self, data: Any) -> bool:
            if not self.head:
                return False
            
            if self.head.data == data:
                self.head = self.head.next
                return True
            
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return True
                current = current.next
            
            return False
        
        def find(self, data: Any) -> bool:
            current = self.head
            while current:
                if current.data == data:
                    return True
                current = current.next
            return False
        
        def to_list(self) -> List[Any]:
            result = []
            current = self.head
            while current:
                result.append(current.data)
                current = current.next
            return result


class GraphAlgorithms:
    """Graph algorithms implementation"""
    
    @staticmethod
    def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
        """Breadth-first search"""
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            node = queue.pop(0)
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    @staticmethod
    def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
        """Depth-first search"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result


def main():
    """Main entry point for testing"""
    # Test sorting algorithms
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Bubble sort: {SortingAlgorithms.bubble_sort(arr.copy())}")
    print(f"Quick sort: {SortingAlgorithms.quick_sort(arr.copy())}")
    print(f"Merge sort: {SortingAlgorithms.merge_sort(arr.copy())}")
    
    # Test search algorithms
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"\nBinary search for 7: {SearchAlgorithms.binary_search(sorted_arr, 7)}")
    print(f"Linear search for 7: {SearchAlgorithms.linear_search(sorted_arr, 7)}")
    
    # Test data structures
    stack = DataStructures.Stack()
    stack.push(1)
    stack.push(2)
    print(f"\nStack pop: {stack.pop()}")
    
    queue = DataStructures.Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Queue dequeue: {queue.dequeue()}")


if __name__ == "__main__":
    main()

