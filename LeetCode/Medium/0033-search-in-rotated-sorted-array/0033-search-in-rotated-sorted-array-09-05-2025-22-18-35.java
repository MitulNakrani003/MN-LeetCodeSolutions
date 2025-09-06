class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0)
        {
            return -1;
        }
        if(nums.length == 1 && nums[0] == target)
        {
            return 0;
        }
        if(nums.length == 1 && nums[0] != target)
        {
            return -1;
        }
        int start = 0, end = nums.length - 1;
        while(start < end)
        {
            int middle = (start + end)/2;
            if(nums[middle] == target)
            {
                return middle;
            }
            if(nums[start] <= nums[middle]) 
            {
                if(target >= nums[start] && target < nums[middle])
                {
                    end = middle - 1;
                }
                else
                {
                    start = middle + 1;
                }
            }
            else
            {
                if(nums[middle] < target && target <= nums[end])
                {
                    start = middle + 1;
                }
                else
                {
                    end = middle - 1;
                }
            }
        }
        if(nums[start] == target)
        {
            return start;
        }
        else
        {
            return -1;
        }
    }
}