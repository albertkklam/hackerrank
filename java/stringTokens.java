import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        if (s.trim().length() == 0 || s.trim().length() >= 400000) {
            System.out.println(0);
            return;
        }
        String[] arr = s.trim().split("[ !,?.\\_'@]+");
        System.out.println(arr.length);
        for(String string: arr) {
            System.out.println(string);
        }
        scan.close();
    }
}
