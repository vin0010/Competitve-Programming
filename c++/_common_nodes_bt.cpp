//common nodes in two binary trees
#include<iostream>
using namespace std;
struct node{
	node *left;
	node *right;
	int value;
}*t1, *t2;
node* insert(node *i, int v){
	if(i){
		if(i->value<v){
			i->right=insert(i->right, v);
		}else if(i->value>v){
			i->left =  insert(i->left, v);
		}else{
			//duplicate
		}
	}else{
		i= new node;
		i->value=v;
		return i;
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
void inorder1(node *i, node *j){
	if(i || j){
		if(i && j) inorder(i->left, j->left);
		if(i && !j) inorder(i->left, j);
		if(!i && j) inorder(i, j->left);

			if(i->value==j->value){
				cout<<"\n Equal:" <<i->value<<endl;
				my_traversal(i->right, j->right);
			}
			if(i->value > j->value){
				my_traversal(i, j->right);
			}else if(i->value < j->value){
				my_traversal(i->right, j);
			}


		cout<<"-"<<i->value;
		inorder(i->right, );
	}
}
void my_traversal(node *i, node *j){
	if(i && j){
		// cout<<"Coming inside : " << i->value <<" - "<<j->value<<endl;
		if(i->left && j->left){
			cout<<"Coming inside1 : " << i->value <<" - "<<j->value<<endl;
			my_traversal(i->left, j->left);
		}else if(i->left){
			cout<<"Coming inside2 : " << i->value <<" - "<<endl;
			my_traversal(i->left, j);
		}else if(j->left){
			cout<<"Coming inside3 : " << " - "<<j->value<<endl;
			my_traversal(i, j->left);
		}
		else{//Reached left most //logic goes here
			if(i->value==j->value){
				cout<<"\n Equal:" <<i->value<<endl;
				my_traversal(i->right, j->right);
			}
			if(i->value > j->value){
				my_traversal(i, j->right);
			}else if(i->value < j->value){
				my_traversal(i->right, j);
			}
		}
	}
}
int main(){
	int n, temp;
	cin >>n;
	for(int i=0; i<n; i++){
		cin>>temp;
		t1=insert(t1, temp);
	}
	cin>>n;
	for(int i=0; i<n; i++){
		cin>>temp;
		t2=insert(t2, temp);
	}
	cout<<endl;
	cout<<endl<<"Tree 1:";
	inorder(t1);
	cout<<endl<<"Tree 2:";
	inorder(t2);
	cout<<endl;
	my_traversal(t1, t2);
	//7 20 10 30 40 50 25 35 5 35 30 50 25 10 
}