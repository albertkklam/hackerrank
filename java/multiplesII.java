import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for(int j=1; j<=n; j++) {
                System.out.printf("%d ",  a - b * (1 - (int) Math.pow(2, j)));
            }
            System.out.println();
        }
        in.close();
    }
}
