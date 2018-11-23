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

public class MedianUpdates {
	class MyComparator implements Comparator<Integer> {

		@Override
		public int compare(Integer o1, Integer o2) {
			return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
		}
	}

	private static void printMedian(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		int l = leftHeap.size();
		int r = rightHeap.size();
//		System.out.println(l + "----" + r);
		if (l == 0 && r == 0) {
			System.out.println("Wrong!");
		} else {
			if ((l + r) % 2 == 0) {
				System.out.println(leftHeap.peek() + "--------" + rightHeap.peek());
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
		PriorityQueue<Integer> leftHeap = new PriorityQueue<>();
		MedianUpdates medianUpdates = new MedianUpdates();
		Comparator<Integer> comparator = medianUpdates.new MyComparator();
		PriorityQueue<Integer> rightHeap = new PriorityQueue<>(comparator);
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
//		checkBalacnce();
//		System.exit(0);
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
//			System.out.println("-->" + s[i] + ":" + x[i]);
		}
		median(x, s);
		in.close();

	}

	private static void checkBalacnce() {
		// TODO Auto-generated method stub
		MedianUpdates medianUpdates = new MedianUpdates();
		Comparator<Integer> comparator = medianUpdates.new MyComparator();
		PriorityQueue<Integer> queue2 = new PriorityQueue<>();
		PriorityQueue<Integer> queue1 = new PriorityQueue<Integer>(comparator);
		queue2.add(10);
		queue2.add(13);
		queue2.add(17);
		queue2.add(19);
		queue2.add(100);
		queue2.add(90);
		queue2.add(90);
		System.out.println(queue2);
		System.out.println(queue2.remove(200));
		System.out.println(queue2);

//		queue1.add(10);
//		queue1.add(11);
//		queue1.add(3);
//		queue1.add(4);
//		queue1.add(7);
//		queue1.add(2);
//		queue1.add(14);
		balanceHeap(queue1, queue2);
		System.out.println("Queue1:--->" + queue1);
		System.out.println("Queue2:--->" + queue2);
//		while (!queue2.isEmpty()) {
//			System.out.println(queue2.poll());
//		}
	}
}
