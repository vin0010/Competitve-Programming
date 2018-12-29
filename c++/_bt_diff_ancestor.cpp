//Maximum difference between node and its ancestor in Binary Tree
//http://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/
#include<iostream>
#include<limits>
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
int minOf(int a, int b){
	return a<b?a:b;
}
int max_diff_tree(node *i, int *current_max){
	if(i){
		if(i->left && i->right){
			int currentMin=minOf(max_diff_tree(i->left, current_max), max_diff_tree(i->right, current_max));
			int temp = i->value - currentMin;
			if(temp > *current_max){
				*current_max = temp;
			}
			return currentMin;
		}else if(i->left || i->right){
			return i->left?max_diff_tree(i->left, current_max):max_diff_tree(i->right, current_max);
		}else{
			return i->value;
		}
	}
	return std::numeric_limits<int>::max();
}
int main(){
	int max_diff=0;
	root=newNode(8);
	root->left = newNode(3);
	root->right = newNode(10);
	root->right->right = newNode(14);
	// root->right->right->right = newNode(2);
	root->right->right->left = newNode(13);
	root->left->left = newNode(1);
	root->left->right = newNode(6);
	root->left->right->left = newNode(4);
	root->left->right->right = newNode(7);
	cout<<endl;
	cout<<"\n Min is: "<<max_diff_tree(root, &max_diff);
	cout<<"\nSol is:"<<max_diff;
	cout<<endl;
	// preorder(root);
	cout<<endl;
}