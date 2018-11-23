package com.codex.hackerrank;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MedianUpdates {
	class MyComparator implements Comparator<Integer>{

		@Override
		public int compare(Integer o1, Integer o2) {
			return o1>o2 ? -1 : (o1==o2 ? 0 : 1);
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
		System.out.println("------>"+queue.peek());
		while(!queue.isEmpty()) {
			System.out.println(queue.poll());
		}
		MedianUpdates medianUpdates = new MedianUpdates();
		Comparator<Integer> comparator = medianUpdates.new MyComparator();
		
		System.out.println("----------------");
		PriorityQueue<Integer> queue1 = new PriorityQueue<Integer>(comparator);
		queue1.add(10);
		queue1.add(11);
		queue1.add(3);
		queue1.add(4);
		queue1.add(7);
		queue1.add(2);
		queue1.add(14);
		System.out.println("---->"+queue1.peek());
		while(!queue1.isEmpty()) {
			System.out.println(queue1.poll());
		}
		
	}
}
