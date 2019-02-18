package codeagon;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
public class UglyOrBeautiful {


    static String uglyOrBeautiful(int[] a) {
    	Set<Integer> myset = new HashSet<Integer>();
    	int max=a[0], last=a[0];
    	boolean sortflag=true;
    	for(int i=1;i<a.length;i++){
    		if(last>a[i]){
    			sortflag=false;
    		}
    		max=Math.max(max, a[i]);
    		if(myset.contains(a[i])){
    			return "Ugly";
    		}else{
    			myset.add(a[i]);
    		}
    		last=a[i];
    	}
//    	System.out.println("Max:"+max+" sortflag:"+sortflag);
    	if(max>a.length || sortflag || max>a.length){
    		return "Ugly";
    	}
    	return "Beautiful";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        for(int a0 = 0; a0 < q; a0++){
            int n = in.nextInt();
            int[] a = new int[n];
            for(int a_i = 0; a_i < n; a_i++){
                a[a_i] = in.nextInt();
            }
            String result = uglyOrBeautiful(a);
            System.out.println(result);
        }
        in.close();
    }

}



