
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> result = new HashMap<>();
        for (String word:strs)
        {
            char[] count = new char[26];
            for(char i:word.toCharArray())
            {
                count[i-'a'] ++;
            }
            String key = new String(count);
            result.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }
        return new ArrayList<>(result.values());
    }
}
