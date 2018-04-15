import java.io.*;
import java.util.*;

public class Solution {
    static boolean isAnagram(String a, String b) {
        char[] A = a.toLowerCase().toCharArray();
        char[] B = b.toLowerCase().toCharArray();
        Arrays.sort(A);
        Arrays.sort(B);
        String sortedA = new String(A);
        String sortedB = new String(B);
        return sortedA.equals(sortedB);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
