package contests.goldmansachs;

import java.util.Scanner;
import java.util.TreeMap;

public class MaximumStocks {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
		int temp =0;
		for(int i=1;i<=n;i++){
			temp = in.nextInt();
			map.put(temp, i);
		}
		long k = in.nextInt(), sum=0;
//		System.out.println("->"+map);
//		System.out.println("k:"+k);
		for(int stockPrice : map.keySet()){
			if(stockPrice<=k){
				int maxStocks=map.get(stockPrice);
				int t=(int) (k/stockPrice);
				if(t<maxStocks){
					sum+=t;
					k=k-(t*stockPrice);
				}else{
					sum+=maxStocks;
					k=k-(maxStocks*stockPrice);
				}
//				sum+=t;
//				k=k-t;
				//System.out.println("price"+stockPrice+" maxstocks:"+maxStocks+"  k:"+k);
			}else{
				break;
			}
		}
		System.out.println(sum);
		in.close();
	}
}
