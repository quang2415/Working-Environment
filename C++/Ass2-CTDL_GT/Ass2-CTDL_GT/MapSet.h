#pragma once
#include"AVLNode.h"
class MapSet
{
private:
	AVLNode * root;
	int count;


protected:
	void clearRec(AVLNode*root);
	void printInOrderRecursion(AVLNode*root);


	

public:
	MapSet();
	~MapSet();
	void clear();
	void print();
	int getSize() { return count; }

	// YOUR TASKS START HERE	
	void add(string word, int line);	
	
	// END HERE
};

