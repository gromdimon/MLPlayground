# Implementation of Trie data structure

from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.output = []
        self.failure_link = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.failure_link = self.root  # The root's failure link points to itself

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.output.append(word)

    def construct(self, words):
        for word in words:
            self.insert(word)
        self._build_failure_links()

    def _build_failure_links(self):
        # Initialize the queue with the root's direct children
        queue = deque(self.root.children.values())

        while queue:
            current_node = queue.popleft()

            # Iterate over the current node's children to set their failure links
            for char, child_node in current_node.children.items():
                # Find the failure link for the current child
                fail_node = current_node.failure_link
                while fail_node != self.root and char not in fail_node.children:
                    fail_node = fail_node.failure_link

                # Set the child's failure link. If the fail_node has a child with the matching char,
                # link to that child; otherwise, link to root.
                child_node.failure_link = fail_node.children.get(char, self.root)

                # If the failure link node is an end of a word, extend the current node's output with it
                if child_node.failure_link.is_end_of_word:
                    child_node.output.extend(child_node.failure_link.output)

                # Add the current child to the queue for further processing of its children
                queue.append(child_node)

    def search(self, text):
        result = []
        node = self.root
        for i, char in enumerate(text):
            while node != self.root and char not in node.children:
                node = node.failure_link
            if char in node.children:
                node = node.children[char]
            else:
                continue
            if node.output:
                for word in node.output:
                    result.append((word, i - len(word) + 1))
        return result
