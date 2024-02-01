class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey == "type": 
            k = 0
        elif ruleKey == "color":
            k = 1
        else:
            k = 2
        match = 0

        for j in items:
            if j[k] == ruleValue:
                match = match + 1
        
        return match
        