#include <fstream>
#include <iostream>
#include <string>
#include <cctype>
#include "MapSet.h"

using namespace std;

void processLine(string line, int linenum, MapSet* map) {
	string word = "";
	for(int i = 0; i <line.length(); i++) {
		if (isalpha(line[i])) {
			word += tolower(line[i]);
		}
		else {
			if (word != "") {
				map->add(word, linenum);
				word = "";
			}
		}
	}
	if (word != "")
		map->add(word, linenum);
}


void processFile(istream& in, MapSet* map) {
	int linenum = 0;
	while (true) {
		string line;
		getline(in, line);
		if (!in)
			break;
		linenum++;
		processLine(line, linenum, map);
	}
}


int main(int argc, char **argv) {
	MapSet* map = new MapSet();
	if (argc == 1) {  // no command line parameters.
		ifstream input("input.txt");
		processFile(input, map);
	}
	else if (argc == 2) {  // one command line parameters.
		ifstream input(argv[1]);
		if (!input) {
			cerr << "Can't open input file, \"" << argv[1] << "\".\n";
			return 1;
		}
		else
			processFile(input, map);
	}
	else {
		cerr << "Usage:  " << argv[0] << " [inputfile].\n";
		return 1;
	}
	map->print();
	delete map;

	/*AVLNode* root = new AVLNode("13", 0);
	AVLNode* n1 = new AVLNode("10", 0);
	AVLNode* n2 = new AVLNode("15", 0);
	AVLNode* n3 = new AVLNode("5", 0);
	AVLNode* n4 = new AVLNode("11", 0);
	AVLNode* n5 = new AVLNode("16", 0);
	AVLNode* n6 = new AVLNode("4", 0);
	AVLNode* n7 = new AVLNode("8", 0);
	AVLNode* n8 = new AVLNode("3", 0);
	root->left = n1;
	root->right = n2;
	n2->right = n5;
	n1->left = n3;
	n1->right = n4;
	n3->left = n6;
	n3->right = n7;
	n6->left = n8;
	MapSet* map = new MapSet();
	map->print2D(root);

	AVLNode* temp = root;
	AVLNode* t2 = n1;
	temp->left = map->right_rotate(t2);
	map->print2D(root);*/

	//AVLNode* root = new AVLNode("30", 0);
	//AVLNode* n1 = new AVLNode("5", 0);
	//AVLNode* n2 = new AVLNode("35", 0);
	//AVLNode* n3 = new AVLNode("32", 0);
	//AVLNode* n4 = new AVLNode("40", 0);
	//AVLNode* n5 = new AVLNode("45", 0);
	//root->left = n1;
	//root->right = n2;
	//n2->left = n3;
	//n2->right = n4;
	//n4->right = n5;
	//MapSet* map = new MapSet();

	//AVLNode* temp = root;

	//map->print2D(temp);
	//cout << endl;
	//cout << "Left rotate at 30" << endl;
	//temp=map->left_rotate(temp);
	//map->print2D(temp);

	system("pause");
	return 0;
}