#include <bits/stdc++.h>
using namespace std;

typedef struct node node;

struct Node{
    int data;
    Node *left;
    Node *right;

    Node(const int & value, Node *lt = NULL, Node *rt = NULL):
        data(value), left(lt), right(rt) {}
};

class BST{
    public:
        BST(): root(NULL) {}
        ~BST(){
            destroy_tree();
        }
        void insert(int key);
        node* search(int key);
        void destroy_tree();
    
    private:
        Node *root;       
};
