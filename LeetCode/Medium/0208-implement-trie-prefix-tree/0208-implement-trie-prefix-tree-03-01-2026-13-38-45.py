class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndFlag = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = TrieNode()
            node = node.children[x]
        node.EndFlag = True

    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]
        return node.EndFlag

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)