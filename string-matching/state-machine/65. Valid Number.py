# https://leetcode.com/problems/valid-number/solutions/23728/a-simple-solution-in-python-based-on-dfa/
# define a DFA
STATE_MACHINE = {
    0: {},
    1: {'blank': 1, 'sign': 2, 'digit': 3, '.': 4}, # State (1) - initial state (scan ahead thru blanks)
    2: {'digit': 3, '.': 4}, # State (2) - found sign (expect digit/dot)
    3: {'digit': 3, '.': 5, 'e': 6, 'blank': 9}, # State (3) - digit consumer (loop until non-digit)
    4: {'digit': 5}, # State (4) - found dot (only a digit is valid)
    5: {'digit': 5, 'e': 6, 'blank': 9}, # State (5) - after dot (expect digits, e, or end of valid input)
    6: {'sign': 7, 'digit': 8}, # State (6) - found 'e' (only a sign or digit valid)
    7: {'digit': 8}, # State (7) - sign after 'e' (only digit)
    8: {'digit': 8, 'blank': 9}, # State (8) - digit after 'e' (expect digits or end of valid input)
    9: {'blank': 9} # State (9) - Terminal state (fail if non-blank found)
}

SIGN = {'+', '-'}
ACCEPT_STATE = {3, 5, 8, 9}

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        currentState = 1
        for c in s:
            if c.isdigit():
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in SIGN:
                c = 'sign'
            elif c.lower() == 'e':
                c = 'e'
            if c not in STATE_MACHINE[currentState]:
                return False
            currentState = STATE_MACHINE[currentState][c]
        if currentState not in ACCEPT_STATE:
            return False
        return True
