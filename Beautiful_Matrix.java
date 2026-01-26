//  https://codeforces.com/problemset/problem/263/A

import java.util.*;

public class Beautiful_Matrix {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int[][] arr = new int[5][5];
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    arr[i][j] = input.nextInt();
                    if (arr[i][j]==1) {
                        System.out.println(Math.abs(i-2) + Math.abs(j-2));
                    }
                }
            }
            
        }
        
    }
}