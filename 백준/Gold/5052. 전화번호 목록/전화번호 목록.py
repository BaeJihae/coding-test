import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, str):
        current_node = self.head

        for char in str:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = str

    def search(self, str):
        current_node = self.head
        for char in str:
            if current_node.data:
                return True

            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        return False

input = sys.stdin.readline

for _ in range(int(input())):
    trie = Trie()
    answer = "YES"

    str_arr = []
    for _ in range(int(input())):
        str_arr.append(input().rstrip())

    str_arr.sort(key=lambda x: len(x))

    for str in str_arr:
        if trie.search(str):
            answer = "NO"
            break
        trie.insert(str)

    print(answer)