package contests.goldmansachs;

import java.util.Scanner;

public class BankAccounts {
	static void getDetails(int arr[], int k, int x,int d){
		float sum=0;
		for(int i: arr){
			sum+=(float)Math.max(k, ((x*i)/100));
		}
		if(sum>d){
			System.out.println("upfront");
		}else if(sum<d){
			System.out.println("fee");
		}else{
			System.out.println("fee");
		}
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int q = in.nextInt();
		for(int j=0;j<q;j++){
			int n = in.nextInt();
			int k = in.nextInt();
			int x = in.nextInt();
			int d = in.nextInt();
			int arr[] = new int[n];
			for(int i=0;i<n ; i++){
				arr[i]=in.nextInt();
			}
			getDetails(arr, k, x, d);
//			for(int i=0;i<n;i++){
//				System.out.print("--"+arr[i]);
//			}
		}
		in.close();
	}

}