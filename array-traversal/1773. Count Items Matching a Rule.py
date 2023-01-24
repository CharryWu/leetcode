class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        check_type = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        for item in items:
            if item[check_type] == ruleValue:
                count += 1
        
        return count