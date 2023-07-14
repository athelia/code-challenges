# CTCI Chapter 3, Stacks and Queues
from typing import Any, Optional, Union
from ctci_2 import LinkedList, Node


class StackLL(LinkedList):
    """Implement a Stack using a LinkedList."""

    def __init__(
        self, top: Union[Node, Any], _: Node = None, verbose: bool = False
    ) -> None:
        # Convenience conversion
        top = Node(top) if type(top) is not Node else top
        super().__init__(head=top, tail=_, verbose=False)
        self.top = self.head
        if verbose:
            print(f"Created Stack top={self.top}")

    def push(self, pushed: Union[Node, Any], verbose: bool = False) -> None:
        """Push a new Node onto the stack by prepending to the LinkedList"""
        # Convenience conversion
        node = Node(pushed) if type(pushed) is not Node else pushed
        super().prepend(node, verbose=False)
        # Prepend reassigns head, but we must manually reassign top
        self.top = self.head
        if verbose:
            print(f"Pushed node {node}")

    def pop(self, verbose: bool = False) -> Node:
        """Pop a Node if any exists off the stack by returning the head of the LinkedList"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty Stack")

        popped = self.top
        self.top = self.head = popped.next
        if verbose:
            print(f"Popped value {popped.value}")
        return popped

    def peek(self) -> Optional[Any]:
        """Return the value of the top node."""
        return self.top.value if not self.is_empty() else None

    def is_empty(self) -> bool:
        return self.top is None

    def __repr__(self) -> str:
        return f"<StackLL top={self.top}>"


class QueueLL(LinkedList):
    """Implement a Queue using a LinkedList."""

    def __init__(
        self, first: Union[Node, Any], last: Node = None, verbose: bool = False
    ):
        # Convenience conversion
        first = Node(first) if type(first) is not Node else first
        super().__init__(head=first, tail=last, verbose=False)
        self.first, self.last = self.head, self.tail
        if verbose:
            print(f"Created Queue first={self.first} last={self.last}")

    def enqueue(self, node: Node, verbose: bool = False) -> None:
        """Enqueue onto the tail and update last"""
        super().append(node=node, verbose=False)
        self.last = self.tail
        if verbose:
            print(f"Enqueued node {node}")

    def dequeue(self, verbose: bool = False) -> Optional[Node]:
        """Dequeue from the head and update `first`."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Queue")

        dequeued = self.first
        self.first = self.head = dequeued.next
        if self.first is None:
            self.last = self.tail = None
        if verbose:
            print(f"Dequeued value {dequeued.value}")
        return dequeued

    def peek(self) -> Optional[Any]:
        """Return the value of the first node."""
        return self.first.value if not self.is_empty() else None

    def is_empty(self) -> bool:
        return self.first is None


class StackList:
    """Implement a Stack using a Python List."""

    def __init__(self, data: Any) -> None:
        self.stack = [data]

    def push(self, data: Any) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Cannot pop from empty Stack")
        return self.stack.pop()

    def peek(self) -> Optional[Any]:
        """Return the value of the top node."""
        return self.stack[-1].value if self.stack else None

    def is_empty(self) -> bool:
        return self.stack is []


class QueueList:
    """Implement a Queue using a Python List."""

    def __init__(self, data: Any) -> None:
        self.queue = [data]

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        """Because it is implemented using a List, dequeueing is O(n) time."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Queue")
        dequeued = self.queue[0]
        self.queue = self.queue[1:]
        return dequeued

    def peek(self) -> Optional[Any]:
        """Return the value of the first node."""
        return self.queue[0].value if self.queue else None

    def is_empty(self) -> bool:
        return self.queue is []


# CTCI 3.2
class MinStack(StackLL):
    """Implement a Stack that also knows the current minimum."""

    def __init__(self, top: Union[Node, Any], verbose: bool = False):
        top = Node(top) if type(top) is not Node else top
        el_type = type(top.value)
        # TODO: implement smarter type checking
        if el_type not in [str, int, float]:
            raise TypeError(
                "MinStack requires rich comparison and only supports str, int, and float types"
            )
        super().__init__(top=top, verbose=verbose)
        self.minimums = StackLL(Node(top.value))
        self.element_type = el_type

    def push(self, pushed: Union[Node, Any], verbose: bool = False) -> None:
        # check that type of pushed element matches the existing elements
        el_type = type(pushed) if type(pushed) is not Node else type(pushed.value)
        if el_type != self.element_type:
            raise TypeError(
                f"MinStack requires rich comparison.\
            Existing elements are {self.element_type}; pushed type is {el_type}"
            )
        super().push(pushed=pushed, verbose=verbose)
        if self.peek() <= self.minimums.peek():
            self.minimums.push(pushed)

    def pop(self, verbose: bool = False) -> Node:
        popped = super().pop(verbose=verbose)
        if popped.value == self.minimums.peek():
            self.minimums.pop()
        return popped

    def get_min(self) -> Node:
        return self.minimums.peek()


# CTCI 3.3 WIP
class SetOfStacks:
    def __init__(
        self, top: Union[Node, Any], overflow_size: int, verbose: bool = False
    ) -> None:
        self.overflow_size = overflow_size
        top_stack = StackLL(top=top, verbose=verbose)
        self.stacks = StackLL(top=Node(top_stack), verbose=verbose)

    def push(self, pushed: Union[Node, Any]) -> None:
        top_stack = self.stacks.peek()
        # If the top stack has too many elements, make a new stack and push it onto the stack of stacks
        if top_stack.get_length() == self.overflow_size:
            new_stack = StackLL(pushed)
            self.stacks.push(Node(new_stack))
        else:
            top_stack.push(pushed)

    def pop(self) -> Node:
        top_stack = self.stacks.peek()
        popped = top_stack.pop()
        if top_stack.is_empty():
            self.stacks.pop()
        return popped

    def peek(self) -> Any:
        """Peek at the top value of the top stack."""
        return self.stacks.peek().peek()

    def is_empty(self) -> bool:
        return self.stacks.is_empty()

    def pop_at(self, i: int) -> Node:
        stack_index = 0
        current = self.stacks.peek()
        while stack_index < i:
            current = current.next
            stack_index += 1
        # Is this a problem? we don't rebalance
        return current.pop()


# CTCI 3.4
class QueueFromStacks:
    def __init__(self, initial: Any) -> None:
        self.stack_newest = StackLL(initial)
        self.stack_oldest = StackLL(None)

    def push(self, value) -> None:
        self.stack_newest.push(Node(value))

    def stack_shift(self) -> None:
        if self.stack_newest.is_empty():
            current = self.stack_oldest.top
            # stack = self.stack_oldest
            transfer_stack = self.stack_newest
        else:
            current = self.stack_newest.top
            # stack = self.stack_newest
            transfer_stack = self.stack_oldest
        while current:
            transfer_stack.push(current)
            current = current.next

    def pop(self) -> Node:
        if self.stack_oldest.is_empty():
            self.stack_shift()
        return self.stack_oldest.pop()


# CTCI 3.6
class AnimalShelter:
    pass
