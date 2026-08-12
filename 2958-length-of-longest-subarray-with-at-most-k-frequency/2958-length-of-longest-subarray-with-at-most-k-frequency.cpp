class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> counter;

        int result = 0, lo = 0, hi = 0;
        while (hi < nums.size()) {
            auto& c = counter[nums[hi]];
            if (c < k) {
                result = max(result, (hi + 1) - lo);
                c++;
            } else {
                c++;
                int out = nums[lo];
                counter[out]--;
                lo++;
                while (out != nums[hi]) {
                    out = nums[lo];
                    counter[out]--;
                    lo++;
                }
            }
            hi++;
        }
        return result;
    }
};