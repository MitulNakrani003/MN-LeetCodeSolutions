class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0)
        {
            return 0;
        }
        HashMap<Character, Integer> freqArr = new HashMap<>();
        int left = 0, right = 0;
        int globalmax = 0, localmax = 0;
        while(right != (s.length()))
        {
            char currElement = s.charAt(right);
            if (freqArr.containsKey(currElement))
            {
                int newleft = freqArr.get(currElement) + 1;
                while (left < newleft)
                {
                    freqArr.remove(s.charAt(left));
                    left++;
                }
                left = newleft;
                localmax = right - left;
            }
            freqArr.put(currElement,right);
            localmax++;
            globalmax = Math.max(globalmax, localmax);
            System.out.println(localmax+" "+globalmax+" "+left+" "+right);
            right++;
        }
        return globalmax;
    }
}