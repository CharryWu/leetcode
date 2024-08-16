def get_freq(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c)-ord('a')] += 1
    return freq

from collections import Counter
def getSequence(dna):
    def is_special(seq1, seq2):

        # Count frequencies of characters in both sequences
        count1 = get_freq(seq1)
        count2 = get_freq(seq2)

        # Check if the sequences are already anagrams
        if count1 == count2:
            return True

        count1_surplus = 0
        count2_surplus = 0

        for freq1, freq2 in zip(count1, count2):
            if freq1 > freq2:
                count1_surplus += 1
                if count1_surplus >= 2: return False
            elif freq2 > freq1:
                count2_surplus += 1
                if count2_surplus >= 2: return False

        if count1_surplus >= 2 or count2_surplus >= 2:
            return False

        return True

    results = []
    for a, b in dna:
        results.append(is_special(a, b))

    return results

# Example usage:
dna_pairs = [
    ["safddadfs", "famafmss"]
] # TRUE

print(getSequence(dna_pairs))

dna_pairs = [
    ["abcee", "acdeedb"],
    ["sljffsajej", "sljsje"]
]


print(getSequence(dna_pairs)) # [true, false]

