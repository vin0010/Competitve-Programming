package practice;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class FraudulentActivityNotifications {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
//		int k = in.nextInt();
		int[] arr = new int[n];
//		for (int j = 0; j < n; j++) {
//			arr[j] = in.nextInt();
//		}
		for(int x=0;x<n;x++){
			arr[x]=in.nextInt();
		}
		PriorityQueue<Integer> leftMaxQ = new PriorityQueue<Integer>(Collections.reverseOrder());
		PriorityQueue<Integer> rightMinQ = new PriorityQueue<Integer>();
		for (int i = 0; i < n; i++) {
			System.out.println("Coming"+n);
			insert(leftMaxQ, rightMinQ, arr[i]);
			balance(leftMaxQ, rightMinQ, arr[i]);
//			System.out.println("Left:"+leftMaxQ);
//			System.out.println("Right:"+rightMinQ);
		}
//		for (int i = 0; i < k; i++) {
//			insert(leftMaxQ, rightMinQ, arr[i]);
//			balance(leftMaxQ, rightMinQ, arr[i]);
//		}
		in.close();
	}

	private static void insert(PriorityQueue<Integer> leftMaxQ, PriorityQueue<Integer> rightMinQ, int i) {
		if(!leftMaxQ.isEmpty()){
			int left = leftMaxQ.peek();
			if (leftMaxQ.isEmpty() && rightMinQ.isEmpty()) {
				leftMaxQ.add(i);
			} else if (left < i) {
				leftMaxQ.add(i);
			} else if (left > i) {
				rightMinQ.add(i);
			}	
		}else{
			leftMaxQ.add(i);
		}
		
	}

	private static void balance(PriorityQueue<Integer> leftMaxQ, PriorityQueue<Integer> rightMinQ, int i) {
		while (!(leftMaxQ.size() == rightMinQ.size() + 1 || leftMaxQ.size() == rightMinQ.size())) {
			if(leftMaxQ.size()>rightMinQ.size()){
				rightMinQ.add(leftMaxQ.poll());
			}else{
				if(!rightMinQ.isEmpty()){
					leftMaxQ.add(rightMinQ.poll());				
				}else{
					break;
				}	
			}
		}
	}
	//10 
	//2 3 4 7 9 6 8 3 1 10 
}
