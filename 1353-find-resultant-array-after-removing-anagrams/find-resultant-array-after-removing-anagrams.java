class Solution {
    public List<String> removeAnagrams(String[] words) {

        List<String> ans = new ArrayList<String>();
        String prev="";
        String curr="";
        
        for (int i=0;i<words.length;i++){
            char[] ch = words[i].toCharArray();
            Arrays.sort(ch);
            curr = String.valueOf(ch);
            if (!curr.equals(prev)){
                ans.add(words[i]);
                prev=curr;
            }

        }

        return ans;
        
    }
}