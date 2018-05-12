import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        BitSet b1 = new BitSet(n);
        BitSet b2 = new BitSet(n);
        BitSet[] bitset = new BitSet[3];
        bitset[1] = b1;
        bitset[2] = b2;

        for(int i = 0; i < m; i++) {
            String op = in.next();
            int x = in.nextInt();
            int y = in.nextInt();

            switch (op) {
            case "AND":
              bitset[x].and(bitset[y]);
              break;
            case "OR":
              bitset[x].or(bitset[y]);
              break;
            case "XOR":
              bitset[x].xor(bitset[y]);
              break;
            case "FLIP":
              bitset[x].flip(y);
              break;
            case "SET":
              bitset[x].set(y);
          }
          System.out.printf("%d %d%n", b1.cardinality(), b2.cardinality());
        }
    }
}
