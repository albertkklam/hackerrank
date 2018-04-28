import java.util.*;
class Solution {

   public static void main(String []argh) {
      Scanner sc = new Scanner(System.in);
      while (sc.hasNext()) {
         String input = sc.next();
         checkBalance(input);
     }
 }

 public static void checkBalance(String input) {
    Stack stack = new Stack();
    int index = 0;
    Boolean balanced = true;
    while(index < input.length() && balanced) {
        String symbol = Character.toString(input.charAt(index));
        if(symbol.equals("(") || symbol.equals("[") || symbol.equals("{")) {
            stack.push(symbol);
        } else {
            if(stack.empty()) {
                balanced = false;
            } else {
                stack.pop();
            }
        }
        index++;
      }
      if(balanced && stack.empty()) {
        System.out.println(true);
      } else {
        System.out.println(false);
      }
  }
}
