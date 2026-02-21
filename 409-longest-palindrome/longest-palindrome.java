class Solution {
    public int longestPalindrome(String s) {

        HashSet<Character> chars = new HashSet<Character>();
        int length=0;

        for (char c:s.toCharArray()){
            if (chars.contains(c)){
                chars.remove(c);
                length+=2;
            }
            else{
                chars.add(c);
            }
        }

        if (!chars.isEmpty()){
            length += 1;
        }

        return length;
        
    }
}