#include <vector>
using namespace std;

const int CYCLE = 2;
const int BIT_WIDTH = 32;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        vector<int> bit_counts(BIT_WIDTH, 0);

        for (int bit_pos = 0; bit_pos < BIT_WIDTH; ++bit_pos)
        {
            int shift = 1 << bit_pos;
            for (int num : nums)
            {
                bit_counts[bit_pos] += (num & shift) ? 1 : 0;
            }
        }

        int num = 0;
        for (int i = 0; i < BIT_WIDTH; ++i)
        {
            int shift = 1 << i;
            num += (bit_counts[i] % CYCLE) * shift;
        }

        return num;
    }
};