//Width of binary tree
//http://ideone.com/FnTICx
//http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
#include<iostream>
#include<map>
using namespace std;
struct node{
	node *left;
	node *right;
	int value;
}*root;
node* insert(node *i, int v){
	if(i){
		if(i->value<v){
			i->right=insert(i->right,v);	
		}else if(i->value>v){
			i->left=insert(i->left,v);	
		}else{
			//duplicate
		}
	}else{
		i = new node;
		i->value= v;
	}
	return i;
}
void inorder(node *i){
	if(i){
		inorder(i->left);
		cout<<"-"<<i->value;
		inorder(i->right);
	}
}
void inordercount(node *i, int *currentmax, int level, map<int ,int> &m){
	if(i){
		cout<<"\nComing";
		inordercount(i->left, currentmax,level+1, m);
		if(m.find(level) != m.end()){
			int temp = m[level]+1;
			m[level] = temp;
			if(temp>*currentmax){
				*currentmax=temp;
			}
		}else{
			m[level] = 1;
		}
		inordercount(i->right, currentmax, level+1, m);
	}
}
int main(){
	int currentmax=0;
	map<int, int> m;
	int temp,n;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>temp;
		root=insert(root,temp);
	}
	// root=insert(root,50);
	// root=insert(root,25);
	// root=insert(root,12);
	// root=insert(root,30);
	// root=insert(root,60);
	// root=insert(root,80);
	// root=insert(root,70);
	// root=insert(root,90);

	cout<<endl;
	inorder(root);
	inordercount(root, &currentmax, 1, m);
	cout<<endl;
	cout<<currentmax;
	cout<<endl;

	// exit(0);
}