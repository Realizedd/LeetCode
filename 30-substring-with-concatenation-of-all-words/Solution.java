import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Solution {

    public List<Integer> findSubstring(String s, String[] words) {
        Map<String, Integer> map = new HashMap<>();

        for (String word : words) {
            Integer res = map.get(word);
            map.put(word, res == null ? 1 : ++res);
        }

        List<Integer> ans = new LinkedList<>();
        int wordLen = words[0].length();
        int wordsLen = words.length;
        int concatLen = wordLen * wordsLen;        

        if (s.length() < concatLen) {
            return ans;
        }
        
        Map<String, Integer> curMap = new HashMap<>();

        for (int start = 0; start < s.length(); start++) {
            int end = start + concatLen - 1;

            //System.out.println("start=" + start + ", end=" + end);
            if (end >= s.length()) {
                break;
            }

            int curLen = 0;

            for (int i = 0; i < wordsLen; i++) {
                int wordIndex = start + i * wordLen;
                String word = s.substring(wordIndex, wordIndex + wordLen);
                //System.out.println("start=" + start + ", end=" + end + ", word=" + word);

                if (map.containsKey(word)) {
                    Integer res = curMap.get(word);

                    if (res != null && res == map.get(word)) {
                        //System.out.println(1);
                        break;
                    }
                    
                    curMap.put(word, res == null ? 1 : ++res);
                    curLen += wordLen;
                    //System.out.println("Put " + word + ". curLen=" + curLen + ", concatLen=" + concatLen);/

                    if (curLen == concatLen) {
                        ans.add(start);
                    }
                } else {
                    //System.out.println(2);
                    break;
                }
            }

            curMap = new HashMap<>();
        }

        return ans;
    }

    public static void main(String[] args) {
        String s = "barfoothefoobarman";
        String[] words = {"foo","bar"};
        Solution solution = new Solution();
        System.out.println(solution.findSubstring(s, words));
    }
}
