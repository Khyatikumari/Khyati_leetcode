class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int end = nums.size()-1;
        int end2 = end;
        while(end > 0 && nums[end-1] >= nums[end]){
            end--;
        }
        // cout<<end<<"-->end"<<endl;
        if(end == 0){
            reverse(nums.begin(), nums.end());
            return;
        }
        while(end2>=end && nums[end2]<=nums[end-1]){
            end2--;
        }
        swap(nums[end-1], nums[end2]);
        reverse(nums.begin()+end, nums.end());

    }
};