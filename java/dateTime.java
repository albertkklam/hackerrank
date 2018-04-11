import java.util.Scanner;
import java.util.Calendar;
import java.text.SimpleDateFormat;

public class Solution {

    public static String getDay(String day, String month, String year) {
        Calendar cal = Calendar.getInstance();
        cal.set(Integer.parseInt(year), Integer.parseInt(month) - 1, Integer.parseInt(day));
        SimpleDateFormat dateFormat = new SimpleDateFormat("EEEEE");
        return dateFormat.format(cal.getTime()).toUpperCase();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}
