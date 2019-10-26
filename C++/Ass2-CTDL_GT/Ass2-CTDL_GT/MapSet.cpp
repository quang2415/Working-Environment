#include "MapSet.h"

MapSet::MapSet()
{
	root = NULL;
	count = 0;
}


MapSet::~MapSet()
{
	clear();
}

void MapSet::clearRec(AVLNode* root) {
	if (root != NULL) {
		clearRec(root->left);
		clearRec(root->right);
		delete root;
	}
}
void MapSet::clear() {
	clearRec(root);
	root = NULL;
	count = 0;
}
void MapSet::printInOrderRecursion(AVLNode* root) {
	if (root != NULL) {		
		printInOrderRecursion(root->left);
		cout << setw(20) << left << root->word.c_str() << "|" << setw(10) << right << root->freq << "|";
		root->list.print();
		cout << endl;
		printInOrderRecursion(root->right);
	}
}

void MapSet::print() {
	cout << "The total number of words: " << count << endl;
	cout << "---------------------------------------" << endl;
	cout << setw(20) << left << "Word" << "|" << setw(10) << right << "Freq." << "|" << "Line No." << endl;
	cout << "---------------------------------------" << endl;
	printInOrderRecursion(root);
	cout << "---------------------------------------" << endl;
}

void MapSet::add(string word, int line) {
	if (root == NULL) {
		root = new AVLNode(word, line);
		count++;
		return;
	}
	AVLNode* temp = root;
	AVLNode* rotate = NULL;
	while (temp) {
		if (word < temp->word) {
			if (temp->balance == -1) {
				rotate = temp;
				temp = temp->left;
				continue;
			}
			if (temp->left == NULL) {
				temp->left = new AVLNode(word, line);
				temp->balance -= 1;
				count++;
				break;
			}
			temp->balance -= 1;
			temp = temp->left;
		}
		else if (word > temp->word) {
			if (temp->balance == 1) {
				rotate = temp;
				temp = temp->right;
				continue;
			}

			if (temp->right == NULL) {
				temp->right = new AVLNode(word, line);
				temp->balance += 1;
				count++;
				break;
			}
			temp->balance += 1;
			temp = temp->right;

		}
		else {
			temp->freq++;
			temp->list.add(line);
			return;
		}
	}
}
