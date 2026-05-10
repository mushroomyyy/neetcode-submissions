class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            // complement = number we need to reach the target
            int complement = target - nums[i];

            // If the complement is already in the map, we found a solution
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }

            // Store the current number in the map
            // Key = current number, Value = its index
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
