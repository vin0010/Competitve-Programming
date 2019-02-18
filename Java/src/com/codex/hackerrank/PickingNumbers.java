package com.codex.hackerrank;

/*
 * https://www.hackerrank.com/challenges/picking-numbers/problem
 */
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

public class PickingNumbers {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();

		for (int t = 0; t < n; t++) {
			int x = scanner.nextInt();
			if (map.containsKey(x)) {
				map.put(x, map.get(x) + 1);
			} else {
				map.put(x, 1);
			}
		}
		Set<Integer> set = map.keySet();
		Integer[] list = new Integer[n];
		Integer[] keys = set.toArray(list);
		int max = map.get(keys[0]);
		int currentMax = max;
		for (int i = 1; i < keys.length; i++) {
			if (Math.abs(keys[i] - keys[i + 1]) == 1) {
				currentMax += map.get(keys[i + 1]);
			} else {
				currentMax = map.get(keys[i]);
			}
			max = max(currentMax, max);
		}

		System.out.println(map);
		System.out.println(max);
		scanner.close();
	}

	private static int max(int a, int b) {
		return a > b ? a : b;
	}
}
