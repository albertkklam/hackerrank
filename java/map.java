import java.util.*;
import java.io.*;

class Solution {
   public static void main(String []argh) {
      Scanner in = new Scanner(System.in);
      Map map = new HashMap();
      int n = in.nextInt();
      in.nextLine();
      for(int i = 0; i < n; i++) {
         String name = in.nextLine();
         int phone = in.nextInt();
         map.put(name, phone);
         in.nextLine();
      }
      while(in.hasNext()) {
         String s = in.nextLine();
         if(map.get(s) == null){
            System.out.println("Not found");
         } else {
            System.out.print(s + "=" + map.get(s) + "\n");
         }
      }
   }
}
