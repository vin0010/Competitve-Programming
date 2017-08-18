//https://www.hackerrank.com/challenges/string-reduction
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main ()
{
	int testCases,a,b,c,mid,big,small,t;
	cin >> testCases;
	string s,str[testCases];
	int arrA[testCases],arrB[testCases],arrC[testCases],tot[testCases];
	for(int i=0; i<testCases; i++){
		cin >> s;
		arrA[i]=count(s.begin(), s.end(), 'a');
		arrB[i]=count(s.begin(), s.end(), 'b');
		arrC[i]=count(s.begin(), s.end(), 'c');
		// cout << "\nValues:\n";
		tot[i]=s.length();
		// cout <<  arrA[i]<< "\n";
		// cout << arrB[i] << "\n";
		// cout << arrC[i] << "\n";
	}
	for(int i=0; i<testCases; i++){
		a=arrA[i];
		b=arrB[i];
		c=arrC[i];
		big = a > b ? (a > c ? a : c) : (b > c ? b : c) ;
		small = a < b ? (a < c ? a : c) : (b < c ? b : c) ;
		mid = tot[i]-(big+small);
		// cout << "\nBig" << big << "		small" << small << "	mid" << mid <<"\n";
		if(small==0 && mid==0){
			cout << big << "\n";
			continue;
		}
		a=big-small;
		b=mid-small;
		c=0;//small-small;
		// cout << "\nA:" << a << "	B:" << b << "	C:" << c <<"\n";
		//if(a){ if either of them equal then different
		//}
			if(b==0){
				if(a%2==0)
					cout << "2\n";
				else
					cout << "1\n";
				continue;
			}
		if(a==b){
			if(a%2==0)
				cout << "2\n";
			else
				cout << "1\n";
			continue;
		}
		if(b==1){
			cout << "1\n";
			continue;
		}
		while(1){
			// cout << "Comingg!!!A:" << a << "	B:" << b;
			if(a-b>0){
				a=a-b;
				if(a<b){
					t=b;
					b=a;
					a=t;
				}
				// cout << "\nInganaA:" << a << "	B:" << b << "	C:" << c <<"\n";
				if(a==1){
					cout << "1\n";
					break;
				}
			}
			else{
				if(b==1 || a==1){
					cout << "1\n";
					break;
				}
				else{
					if(a%2==0)
						cout << "2\n";
					else
						cout << "1\n";
						break;
				}
			}
		}
	}
	
return 0;
}
//baaaaccabbabcbacabbcbcababbbaaacaacaacbbbbacbaccbbccaabbbaccbc