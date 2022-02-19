"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        # self.__priority_queue = {
        #     0: [],
        #     1: [],
        #     2: [],
        #     3: [],
        #     4: [],
        #     5: [],
        #     6: [],
        #     7: [],
        #     8: [],
        #     9: [],
        #     10: []
        # }  # todo для очереди можно использовать python dict
        self.__priority_queue = {}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        try:
            self.__priority_queue[priority].append(elem)

        except KeyError:
            self.__priority_queue[priority] = [elem]

        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for i in range(11):
            try:
                if self.__priority_queue[i]:
                    return self.__priority_queue[i].pop(0)
            except KeyError:
                continue
            return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        # for i in range(11):
        #     if self.__priority_queue[i]:
        #         try:
        #             return self.__priority_queue[i][ind]
        #         except IndexError:
        #             ind = 0
        #             pass
        try:
            if self.__priority_queue[priority]:
                return self.__priority_queue[priority][ind]
            else:
                return None
        except:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        # for priority in range(11):
        #     self.__priority_queue[priority] = None
        self.__priority_queue.clear()
        return None
