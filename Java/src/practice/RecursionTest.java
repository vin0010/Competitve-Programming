package practice;

import java.util.HashMap;
import java.util.Map;

public class RecursionTest {
	private static Map<Integer, Integer> map = new HashMap<>();
	
	public static int fibo(int i) {
		System.out.println("Going to find fibo for :"+i);
		if (map.containsKey(i))
			return map.get(i);
//		if(i==0)
//			return 0;
//		else if (i==1)
//			return 1;
		else {
			int result = fibo(i-1)+fibo(i-2);
			map.put(i, result);
			return result;
		}
	}
	
	public static void main(String[] args) {
		//0 1 1 2 3 5 8
		map.put(0, 0);
		map.put(1, 1);
		System.out.println(fibo(6));
	}
}
