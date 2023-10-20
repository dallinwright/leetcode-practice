class TrieNode:

    # constructor, Time O(1) Space O(1)
    def __init__(self, c):
        self.data = c
        self.is_end = False
        self.children = {}  # map


class Trie:
    # constructor, Time O(1) Space O(1)
    def __init__(self):
        self.root = TrieNode('')

    # Add a word to trie, Time O(s) Space O(1) s is word length
    def insert(self, word):
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode(character)

            node = node.children[character]

        node.is_end = True

    # find all word with given prefix
    # Time O(n), Space O(n), n is number of nodes involved (include prefix and branches)
    def autocomplete(self, word):
        res = []
        node = self.root

        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return []

        self.helper(node, res, word[:-1])  # except the last "ama", node is "z"

        return res

    # recursive function called by autocomplete
    # Time O(n), Space O(n), n is number of nodes in branches
    def helper(self, node, res, prefix):
        if node.is_end:
            res.append(prefix + node.data)

        for child in node.children.values():
            self.helper(child, res, prefix + node.data)


def test_trie_autocomplete():
    trie = Trie()
    trie.insert("amazon")
    trie.insert("amazon prime")
    trie.insert("amazing")
    trie.insert("amazing spider man")
    trie.insert("amazed")
    trie.insert("apple")

    print(trie.autocomplete('amaz'))
