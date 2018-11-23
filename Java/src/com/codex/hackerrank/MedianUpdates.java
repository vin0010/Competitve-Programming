package com.codex.hackerrank;

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
 * 				
 * 
 */

public class MedianUpdates {
	class MyComparator implements Comparator<Integer> {

		@Override
		public int compare(Integer o1, Integer o2) {
			return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
		}
	}

	private static void printMedian(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		
	}

	private static void balanceHeap(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		int l = leftHeap.size();
		int r = rightHeap.size();
	}

	private static void median(int[] numbers, String[] operations) {
		PriorityQueue<Integer> leftHeap = new PriorityQueue<>();
		MedianUpdates medianUpdates = new MedianUpdates();
		Comparator<Integer> comparator = medianUpdates.new MyComparator();
		PriorityQueue<Integer> rightHeap = new PriorityQueue<>(comparator);
		for (int i = 0; i < numbers.length; i++) {
			if (operations[i] == "r") {
				if (leftHeap.isEmpty() && rightHeap.isEmpty()) {
					System.out.println("Wrong!");
				} else if (!leftHeap.isEmpty()) {
					rightHeap.remove(numbers[i]);
					balanceHeap(leftHeap, rightHeap);
				} else {
					leftHeap.remove(numbers[i]);
					balanceHeap(leftHeap, rightHeap);
				}
			} else if (operations[i] == "a") {
				if (leftHeap.isEmpty() && rightHeap.isEmpty()) {
					leftHeap.add(numbers[i]);
					//print here itself
				} else if (!leftHeap.isEmpty()) {
					leftHeap.add(numbers[i]);
					balanceHeap(leftHeap, rightHeap);
				} else {
					rightHeap.add(numbers[i]);
					balanceHeap(leftHeap, rightHeap);
				}
			}
		}
	}

	public static void main(String[] args) {
		PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
		queue.add(10);
		queue.add(13);
		queue.add(11);
		queue.add(19);
		queue.add(100);
		queue.add(90);
//		System.out.println("------>" + queue.peek());
//		while (!queue.isEmpty()) {
//			System.out.println(queue.poll());
//		}
		MedianUpdates medianUpdates = new MedianUpdates();
		Comparator<Integer> comparator = medianUpdates.new MyComparator();

//		System.out.println("----------------");
		PriorityQueue<Integer> queue1 = new PriorityQueue<Integer>(comparator);
		queue1.add(10);
		queue1.add(11);
		queue1.add(3);
		queue1.add(4);
		queue1.add(7);
		queue1.add(2);
		queue1.add(14);
//		System.out.println("---->" + queue1.peek());
//		while (!queue1.isEmpty()) {
//			System.out.println(queue1.poll());
//		}
		Scanner in = new Scanner(System.in);

		int N;
		N = in.nextInt();

		String s[] = new String[N];
		int x[] = new int[N];

		for (int i = 0; i < N; i++) {
			s[i] = in.next();
			x[i] = in.nextInt();
			System.out.println("-->" + s[i] + ":" + x[i]);
		}
//		median(x, s);
		in.close();
	}
}
