class Solution {
    public int[] searchRange(int[] nums, int target) {

        int len = nums.length;
        int left = 0;
        int rigth = len - 1;

        while (left <= rigth) {
            int mid = left + (rigth - left) / 2;

            if (nums[mid] == target) {
                int i = mid - 1;
                int j = mid + 1;

                while (i >= 0 && nums[i] == target) {
                    i--;
                }

                while (j < len && nums[j] == target) {
                    j++;
                }

                return new int[] { i + 1, j - 1 };

            } else if (nums[mid] > target) {
                rigth = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return new int[] { -1, -1 };
    }
}