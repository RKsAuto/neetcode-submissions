class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }
        else
        {
            int[] alpha = new int[26];
            int len = s.length();
            for(int i=0;i<len;i++)
            {
                alpha[s.charAt(i) - 'a'] ++;
                alpha[t.charAt(i) - 'a'] --;
            }

            for(int num:alpha)
            {
                if(num!=0)
                {
                    return false;
                }
                
            }
        }
        return true;
    }
}
