package practice;

import java.util.Scanner;

//https://www.hackerrank.com/challenges/cavity-map
public class CavityMap {
//convert or process with strings?
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
        String[] grid = new String[n];
        for(int i=0; i < n; i++){
            grid[i] = in.next();
        }
//        int arr[][] = new int[n][n];
        for(int i=0;i<n;i++){
        	
        }
        for(int grid_i=0; grid_i < n; grid_i++){
            System.out.println(grid[grid_i]);
        }
		in.close();
	}
}
/*
4
1112
1912
1892
1234

output
1112
1X12
18X2
1234
*/