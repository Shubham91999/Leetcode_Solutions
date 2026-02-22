class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        root = trie.root
        for word in words:
            trie.addWord(word)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, cur, word):
            if r < 0 or c < 0 or r >= rows or c >= cols \
            or (r, c) in visit or board[r][c] not in cur.children:
                return

            visit.add((r, c))
            cur = cur.children[board[r][c]]
            word += board[r][c]
            if cur.endOfWord:
                res.add(word)

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, cur, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)

