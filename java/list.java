import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        LinkedList<Integer> list = new LinkedList<Integer>();
        for(int i = 0; i < n; i++) {
            list.add(in.nextInt());
        }
        int q = in.nextInt();
        while(q-- > 0) {
            String command = in.next();
            if(command.equals("Insert")) {
                int x = in.nextInt();
                int y = in.nextInt();
                list.add(x,y);
            } else {
                int x = in.nextInt();
                list.remove(x);
            }
        }
        for (Integer num : list) {
            System.out.print(num + " ");
        }
    }
}
