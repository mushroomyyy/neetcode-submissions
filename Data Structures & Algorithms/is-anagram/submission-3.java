class Solution {
    public boolean isAnagram(String s, String t) {
        // if the strings have different length, they cannot be an anagram, return
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> anagramMap = new HashMap<>();
        //record each char in a map
        for (char c : s.toCharArray()) {
            anagramMap.put(c, anagramMap.getOrDefault(c, 0) + 1);
        }
        // if the s map does not contain this alphabet, return
        for (char c : t.toCharArray()) {
            if (!anagramMap.containsKey(c)) {
                return false;
            }
            // if it does then take 1 out from s map
            anagramMap.put(c, anagramMap.get(c) - 1);
            // if t list has characters not in s map, return
            if (anagramMap.get(c) < 0) {
                return false;
            }
        }

        return true;
    }
}
