package practice;

import java.util.Scanner;
import java.util.TreeMap;

public class PickingNumbers {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
		int temp =0;
		for(int i=0;i<n;i++){
			temp = in.nextInt();
			if(map.containsKey(temp)){
				map.put(temp, map.get(temp)+1);
			}else{
				map.put(temp, 1);
			}
		}
		int max=0;
		//System.out.println(map);
		for(int i : map.keySet()){
			Integer next = map.higherKey(i);
			if(next!=null){
				int diff =Math.abs(i-next);
				if(diff<=1){
					max=Math.max(max, map.get(i)+map.get(map.higherKey(i)));	
				}
				//System.out.println("Max:"+max+"   next"+Math.abs(map.get(i)-next));
				
			}
//			System.out.println("Current key : "+i+"  next key:"+map.higherKey(i));
		}
		System.out.println(max);
		in.close();
	}
}
