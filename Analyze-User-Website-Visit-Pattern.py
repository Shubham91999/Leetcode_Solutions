from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        graph = defaultdict(list)  # Using default dict to prevent key error
        for (t, user, web) in sorted(zip(timestamp, username, website)):
            graph[user].append(web)  # Making adj list of user => websites visited

        scores = defaultdict(int)  # Dict to maintain pattern => scores
        for user, websites in graph.items():
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1  # Incrementing score for the pattern given by combinations

        max_pattern, max_cnt = '', 0
        for pattern, cnt in scores.items():
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt
        return max_pattern


        

        

