import java.io.*;
import java.util.*;
import org.apache.commons.lang3.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        System.out.println(A.length() + B.length());
        if(A.compareTo(B) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        System.out.println(StringUtils.capitalize(A) + " " + StringUtils.capitalize(B));

    }
}
