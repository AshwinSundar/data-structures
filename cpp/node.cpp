#include <iostream>
#include <memory>
#include <optional>

template<typename T>
class Node
{
	public:
		Node<T>(int val) : _value(val), _balance(0) { };

		Node<T>(int val, Node<T>& left, Node<T>& right)
			: _value(val), _leftNode(left), _rightNode(right)
		{
			// updateBalance();	// TO DO
		}

		~Node<T>() 
		{
			// check if child pointers, parents are connected to anything, delete if not
		}
	
		friend std::ostream & operator << (std::ostream &out, const Node<T> &n) {
			out << n._value;	
			if (n._leftNode) { out << "--" << n._leftNode; }
			if (n._rightNode) { out << "\n|\n" << n._rightNode; }
			return out << std::endl;	
		}

		T getValue() { return _value; }

		T getBalance() { return _balance; }

		void addChild(Node<T>& n)
		{
			if (n.getValue() < _value) { !_leftNode ?  _leftNode = n : _leftNode->addChild(n); }
			else { !_rightNode ? _rightNode = n : _rightNode->addChild(n); }
		}

		Node<T>& _parentNode;
		Node<T>& _leftNode;
		Node<T>& _rightNode;

	private:
		void setBalance(int bal) { _balance = bal; }

		void updateBalance() { } // TO DO

		Node<T>& find(T val) { } // TO DO

		// opportunity for memoization?
		bool contains(T val) { } // TO DO 

		T _value;
		int _balance;
};

int main() {
	Node<int> nodeA(2);
	Node<int> nodeB(3);
	Node<int> headNode(1, nodeA, nodeB);
	// Node<int> headNode(1, std::make_unique<Node<int>>(nodeA), std::make_unique<Node<int>>(nodeB)); // problems here
	// See ~4:30 -> https://www.youtube.com/watch?v=UOB7-B2MfwA

	// headNode.addChild(childNode); // some issues here
	// std::cout << headNode << std::endl;
	return 0;
};

// SMART POINTERS
// The use case for a smart pointer became obvious to me when I was attempting to solve a particular problem - what happens if a Node's parent or children are deleted? The obvious solution was to define a destructor that accessed the Node's parent and children, and removed corresponding link from their side. But then this required access to other Node's private members. The solution is to use a smart pointer. According to to cppreference.com, **Smart pointers are used to make sure that an object is deleted if it is no longer used (referenced)**. 
// test whether you want unique_ptr and shared_ptr. What happens to when an object is deleted? Does the pointer keep existing? Try inspecting with gdb. Could be a cool article to test it out as well. You will learn a LOT about pointers if you can get through that. Use gdb

// PATTERN MATCHING
// Without pattern matching, the addChild method looks like this:
/*
		void addChild(Node<T> n)
		{
			std::unique_ptr<Node<T>> childNode = std::make_unique<Node<T>>(n.getValue());
			if (n.getValue() < _value) 
			{
				if (!_leftNode)
				{
					_leftNode = n;
				}	
				else 
				{
					_leftNode.addChild(n);
				}
			}
			else
			{
				if (!_rightNode)
				{
					_rightNode = n;
				}	
				else
				{
					_rightNode.addChild(n);
				}
			}
		}
*/

// Not very pretty. 
