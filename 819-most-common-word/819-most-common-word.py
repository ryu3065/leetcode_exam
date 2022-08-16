import re, collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        temp = re.sub(r'[^\w]',' ', paragraph).lower().split()
        
        list_para = [value for value in temp if value not in banned]
        # print(list_para)
 
        return collections.Counter(list_para).most_common(1)[0][0]
    
        