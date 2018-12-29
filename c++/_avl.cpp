//AVL tree
#include<iostream>
using namespace std;
struct node{
	node *left;
	node *right;
	int value;
	int height;
}*root;
int max(int a, int b){
	return a>b?a:b;
}
int height(node *i){
	return i ? i->height : 0;
}
int checkBalance(node *i){
	return height(i->left)-height(i->right);
}
int maxLeft(node *i){
	while(i->right){
		i=i->right;
	}
	return i->value;
}
//		  x							 y
//	    /   \					  /     \
//     T1	 y					 x	      z
//			/ \			=> 	   /   \    /   \
//		  T2   z			  T1   T2  T3   T4
//			  / \
//			 T3	T4
node* leftRotate(node *x){
	node *y = x->right;	
	node *T2 = y->left;
	y->left = x;
	x->right = T2;
	//Update height - dont forget to update height of x and y
	x->height = max(height(x->left), height(x->right))+1;
	y->height = max(height(y->left), height(y->right))+1;
	return y;
}
//		  		  x							 y
//	    		/   \					  /     \
//     		   y	 T1					 z	      x
//			  / \			=> 	   	   /   \  	/   \
//		     z   T2			  	      T3   T4  T2   T1
//	       /   \
//		  T3   T4
node* rightRotate(node *x){
	node *y = x->left;
	node *T2 = y->right;
	y->right = x;
	x->left = T2;
	//update height -  dont forget to update modified x and y
	x->height = max(height(x->left), height(x->right))+1;
	y->height = max(height(y->left), height(y->right))+1;
	return y;
}
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
		i->height=1;
		return i;
	}
	//My code to balance the tree or check height factor
	i->height = max(height(i->left), height(i->right))+1;
	int diff = checkBalance(i);

	if(diff < -1 && i->right->value>v){
		// cout<<"\nRL@"<<i->value;
		i->right = rightRotate(i->right);
		i=leftRotate(i);
	}else if(diff<-1 && i->right->value<v){
		// cout<<"\nLL@"<<i->value;
		i=leftRotate(i);
	}else if(diff>1 && i->left->value>v){
		// cout<<"\nRR@"<<i->value;
		i=rightRotate(i);
	}else if(diff>1 && i->left->value<v){
		// cout<<"\nLR@"<<i->value;
		i->left = leftRotate(i->left);
		i=rightRotate(i);
	}
	return i;
}
node* delete_node(node *i, int v){
	if(i){
		if(i->value>v){
			i->left=delete_node(i->left, v);
		}else if(i->value<v){
			i->right = delete_node(i->right, v);
		}else{//to be deleted
			cout<<"\nDelteing:"<<i->value<<endl;
			if(i->left && i->right){
				int temp = maxLeft(i->left);
				i->value = temp;
				i->left = delete_node(i->left, v);
			}else if(i->left){
				i=i->left;
			}else if(i->right){
				i=i->right;
			}else{
				i=NULL;
				return i;
			}
		}
	}

	//update height
	i->height = max(height(i->left), height(i->right))+1;
	//check balance and do rotate if required
	int balance = checkBalance(i);
	// Left Left Case
	if (balance > 1 && checkBalance(root->left) >= 0)
		return rightRotate(root);
	// Left Right Case
	if (balance > 1 && checkBalance(root->left) < 0){
		root->left =  leftRotate(root->left);
		return rightRotate(root);
	}
	// Right Right Case
	if (balance < -1 && checkBalance(root->right) <= 0)
		return leftRotate(root);

	// Right Left Case
	if (balance < -1 && checkBalance(root->right) > 0){
		root->right = rightRotate(root->right);
		return leftRotate(root);
	}
	//update height for modified x and y nodes - it will be done through rotate operations
	return i;
}
int tree_height(node *i){
	if(i==NULL)
		return 0;
	else{
		int left = height(i->left);
		int right = height(i->right);
		return left>right ? left+1 : right +1;
	}
}
void inorder(node *i){
	if(i){
		inorder(i->left);
		cout<<"-"<<i->value;
		inorder(i->right);
	}
}

int main(){
	// int temp,n;
	// // exit(0);
	// cin>>n;
	// for(int i=0;i<n;i++){
	// 	cin>>temp;
	// 	root=insert(root,temp);
	// }
	root = insert(root, 10);
	root = insert(root, 20);
	root = insert(root, 30);
	root = insert(root, 40);
	root = insert(root, 50);
	root = insert(root, 25);
	cout<<endl;
	inorder(root);
	cout<<endl;
	root=delete_node(root, 40);
	root=delete_node(root, 50);
	inorder(root);
	cout<<endl;
	// cout<<"\n"<<height(root);
	// cout<<"\n"<<height(root->right);
	// cout<<"\t"<<height(root->right);
	// cout<<"\n"<<root->value;
	// cout<<"\n"<<root->left->value;
	// cout<<"\t"<<root->right->value;
	// cout<<"\nO\t0";
	// cout<<"\t"<<root->right->left->value;
	// cout<<"\t"<<root->right->right->value;
	// cout<<"\n"<<root->right->right->right->value;
	//6 10 20 30 40 50 25
	cout<<endl;
	return 0;
}