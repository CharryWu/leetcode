class SparseVector:
    def __init__(self, nums):
        """
        Each non-zero value is saved as a (index, value) tuple
        """
        self.val = [(idx, num) for idx, num in enumerate(nums) if num != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        Use two pointers i, j, pointing to self and vec
        if self[i] and vec[j] points to same position, can do dot product;
        if point to different position, product is zero, move pointer to smaller index to next
        """
        i, j = 0, 0
        res = 0

        while i < len(self.val) and j < len(vec.val):
            if self.val[i][0] == vec.val[j][0]: # if index is same, can do dot product
                res += self.val[i][1] * vec.val[j][1]
                i += 1
                j += 1
            elif self.val[i][0] < vec.val[j][0]: # index not same, product is zero, skip to next
                i += 1
            else:
                j += 1
        return res
