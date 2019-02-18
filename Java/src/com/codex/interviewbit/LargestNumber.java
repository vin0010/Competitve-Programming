package com.codex.interviewbit;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * @author Vinoth.Gopu https://www.interviewbit.com/problems/largest-number/
 * 
 *         get all digits starts with maximum number
 * 
 */
public class LargestNumber {
	public static String largestNumber(final List<Integer> A) {
		

		TreeMap<Integer, TreeSet<Integer>> map = new TreeMap<>(Collections.reverseOrder());

		for (int i : A) {
			int firstDigit = Integer.parseInt(new String(i + "").charAt(0) + "");

			System.out.println(i + "--" + new String(i + "").charAt(0));
			if (!map.containsKey(firstDigit)) {
				TreeSet<Integer> treeSetObj = new TreeSet<Integer>(new Comparator<Integer>() {
					@Override
					public int compare(Integer i1, Integer i2) {
						return i2.compareTo(i1);
					}

				});
				treeSetObj.add(i);
				map.put(firstDigit, treeSetObj);
			}
			else
				map.get(firstDigit).add(i);
		}
		System.out.println(map);
		return "";
	}

	public static void main(String[] args) {
		largestNumber(new ArrayList<>(Arrays.asList(10, 122, 1240,112, 20, 224, 3099,39, 388)));
	}
}
