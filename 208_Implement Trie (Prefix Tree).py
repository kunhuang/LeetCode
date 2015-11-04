class TrieNode(object):
    def __init__(self, val):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.children = []
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        i = 0
        node = self.root
        stop = False
        while not stop and i < len(word):
            stop = True
            for children in node.children:
                if children.val == word[i]:
                    i += 1
                    node = children
                    stop = False
                    break
                
        for j in range(i, len(word)):
            new_node = TrieNode(word[j])
            node.children.append(new_node)
            node = new_node

        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        i = 0
        while i < len(word):
            stop = True
            for children in node.children:
                if children.val == word[i]:
                    node = children
                    i += 1
                    stop = False
                    break
            if stop:
                return False
        if node.is_end:
            return True
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        i = 0
        while i < len(prefix):
            stop = True
            for children in node.children:
                if children.val == prefix[i]:
                    node = children
                    i += 1
                    stop = False
                    break
            if stop:
                return False
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("keys")
trie.insert("ke")
trie.insert("y")
print trie.search("key")
print trie.startsWith("ys")