package com.codex.interviewbit;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Vinoth.Gopu https://www.interviewbit.com/problems/largest-number/
 *
 */
public class LargestNumber {
	public static String largestNumber(final List<Integer> A) {
		for (int i : A) {
			System.out.println(i+"--"+new String(i+"").charAt(0));
		}
		return "";
	}
	
	public static void main(String[] args) {
		largestNumber(new ArrayList<>(Arrays.asList(10,20,30)) );
	}
}
