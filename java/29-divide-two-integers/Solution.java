import java.util.Scanner;

public class Solution {


    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        if (dividend == divisor) {
            return 1;
        }
        
		boolean positive = (dividend < 0) ^ (divisor < 0) ? false : true;
        int result = 0;
		long x = Math.abs((long) dividend);
        long y = Math.abs((long) divisor);
        
		while (x >= y) {
            x -= y;
            result++;
        }
        
        return positive ? result : -result;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String dividend = scanner.next();
            String divisor = scanner.next();
            System.out.println(dividend + " / " + divisor + " is " + solution.divide(Integer.parseInt(dividend), Integer.parseInt(divisor)));
        }
        scanner.close();
    }   
}