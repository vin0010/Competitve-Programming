package com.codex.hackerrank;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Test {
	static void median(String a[], long x[]) {
		List<Long> nums = new ArrayList<Long>();
		for (int i = 0; i < a.length; i++) {
			updateMedian(a[i], x[i], nums);
		}

	}

	public static void updateMedian(String str, long num, List<Long> nums) {
		int index = Collections.binarySearch(nums, num);
		if (str.equalsIgnoreCase("r")) {
			if (index < 0) {
				System.out.println("Wrong!");
				return;
			} else
				nums.remove(index);
		} else {
			if (index < 0)
				nums.add(-index - 1, num);
			else
				nums.add(index, num);
		}
		if (nums.size() == 0)
			System.out.println("Wrong!");
		else if (nums.size() % 2 == 0) {
			long median = (nums.get(nums.size() / 2) + nums.get(nums.size() / 2 - 1));
			if (median % 2 != 0) {
				System.out.printf("%.1f", median / 2.0);
				System.out.println();
			} else
				System.out.println(median / 2);
		} else
			System.out.println(nums.get((nums.size() - 1) / 2));
	}

	public static void main(String args[]) {
//		final String A="<<<<>";
//		final String A="][";
		final String A="([<>]()}[";
		 char[] chararr =A.toCharArray();
	        ArrayList<Character> arr = new ArrayList<Character>(10);
	        Map<Character, Character> map = new HashMap<>();
	        map.put('<','>');
	        map.put('(',')');
	        map.put('{','}');
	        map.put('[',']');
	        
	         map.put('>','<');
	        map.put(')','(');
	        map.put('}','{');
	        map.put(']','[');
	        // System.out.println(":1:"+chararr[2]);
	        int count =0;
	        int currentMax=0;
	        int max=0;
	        for (Character c : chararr) {
	        	 if (arr.isEmpty()){
	                 count+=1;
	                 arr.add(c);
	             } else{
	            	 if (c.equals(map.get(arr.get(count-1)))) {
	                     currentMax+=2;
	                     arr.remove(count-1);
	                     count-=1;
	                 }else{
	                     currentMax =0;
	                     arr.add(c);
	                     count+=1;
	                 }
	             }
	            max = Math.max(max,currentMax);
	            System.out.print("-->"+c);
	        }
	        System.out.println(max);
	}
}
