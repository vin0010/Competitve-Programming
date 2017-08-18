package practice;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class BeautifulPairs {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for (int j = 0; j < n; j++) {
			// get n p m
			a[j] = in.nextInt();
		}
		for (int j = 0; j < n; j++) {
			b[j] = in.nextInt();
		}
		computePosiibility(a, b, n);
		in.close();
	}

	private static void computePosiibility(int[] a, int[] b, int n) {
		Map<Integer, Integer> aMap = mappify(a);
		Map<Integer, Integer> bMap = mappify(b);
		int count = 0;
		for (int i : aMap.keySet()) {
			if (bMap.containsKey(i)) {
				System.out.println(i + " :"+aMap.get(i)+"   B:"+bMap.get(i));
				if (aMap.get(i) == bMap.get(i)) {
					count += aMap.get(i);
				} else {
					System.out.println("Here--------");
					if(aMap.get(i)> bMap.get(i)){
						
					}else{
						
					}
					count +=(minOf(aMap.get(i), bMap.get(i)));
//					if (aMap.get(i) > bMap.get(i)) {
//						count += (bMap.get(i));
//					}
				}
				// count+=(minOf(aMap.get(i),bMap.get(i))*2);
			}else{
				System.out.println("A:"+aMap.get(i)+"   B:"+null);
			}
		}
		if (count==n) {
			System.out.println(count-1);
		} else {
			System.out.println(count+1);
		}
		// eliminate=eliminate*2;

	}

	private static int minOf(Integer a, Integer b) {
		return a>b?b:a;
	}

	private static Map<Integer, Integer> mappify(int[] mids) {
		Map<Integer, Integer> pMap = new HashMap<Integer, Integer>();
		for (int m : mids) {
			if (pMap.containsKey(m)) {
				pMap.put(m, pMap.get(m) + 1);
			} else {
				pMap.put(m, 1);
			}
		}
		return pMap;
	}
}

