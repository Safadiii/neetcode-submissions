class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        final_arr = []
        dp_answers = {}
        for query in queries:
            if query in dp_answers.keys():
                continue
            max_beauty = 0
            for entry in items:
                if query >=  entry[0]:
                    if max_beauty <= entry[1]:
                        max_beauty = entry[1]
            dp_answers[query] = max_beauty
        
        for fquery in queries:
            final_arr.append(dp_answers[fquery])
        return final_arr
