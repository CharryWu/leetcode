# https://leetcode.com/problems/valid-number/solutions/23728/a-simple-solution-in-python-based-on-dfa/
# define an NFA
import string
class Solution():
    def isMatch(self, s: str, p: str) -> bool:
        STATE_MACHINE = []
        STARTING_STATE = 0
        ACCEPT_STATE = len(p)
        FAIL_STATE = len(p)+1

        for i, c in enumerate(p):
            nextState = i+1
            if c == '.':
                STATE_MACHINE.append({ x: {nextState} for x in string.ascii_lowercase})
            elif c == '*':
                prev_state = STATE_MACHINE[-1]
                for trans in prev_state:
                    prev_state[trans].add(nextState)
                prev_state['*'] = {nextState}
                STATE_MACHINE.append(prev_state)
            else:
                STATE_MACHINE.append({ c: {nextState}})

        STATE_MACHINE.append({ x: {FAIL_STATE} for x in string.ascii_lowercase+'.*'})
        STATE_MACHINE.append({ x: {FAIL_STATE} for x in string.ascii_lowercase+'.*'})
        print(STATE_MACHINE)
        currentStates = {STARTING_STATE}

        for c in s:
            nextStates = set()
            for state in currentStates:
                if c in STATE_MACHINE[state]:
                    nextStates |= STATE_MACHINE[state][c]
                if '*' in STATE_MACHINE[state]:
                    nextStates |= STATE_MACHINE[state]['*']
            currentStates = nextStates
        if ACCEPT_STATE in currentStates:
            return True
        def hasNext(currentStates):
            return set(filter(lambda state: '*' in STATE_MACHINE[state] and state != FAIL_STATE and state != ACCEPT_STATE, currentStates))
        while (candidate_states := hasNext(currentStates)):
            nextStates = set()
            for state in candidate_states:
                nextStates |= STATE_MACHINE[state]['*']
            if ACCEPT_STATE in nextStates:
                return True
            currentStates = nextStates

        return ACCEPT_STATE in currentStates
