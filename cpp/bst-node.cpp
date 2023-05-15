class BstNode {
	public:
		int balance;
		int val;
		BstNode &leftNode;
		BstNode &rightNode;
		void addChild(BstNode &node);	
		void find(int val);
	private:
		
}
