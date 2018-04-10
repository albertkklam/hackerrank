import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 0;
        while(sc.hasNext()) {
            String s = sc.nextLine();
            i++;
            System.out.printf("%d %s\n", i, s);
        }
    }
}
