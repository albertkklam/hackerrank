import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.IntStream;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int i = 0; i < 6; i++) {
            for(int j = 0; j < 6; j++) {
                arr[i][j] = in.nextInt();
            }
        }
        int sums[][] = new int[4][4];
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                sums[i][j] = sumArray(i, j, arr);
            }
        }
        IntStream stream = Arrays.stream(sums).flatMapToInt(Arrays::stream);
        int max = stream.max().getAsInt();
        System.out.println(max);
    }

    public static int sumArray(int i, int j, int[][] array) {
        int sum = 0;
        for(int index_i = i; index_i < i + 3; index_i++) {
            for(int index_j = j; index_j < j + 3; index_j++) {
                sum += array[index_i][index_j];
            }
        }
        sum -= array[i + 1][j];
        sum -= array[i + 1][j + 2];
        return sum;
    }
}
