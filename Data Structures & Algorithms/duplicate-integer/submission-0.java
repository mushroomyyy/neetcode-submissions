class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seenNumbers = new HashSet<>();
        for (int num: nums) {
            if (!seenNumbers.add(num)) {
                return true;
            }
        }
        return false;
    }
}