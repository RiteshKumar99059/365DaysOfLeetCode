class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();

        int start = 0;

        for(int end = 0; end <= s.length(); end++){
            if(end == s.length() || s.charAt(end)==' '){

                for(int i = end - 1; i >= start; i-- ){
                    res.append(s.charAt(i));
                }
                if(end != s.length()){
                    res.append(' ');
                }
                start = end + 1;
            }
        }
        return res.toString();
        
    }
}