//Test file in CPP
#include<iostream>
using namespace std;
struct node{
	node *next;
	int value;
}*root;

int main(){
	root = new node;
	// root->value =100;
	if(root != NULL){
		cout<<"\nNot empty";
	}else{
		cout<<"\nEmpty";
	}

	cout<<endl;
	return 0;
}