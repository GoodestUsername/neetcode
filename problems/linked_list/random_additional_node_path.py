from collections import defaultdict, deque
from typing import Optional


# TODO: Look at figure out 1 pass and space optimization
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def get_random_val(self):
        if self.random:
            return self.random.val
        return None

    def get_next_val(self):
        if self.next:
            return self.next.val
        return None


def traverse_and_generate_random_paths(node):
    if node == None:
        return None

    return Node(node.random.val, None, None)


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head == None:
            return None
        if head.next == None:
            new_head = Node(head.val, None, None)
            if head.random != None:
                new_head.random = new_head
            return new_head

        node = head.next
        new_head = Node(head.val, None, None)
        new_node = new_head

        node_space = defaultdict(deque)
        node_space[(head.val, head.get_next_val())] = deque([0])

        node_list = [new_head]
        i = 1
        while node:
            new_node.next = Node(node.val, None, None)
            # if node.get_random_val() == None:
            #     node_space[(node.val, node.get_next_val())].append(-1)
            # else:
            node_space[(node.val, node.get_next_val())].append(i)

            node_list.append(new_node.next)
            new_node = new_node.next
            node = node.next
            i += 1

        node = head
        new_node = new_head
        print(node_space)
        while node:
            if node.random != None:
                print(node.val, (node.get_random_val(), node.random.get_next_val()))
                if (
                    len(node_space[(node.get_random_val(), node.random.get_next_val())])
                    > 1
                ):
                    ran_index = node_space[
                        (node.get_random_val(), node.random.get_next_val())
                    ].popleft()
                else:
                    ran_index = node_space[
                        (node.get_random_val(), node.random.get_next_val())
                    ][0]
                new_node.random = node_list[ran_index]

            node = node.next
            new_node = new_node.next
        return new_head
        # do this in (1)n time using recursion
        # make random on reference to it, and check if it's been made for next

    # one pass version of above
    # creates default dict of node, so that each access will create the one required, then
    # we set the right values

    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     oldToCopy = collections.defaultdict(lambda: Node(0))
    #     oldToCopy[None] = None

    #     cur = head
    #     while cur:
    #         oldToCopy[cur].val = cur.val
    #         oldToCopy[cur].next = oldToCopy[cur.next]
    #         oldToCopy[cur].random = oldToCopy[cur.random]
    #         cur = cur.next
    #     return oldToCopy[head]


# space optimal I
# def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
#     if head is None:
#         return None

#     l1 = head
#     while l1 is not None:
#         l2 = Node(l1.val)
#         l2.next = l1.next
#         l1.next = l2
#         l1 = l2.next

#     newHead = head.next

#     l1 = head
#     while l1 is not None:
#         if l1.random is not None:
#             l1.next.random = l1.random.next
#         l1 = l1.next.next

#     l1 = head
#     while l1 is not None:
#         l2 = l1.next
#         l1.next = l2.next
#         if l2.next is not None:
#             l2.next = l2.next.next
#         l1 = l1.next

#     return newHead

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# space optimal 2
# class Solution:
#     def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
#         if head is None:
#             return None

#         l1 = head
#         while l1:
#             l2 = Node(l1.val)
#             l2.next = l1.random
#             l1.random = l2
#             l1 = l1.next

#         newHead = head.random

#         l1 = head
#         while l1:
#             l2 = l1.random
#             l2.random = l2.next.random if l2.next else None
#             l1 = l1.next

#         l1 = head
#         while l1 is not None:
#             l2 = l1.random
#             l1.random = l2.next
#             l2.next = l1.next.random if l1.next else None
#             l1 = l1.next

#         return newHead
