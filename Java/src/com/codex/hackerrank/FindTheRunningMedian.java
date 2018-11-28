package com.codex.hackerrank;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class FindTheRunningMedian {
	public static void main(String[] args) {
		PriorityQueue<Integer> rightHeap = new PriorityQueue<Integer>();
		PriorityQueue<Integer> leftHeap = new PriorityQueue<Integer>(100, new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o1 > o2 ? -1 : (o1 == o2 ? 0 : 1);
			}
		});
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		for (int i = 0; i < n; i++) {
			int number = in.nextInt();
			printMedian(number, leftHeap, rightHeap);
		}
		in.close();
	}

	private static void printMedian(int number, PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		if (!leftHeap.isEmpty() && leftHeap.peek() > number) {
			leftHeap.add(number);
		} else {
			rightHeap.add(number);
		}
		balanceHeap(leftHeap, rightHeap);
	}

	private static void balanceHeap(PriorityQueue<Integer> leftHeap, PriorityQueue<Integer> rightHeap) {
		int l = leftHeap.size();
		int r = rightHeap.size();
		if (r > l) {
			while (rightHeap.size() - leftHeap.size() > 1) {
				leftHeap.add(rightHeap.poll());
			}
		} else {
			while (leftHeap.size() - rightHeap.size() > 1) {
				rightHeap.add(leftHeap.poll());
			}
		}
		l = leftHeap.size();
		r = rightHeap.size();
		if (l == r) {
			System.out.println(((double) leftHeap.peek() + (double) rightHeap.peek()) / 2);
		} else if (l > r) {
			System.out.println((double) leftHeap.peek());
		} else {
			System.out.println((double) rightHeap.peek());
		}
	}
}
