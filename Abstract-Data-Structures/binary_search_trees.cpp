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

        Node* search(const int & key){
            search(key, root);
        }

        void insert(const int & key){
            insert(key, root);
        }

        void remove(const int & key){
            remove(key, root);
        }

        const int & findMin(){
            Node* min_node = findMin(root);
            if(min_node != NULL)
                return min_node->data;
            return -1;
        }

        void destroy_tree();
    
    private:
        Node *root;
        Node* search(const int &key, Node* & t);        
        void insert(const int & key, Node* & t);
        Node* findMin(Node *t);
        void remove(const int & key, Node* & t);
};

Node* BST::search(const int & key, Node* & t){
    if(t == NULL)
        return NULL;

    if(key == t->data)
        return t;

    if(key < t->data)
        return search(key, t->left);

    return search(key, t->right);
}

void BST::insert(const int & key, Node * & t){
    if(t == NULL){
        t = new Node(key);
    }
    else if(key < t->data)
        insert(key, t->left);
    else if(key > t->data)
        insert(key, t->right);
    else
        ; //duplicate: do nothing
}

void BST::remove(const int & key, Node * & t){
    if(t == NULL)
        return; // key not found

    if(key < t->data)
        remove(key, t->left);

    if(key > t->data)
        remove(key, t->right);

    else if(t->left != NULL && t->right != NULL){
        Node* min_right = findMin(t->right);
        t->data = min_right->data;
        remove(min_right->data, t->right);
    }

    else{
        Node* old_node = t;
        t = (t->left != NULL) ? t->left : t->right;
        delete old_node;
    }
}

Node* BST::findMin(Node *t){
    if(t != NULL){
        while(t->left != NULL)
            t = t->left;
    }
    return t;
}
