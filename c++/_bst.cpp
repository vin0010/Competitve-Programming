//BST
#include<iostream>
using namespace std;
struct node{
	node *left;
	node *right;
	int value;
}*root;
node* insert(node *i, int v){
	if(i){
		if(i->value<v){
			i->right = insert(i->right,v);
		}else if(i->value>v){
			i->left = insert(i->left,v);
		}else{
			//duplicate vallue
		}
	}else{
		i=new node;
		i->value = v;
	}
	return i;
}
node* maxleft(node *i){
	while(i->right){
		i=i->right;
	}
	// cout << "\tReturning :"<<i->value;
	return i;
}
node* delete_node(node *i, int v){
	if(i){
		if(i->value<v){
			i->right = delete_node(i->right,v);
		}else if(i->value>v){
			i->left = delete_node(i->left,v);
		}else{ //node to be deleted
			cout << "\nGoing to delete::"<<v;
			if(i->right && i->left){
				node *temp = maxleft(i->left);
				cout << "\tMax Left:"<<temp->value<<"\n";
				i->value = temp->value;
				// temp = delete_node(temp, temp->value); //checlk if delete is happening properly without tree cut
				i->left = delete_node(i->left, temp->value);
				// temp = delete_node(temp, temp->value);
				// root = delete_node(root, temp->value); //checlk if delete is happening properly without tree cut
			}else if(i->right){
				cout<<"\n No Left";
				i=i->right;
			}else if(i->left){
				cout<<"\n No Right";
				i=i->left;
			}else{
				cout<<"\n Empty Leaves";
				delete(i);
				return NULL;
			}
		}
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
int main(){
	//44 200 100 300 50 150 250 400 25 75 125 175 225 275 350 450 12 37 63 87 113 137 163 187 224 223 222 219 280 285 290 299 282 500 425 426 430 439 444 186 185 184 38 39 40
	int n,temp;
	cin >>n;
	// int arr[n];
	for(int i=0;i<n;i++){
		cin>>temp;
		root=insert(root, temp);		
	}
	cout<<"\nRoot:"<<root->value<<endl;
	// cout<<"\nRoot:"<<root->left->value<<endl;
	// cout<<"\nRoot:"<<root->right->value<<endl;
	inorder(root);
	cout<<	endl;
	root=delete_node(root,184);
	root=delete_node(root,150);
	root=delete_node(root,200);
	cout<<	endl;
	inorder(root);
	cout<<	endl;
}