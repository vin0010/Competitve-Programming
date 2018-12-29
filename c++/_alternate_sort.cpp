#include<iostream>
using namespace std;

void process_array(int *arr, int n){
	int temp=arr[0],index=0,mid=n/2;
	for(int i=0;i<n;i++){
		if(index<=mid-1) {
			// cout<<"\nIndex now: "<<index;
			int next=2*(index+1)-1;
			// cout<<"\tNext now: "<<next;
			int x = temp; 
			temp=arr[next];
			arr[next]=x;
			// cout<<"\tTemp now: "<<temp;
			// cout<<"\tWrite   : "<<arr[next];
			// cout<<"\tCurnt bef: "<<arr[index];
			index=next;
			// cout<<"\tIndex now: "<<index;
			// cout<<"\tCurnt now: "<<arr[index];
			// break;
		}else{
			// cout<<"\nComing here: "<<index;
			// int next=2*(n-index+1);
			// int x = temp; 
			// temp=arr[next];
			// arr[next]=x;
			// index=next;
		}
	}
	cout<<"\nProcess_array:"<<temp<<endl;
}
void print_array(int *a,int n){
	cout<<"\nArray:"<<endl;
	for(int i=0;i<n;i++){
		cout<<a[i]<<"-";
	}
}
int main(){
	int arr[8]={1,2,3,4,5,6,7,8};
	cout<<"Begins:"<<endl;
	process_array(arr,8);
	print_array(arr,8);
}

// 1-2-3-4-5-6-7-8-9
// 9-1-8-2-7-3-6-4-5

// 1-2-3-4-5-6-7-8
// 8-1-7-2-6-3-5-4