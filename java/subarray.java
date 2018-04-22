import java.io.*;
import java.util.*;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        in.close();

        int l = a.length;
        int[] sums = new int[l * (l+1) / 2];
        int index = 0;
        for(int i = 0; i < l; i++) {
            for(int j = i; j < l; j++) {
                sums[index] = IntStream.range(i,j+1).map(k -> a[k]).sum();
                index++;
            }
        }
        int count = 0;
        for(int i = 0; i < sums.length; i++) {
            if(sums[i] < 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
