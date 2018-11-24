package com.codex.hackerrank;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
/*
 *     Problem : https://www.hackerrank.com/challenges/median/problem
 *     Solution:
 *             Key point is we don't have to sort the items every time since we just want the median.
 *             
 *             Keep left heap(max heap) and right heap(min heap).  
 *             Center element required? - for starters I dont keep center element
 *             
 *                 7  
                r 1  
                a 1  
                a 2  
                a 1  
                r 1  
                r 2  
                r 1  
 * 
 */

public class Solution {
	private static void printMedian(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap,
			boolean isNotRemoved) {
//		System.out.println("Left:" + leftHeap);
//		System.out.println("Right:" + rightHeap);
		int l = leftHeap.size();
		int r = rightHeap.size();
		if (l == 0 && r == 0 || isNotRemoved) {
			System.out.println("Wrong!");
		} else {
			if (l == r) {
				long left = leftHeap.peek();
				long right = rightHeap.peek();
				
				if ((left+right)%2==0) {
					long sum = left + right;
					System.out.println(sum / 2);
				}else {
					double sum = (double) leftHeap.peek() + (double) rightHeap.peek();
					System.out.printf("%.1f", (sum)/2);
					System.out.println();
				}
			} else if (l > r) {
				System.out.println(leftHeap.peek());
			} else {
				System.out.println(rightHeap.peek());
			}
		}

	}

	private static void balanceHeap(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		int l = leftHeap.size();
		int r = rightHeap.size();
		if (l == r) {
			return;
		}
		if (r > l) {
			while (rightHeap.size() - leftHeap.size() > 1) {
				leftHeap.add(rightHeap.poll());
			}
		} else {
			while (leftHeap.size() - rightHeap.size() > 1) {
				rightHeap.add(leftHeap.poll());
			}
		}
	}

	private static void median(int number, String operation, PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
				// PriorityQueue<Integer> rightHeap = new PriorityQueue<Integer>(comparator);
			boolean isNotRemoved = false;
			if (operation.equals("r")) {
				if (!leftHeap.remove(number)) {
					if (!rightHeap.remove(number))
						isNotRemoved = true;
				}
			} else if (operation.equals("a")) {
				//add logic to add it to either left or right
				if(leftHeap.isEmpty() && rightHeap.isEmpty() || (leftHeap.peek() != null && leftHeap.peek() < number)) {
					leftHeap.add(number);
				} else{
					rightHeap.add(number);
				}
			}
			balanceHeap(leftHeap, rightHeap);
//			System.out.println("---------------------\nAfter :" + operations[i] + " " + numbers[i]);
			printMedian(leftHeap, rightHeap, isNotRemoved);
	}

	public static void main(String[] args) {
		PriorityQueue<Integer> leftHeap = new PriorityQueue<Integer>();
		PriorityQueue<Integer> rightHeap = new PriorityQueue<Integer>(100, new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
			}
		});

		Scanner in = new Scanner(System.in);
		int N;
		N = in.nextInt();

		for (int i = 0; i < N; i++) {
			String operation = in.next();
			int number = in.nextInt();
			median(number, operation, leftHeap, rightHeap);
		}
		in.close();
	}
	/*
	 * 15 a -2147483648 a -2147483648 a -2147483647 r -2147483648 a 2147483647 r
	 * -2147483648 a 10 a 10 a 10 r 10 r 10 r 10 r 100 r 100 r 100 -2147483648
	 * -2147483648 -2147483648 -2.14748365E9 -2147483647 0 10 10 10 10 10 0 0 0 0
	 */
	/*
	 5
a -2147483648
a -2147483648
a -2147483647
r -2147483648
a 2147483647
	 
	 */

}
