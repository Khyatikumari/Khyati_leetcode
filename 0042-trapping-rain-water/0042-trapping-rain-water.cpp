class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0, n = height.size();

        vector<int> lefts(n, 0);
        lefts[0] = (height[0]);
        for(int i =1; i<n; i++){
            lefts[i] = max(lefts[i-1], height[i]);
        }

        vector<int> rights(n, 0);
        rights[n-1] = (height[n-1]);
        for(int i =n-2; i>-1; i--){
            rights[i] = max(rights[i+1], height[i]);
        }

        for(int i =0; i<n; i++){
            res += min(rights[i],lefts[i]) - height[i];
        }
        return res;
    }
};