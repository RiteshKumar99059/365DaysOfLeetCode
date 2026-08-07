class Solution {
    public String reverseWords(String s) {
        int n = s.length();
        StringBuilder res = new StringBuilder(n);

        int start = 0;

        for(int end = 0; end <= n; end++){
            if(end == n || s.charAt(end)==' '){

                for(int i = end - 1; i >= start; i-- ){
                    res.append(s.charAt(i));
                }
                if(end != n){
                    res.append(' ');
                }
                start = end + 1;
            }
        }
        return res.toString();
        
    }
}