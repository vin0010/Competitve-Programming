//Diameter of a binary tree
//http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
//http://ideone.com/TeNFP1
#include<iostream>
using namespace std;
struct node{
	node *left;
	node *right;
	int value;
}*root;
node* newNode(int value){
	node *i = new node;
	i->value=value;
	return i;
}
int diameter(node *i, int *max_depth){
	if(i){
		cout<<"\nComing";
		int left= diameter(i->left, max_depth);
		int right= diameter(i->right, max_depth);
		if(left+right+1>*max_depth){
			*max_depth=left+right+1;
		}
		// cout<<"\n Height of "<<;
		return left>right ? left+1 : right+1;
	}
	return 0;
}
void preorder(node *i){
	if(i){
		preorder(i->left);
		preorder(i->right);
		cout<<"-"<<i->value;
	}
}
int main(){
	int max_depth=0;
	root=newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->right->right = newNode(13);
	root->right->left = newNode(12);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	cout<<endl;
	cout<<diameter(root, &max_depth);
	cout<<"\nDiameter is:"<<max_depth;
	cout<<endl;
	preorder(root);
	cout<<endl;
}