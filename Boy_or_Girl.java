//  https://codeforces.com/problemset/problem/236/A
import java.util.*;

public class Boy_or_Girl {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            String s = input.next();

            HashSet<Character> h = new HashSet<>();

            for (int i = 0; i < s.length(); i++) {
                h.add(s.charAt(i));
            }
            if (h.size() % 2 == 0) {
                System.out.println("CHAT WITH HER!");
            } else {
                System.out.println("IGNORE HIM!");
            }
        }
        
    }
}