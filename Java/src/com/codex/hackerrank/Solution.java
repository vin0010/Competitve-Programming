package com.codex.hackerrank;

import java.math.BigInteger;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
/*
 * 	Problem : https://www.hackerrank.com/challenges/median/problem
 * 	Solution:
 * 			Key point is we don't have to sort the items every time since we just want the median.
 * 			
 * 			Keep left heap(max heap) and right heap(min heap).  
 * 			Center element required? - for starters I dont keep center element
 * 			
 * 				7  
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
//	class MyComparator implements Comparator<Integer> { // commented to solve hackerrank behavior
//
//		@Override
//		public int compare(Integer o1, Integer o2) {
//			return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
//		}
//	}

	private static void printMedian(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		int l = leftHeap.size();
		int r = rightHeap.size();
//		System.out.println(l + "-----------" + r);
		if (l == 0 && r == 0) {
			System.out.println("Wrong!");
		} else {
			if (l == r) {
				Long sum = (long) leftHeap.peek() + (long)rightHeap.peek();
//				System.out.println("Sum:" + sum);
				if (sum % 2 == 0) {
					System.out.println(sum / 2);
				} else {
					System.out.println((float) sum / 2);
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

	private static void median(int[] numbers, String[] operations) {
		PriorityQueue<Integer> leftHeap = new PriorityQueue<Integer>();
		Solution medianUpdates = new Solution();
//		Comparator<Integer> comparator = medianUpdates.new MyComparator();
		PriorityQueue<Integer> rightHeap = new PriorityQueue<>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
			}
		});
//		PriorityQueue<Integer> rightHeap = new PriorityQueue<Integer>(comparator);
		for (int i = 0; i < numbers.length; i++) {
			if (operations[i].equals("r")) {
				if (!leftHeap.remove(numbers[i])) {
					rightHeap.remove(numbers[i]);
				}
			} else if (operations[i].equals("a")) {
				leftHeap.add(numbers[i]);
			}
			balanceHeap(leftHeap, rightHeap);
			printMedian(leftHeap, rightHeap);
		}
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N;
		N = in.nextInt();

		String s[] = new String[N];
		int x[] = new int[N];

		for (int i = 0; i < N; i++) {
			s[i] = in.next();
			x[i] = in.nextInt();
		}
		median(x, s);
		in.close();
	}
}
