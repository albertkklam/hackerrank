import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static Scanner in = new Scanner(System.in);
    static int B = in.nextInt();
    static int H = in.nextInt();
    static boolean flag = (B > 0) && (H > 0);
    static { 
        try {
            if(!flag) {
                throw new Exception("Breadth and height must be positive");
            }
        } catch(Exception e) {
            System.out.println(e);
        }
    }

public static void main(String[] args) {
        if(flag) {
            int area = B * H;
            System.out.print(area);
        }
    }
}

