import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> allLists = new ArrayList<ArrayList<Integer>>();
        int n = in.nextInt();
        in.nextLine();
        for(int i = 0; i < n; i++) {
            ArrayList<Integer> list = new ArrayList<Integer>();
            int m = in.nextInt();
            if(m > 0) {
                for(int j = 0; j < m; j++) {
                    list.add(in.nextInt());
                }
            }
            allLists.add(list);
            in.nextLine();
        }
        int q = in.nextInt();
        for(int k = 0; k < q; k++) {
            try {
                int result = allLists.get(in.nextInt() - 1).get(in.nextInt() - 1);
                System.out.println(result);
                in.nextLine();
            } catch(IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
                in.nextLine();
            }
        }
    }
}
