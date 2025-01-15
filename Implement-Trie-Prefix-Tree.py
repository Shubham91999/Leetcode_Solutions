class Trie:
    def __init__(self):
        # Initialize the root of the trie with 26 children for each letter of the alphabet.
        self.children = [None] * 26
        # A boolean flag to check if the node represents the end of a word.
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self
        for char in word:
            index = ord(char) - ord('a')  # Map character to trie node index.
            if node.children[index] is None:
                node.children[index] = Trie()  # Create a new node if none exists.
            node = node.children[index]
        node.is_end_of_word = True  # Mark the end of the word.

    def search(self, word: str) -> bool:
        """Searches for a word in the trie."""
        node = self._search_prefix(word)
        # Word is found if we found a node where the prefix ends and is_end_of_word is True.
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        node = self._search_prefix(prefix)
        # If we found a node, the prefix exists in the trie.
        return node is not None

    def _search_prefix(self, prefix: str):
        """Searches for a node in the trie that represents the given prefix."""
        node = self
        for char in prefix:
            index = ord(char) - ord('a')  # Map character to trie node index.
            if node.children[index] is None:
                return None  # If a node doesn't exist for a character, return None.
            node = node.children[index]
        return node