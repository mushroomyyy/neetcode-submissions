class Solution {
    public int longestConsecutive(int[] nums) {
        // if length is 0 return
        if (nums.length == 0) return 0;
        // change it into a set of O(n) operations
        HashSet<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }
        // min value
        int longest = 0;

        for (int num: set) {
            //start counting the length when the number is the beginning of a sequence
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int length = 1;
            // if the set has the next value, continue to count the length
            while(set.contains(currentNum + 1)) {
                currentNum++;
                length ++;
            }   
                // see if the current length is longer or the previous longest length
                longest = Math.max(length,longest); 

            }


    }
        return longest;
    }
    }

