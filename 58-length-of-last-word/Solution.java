public class Solution {

	public int lengthOfLastWord(String s) {
		int len = 0;

		for (int i = s.length() - 1; i >= 0; i--) {
			if (s.charAt(i) == ' ') {
				if (len > 0) {
					break;
				}
			} else {
				len++;
			}
		}

		return len;
  	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.lengthOfLastWord("a"));
	}
}
