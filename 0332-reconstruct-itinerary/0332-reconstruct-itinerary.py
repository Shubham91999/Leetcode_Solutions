class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        tickets = sorted(tickets)

        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)

        res = ['JFK']

        def dfs(src: str) -> None:
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, nei in enumerate(temp):
                res.append(nei)
                adj[src].pop(i)
                if dfs(nei):
                    return True
                res.pop()
                adj[src].insert(i, nei)

            return False

        dfs('JFK')
        return res
        """
        tickets = sorted(tickets)[::-1]
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)

        res = []

        def dfs(src: str) -> None:
            while adj[src]:
                nei = adj[src].pop()
                dfs(nei)
            res.append(src)

        dfs('JFK')
        return res[::-1]