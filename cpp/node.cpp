#include <optional>
#include <iostream>
#include <memory>

template<typename T>
class Node
{
	public:
		// constructors
		Node<T>(int val) : _value(val), _parentNode(nullptr), _leftNode(nullptr), _rightNode(nullptr) { };
		Node<T>(int val, Node<T>& parent, Node<T>& left, Node<T>& right) : _value(val), _parentNode(parent), _leftNode(left), _rightNode(right) { };
		// ~Node<T> // do something on destruction. send a note somewhere? maybe parent and child nodes need to know about it actually
		// SMART POINTERS are the solution! Instead of doing manual cleanup with a destructor, let a smart pointer handle it automatically
		T getValue() { return _value; }
		T getBalance() { return _balance; }
		std::unique_ptr<Node<T>> _parentNode;
		std::unique_ptr<Node<T>> _leftNode;
		std::unique_ptr<Node<T>> _rightNode;

	private:
		T _value;
		int _balance;
		void setBalance(int bal) { _balance = bal; }
		void calcBalance(); 
		void addChild(Node<T>); // re-calc balance at end
		std::unique_ptr<Node<T>> find(T val);
		bool contains(T val); // opportunity for memoization?
		// void print(); 
};

int main() {
	Node<int> int_node(1);
	// std::cout << "New node has value: " << (std::string)int_node.getValue() << std::endl;
	std::cout << "EY" << std::endl;
	return 0;
};
/*
class Node<int> {
	public:
		Node() = delete;
		Node(int val);
		Node(int val, Node parentNode, Node leftNode, Node rightNode);
		int _balance;
		int _value; // change to const
		void addChild(Node& node);	
		void find(int val);
	private:
		// std::optional<Node> _parentNode;
		// Node& _leftNode;
		// Node& _rightNode;
};
*/

// is this needed? let's implement it anyway, as an exercise
// implement as singleton, in separate file. import here
/*
class NullNode {
	public:
		NullNode() = delete;
};
*/

// SMART POINTERS
// The use case for a smart pointer became obvious to me when I was attempting to solve a particular problem - what happens if a Node's parent or children are deleted? The obvious solution was to define a destructor that accessed the Node's parent and children, and removed corresponding link from their side. But then this required access to other Node's private members. The solution is to use a smart pointer. According to to cppreference.com, **Smart pointers are used to make sure that an object is deleted if it is no longer used (referenced)**. 
// test whether you want unique_ptr and shared_ptr. What happens to when an object is deleted? Does the pointer keep existing? Try inspecting with gdb. Could be a cool article to test it out as well. You will learn a LOT about pointers if you can get through that. 
