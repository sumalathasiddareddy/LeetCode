class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> hm1 = new HashMap<Character,Integer>();
        HashMap<Character,Integer> hm2 = new HashMap<Character,Integer>();

        for (char c:s.toCharArray()){
            hm1.compute(c,(k,v)->v==null?1:v+1);
        }
        
        for (char c:t.toCharArray()){
            hm2.compute(c,(k,v)->v==null?1:v+1);
        }
    
        return hm1.equals(hm2);    
    
    }
}