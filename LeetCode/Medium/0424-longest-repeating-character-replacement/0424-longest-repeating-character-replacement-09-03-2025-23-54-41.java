class Solution {
    public int characterReplacement(String s, int k) {
        int fuel = k;
        int left = 0, right = 0;
        int globMaxFreq = 0, winLength = 0, globMaxWinLength = 0;
        HashMap<Character, Integer> freqArr = new HashMap<>();
        while(right != s.length())
        {
            char current = s.charAt(right);
            if (freqArr.containsKey(current))
            {
                freqArr.put(current, freqArr.get(current)+1);
            }
            else
            {
                freqArr.put(current, 1);
            }
            int currMaxFreq = freqArr.get(current);
            globMaxFreq = Math.max(currMaxFreq,globMaxFreq);
            winLength = right - left + 1;
            int extraNeededFuel = winLength - globMaxFreq;
            if(extraNeededFuel > fuel)
            {
                freqArr.put(s.charAt(left), freqArr.get(s.charAt(left))-1);
                left++;
                winLength = right - left + 1;
            }
            globMaxWinLength = Math.max(globMaxWinLength, winLength);
            System.out.println(left+" "+right+" "+winLength+" "+globMaxWinLength+" "+globMaxFreq);
            right++;
        }
        return globMaxWinLength;
    }
}