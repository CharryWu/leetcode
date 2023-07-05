#include <vector>
using namespace std;
class Solution {
public:
    /**
    Lets take xor of the whole array( my first for loop ).
    The resultant would be of the form a^b, where a and b both are unique number whose frequency is one and the xor would not be zero because numbers are distinct
    Now we know that the total xor is non zero therefore atleast one bit in it must be set. This set bit would have come from either a or from b but not both becasue 1 ^ 1 = 0 i.e if both a and b have same set bit it would get toggled.
    lets assume that it came from b. Iterate through the array and take xor of all the elements where that bit is set( it wont be in a ). Every number would come in pair except b so prevxor ^ b = a;
    Now that we have a, xor it with initial array xor to get b.
    NOTE : It doesn't matter which set bit we choose in point 4. The concept would remain the same.
    */
    vector<int> singleNumber(vector<int>& nums) {
        int number = 0;
        for( int i = 0; i < nums.size(); i++ ){
            number ^= nums[i];
        }
        int setBit = 1;
        while( true ){
            if( number & ( setBit ) ){
                break;
            }
            setBit <<= 1;
        }
        int firstAns = 0;
        for( int i = 0; i < nums.size(); i++ ){
            if( nums[i]&setBit ){
                firstAns ^= nums[i];
            }
        }
        int secondAns = firstAns^number;
        return {firstAns,secondAns};
    }
};