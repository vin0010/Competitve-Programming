//Distance in B(S)T
#include<iostream>
using namespace std;
struct node{
	node *right;
	node *left;
	int value;
}*root;
node* insert(node *i, int v){
	if(i){
		if(i->value>v)
			i->left = insert(i->left,v);
		else if(i->value<v)
			i->right = insert(i->right,v);
		else
			cout<<"\t Duplicate Value\n";
	}else{
		i= new node;
		i->value=v;
	}
	return i;
}
int distance(node *i, int a, int dist){
	if(i==NULL)
		return 0;
	if(i->value==a){
		return dist;
	}else{
		int left = distance(i->left,a,dist+1);
		int right = distance(i->right,a,dist+1);
		return right>left ? right : left;
	}
}
node* lca(node *i, int a, int b){
	if(i==NULL || i->value == a || i->value == b)
		return i;
	else{
		node *left = lca(i->left,a,b);
		node *right = lca(i->right,a,b);
		return (left && right) ? i : (left?left:right);
	}
}
int distance_node(node *i,  int a, int b){
	return (distance(i, a, 0) + distance(i, b, 0))-2*(distance(i,lca(i,a,b)->value, 0));
}
void inorder(node *i){
	if(i){
		inorder(i->left);
		cout<<"-"<<i->value;
		inorder(i->right);
	}
}
int main(){
	int n,temp;
	cin >>n;
	// int arr[n];
	for(int i=0;i<n;i++){
		cin>>temp;
		root=insert(root, temp);		
	}
	cout<<endl;
	inorder(root);
	cout<<"\nRoot:"<<root->value<<endl;
	cout<<"\n Dist between 100:"<<distance(root, 100,0)<<endl;
	// cout<<"\n Dist between 25:"<<distance(root, 25,0)<<endl;
	cout<<"\n LCA of 100 and 300:"<<lca(root, 100,300)->value<<endl;
	cout<<"\n LCA of 100 and 184:"<<lca(root, 100,184)->value<<endl;
	cout<<"\n LCA of 137 and 184:"<<lca(root, 137,184)->value<<endl;
	cout<<"\n Ditance between 137 and 184:"<<distance_node(root, 137,184);
	return 0;
}