package com.codex.hackerrank;

import java.util.ArrayList;
import java.util.Scanner;
//import java.util.TreeMap;

public class MaximumIndexProductSum {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			list.add(scanner.nextInt());
		}
		preparemap(list);
		scanner.close();
	}

	private static void preparemap(ArrayList<Integer> list) {/*
		TreeMap<Integer, Integer> leftMap = new TreeMap<>();
		TreeMap<Integer, Integer> rightMap = new TreeMap<>();
//		int left = 0, right = list.size() - 1;
//		int max = 0;
//		while (left < list.size() && right > -1) {
//			
//		}
		for (int i = 0; i < list.size(); i++) {
			leftMap.put(list.get(i), i);
		}
		System.out.println(leftMap);
	*/}
}
