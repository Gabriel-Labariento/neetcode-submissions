class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        else {
            char[] sString = s.toCharArray();
            char[] tString = t.toCharArray();

            Arrays.sort(sString);
            Arrays.sort(tString);
            return Arrays.equals(sString, tString);
        }
    }
}
