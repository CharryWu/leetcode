class CustomStack:

    def __init__(self, maxSize: int):
        self.n = 0
        self.maxSize = maxSize
        self.inc = []
        self.nums = []

    def push(self, x: int) -> None:
        if self.n < self.maxSize:
            self.nums.append(x)
            self.inc.append(0)
            self.n += 1

    def pop(self) -> int:
        if self.n == 0:
            return -1
        elif self.n == 1:
            self.n -= 1
            return self.nums.pop() + self.inc.pop()
        else:
            inctop = self.inc.pop()
            ret = self.nums.pop() + inctop
            self.inc[-1] += inctop
            self.n -= 1
            return ret

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

    def sum(self) -> int:
        s = 0
        inc_acc = 0
        for i in range(self.n-1, -1, -1):
            inc_acc += self.inc[i]
            num = self.nums[i]
            s += (inc_acc + num)
        return s

if __name__ == '__main__':
    cs = CustomStack(4)
    cs.push(4)
    cs.push(5)
    cs.increment(2,1)
    cs.push(6)
    cs.push(7)
    cs.increment(4,2)
    assert cs.sum() == 32
    assert cs.pop() == 9
    assert cs.pop() == 8
    assert cs.pop() == 8
    assert cs.pop() == 7


"""
solution from: https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539716/JavaC%2B%2BPython-Lazy-increment-O(1)

Intuition: like lee215 says, "Use an additional array to record the increment value.
inc[i] means for all elements stack[0] ~ stack[i],
we should plus inc[i] when popped from the stack.
Then inc[i-1]+=inc[i],
so that we can accumulate the increment inc[i]
for the bottom elements and the following pops."

I would like to expand on his explanation a bit further and hand simulate a bit. Some key obsrvations:

when we push we push to both inc and stack, so that at any point in time inc and stack have the same amount of elements.
earlier we said that "inc[i] means for all elements stack[0] ~ stack[i], we should plus inc[i] when popped from the stack" -- let's look at this idea a bit further. The key with this idea is easier to see with hand simulation:
let's say we have a list of ops: push 5, push 3, push 1, inc 2 3, push 9, inc 4 -1

after the 1st inc our data looks like this:
stack: [5,3,1]
inc: [0,3,0]

inc[1] encodes the knowledge that elements 0 thru 1 (inclusive) in the stack are incremented by 3. If we generalize this a bit, inc[i] encodes the knowledge that elements 0 thru i (inclusive) are incremented by the value at inc[i].

let's continue examining this idea. What does our data look like after the second inc?
stack: [5,3,1,9]
inc:[0,3,0,-1]

so this is what our data looks like at the end of all of our operations stated above. we see that our second inc operation is now encoded in our inc array, since inc[3] = -1, which encodes the knowledge that elements 0 thru 3 (inclusive) are incremented by -1. Now observe that our two increment operations now 'overlap' eachother. In the sense that inc[1] is applied to elements 0 thru 1 inclusive and inc[3] is applied to elements 0 thru 3 inclusive. Hence, elements 0 and 1 will have both increment operators applied to them. So for elements 0 and 1, we don't just need to add 3 upon pop (we also need to -1).

Now here's the tricky part which requires somewhat of an intellectual leap to get to. observe that, for our inc array, only inc[-1] (the last element) accurately encodes what to increment by (and this is only accurate for stack[-1] at any given point in time). What this means concretely is that whatever inc[-1] is, if we have a pop operation from our stack, all we have to do is stack.pop()+inc.pop() in order to get the right value popped.

Let's come back to the example we had earlier:
stack: [5,3,1,9]
inc:[0,3,0,-1]

Starting with our data like this, what if we perform a pop? Then we can do inc.pop()+stack.pop() which will yield 8. This is the correct output. However, what we do next is more important. Earlier we said that inc[3] encodes the value we want to add to elements 0 thru 3 (inclusive) of the stack. However at this point we've only added inc[3] to the 3rd element, so we don't want to lose this knowledge before we've acted on all of it. So now that we've popped 3rd element,

inc[3] encodes the value we want to add to elements 0 thru 3 (inclusive) of the stack -> inc[3] encodes the value we want to add to elements 0 thru 2 (inclusive) of the stack

Do you understand how that leap was made? since i've already applied the increment operation to 3rd element, inc[3] no longer needs to encode that knowledge because it's already been acted upon, so at that point inc[3] only encodes the knowledge that this is the value we want to add to elements 0 thru 2 (inclusive), instead of 0 thru 3. So how do we represent this in code? This next step requires a combination of ideas. If we think back to our representation, we said we want at any given point for our last element inc[-1] to have the accurate increment for stack[-1]. And also if we think back to our discussion earlier, we discussed overlap and how our algorithm needs to take into account that overlap. So the way we can do that is by taking inc[3]'s value and adding it to inc[2]. This represents the knowledge transition, from inc[3] encoding the value we want to add to elements 0 thru 3 of ths stack to inc[3] only encoding the value we want to add to elements 0 thru 2. So how do represent this knowledge transition? by moving inc[3]'s value into inc[2]. This is an exact move of our knowledge transition.

So then after that pop we look like this:
stack: [5,3,1]
inc:[0,3,-1]

where inc[2] encodes that -1 should be added to stack elements 0 thru 2 (inclusive). This is in line with what we believe because we are keeping the information from inc[3] alive, as long as we haven't fully acted upon the information. Also -1 is the correct value here because there is no overlap at this element.

So we pop again and end up looking like this:

stack: [5,3]
inc:[0,2]

Notice that we incorporate inc[2]'s value into inc[1]. This is because of the same reasoning as earlier, that inc[2] encodes value about elements 0 thru 2 (incl), and now that we've acted on element 2, we still need to encode the knowledge regarding elements 0 thru 1 (incl), so the way we do that is by bringing inc[2] into inc[1]. But notice that is how our overlap gets handled here. Now instead of increment elements 0 thru 1 by 3 (as our first increment operation suggests), we incorporate the second increment operation (since the ranges overlap), and we only increment the first 2 elements by exactly what is necessary.
"""

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
