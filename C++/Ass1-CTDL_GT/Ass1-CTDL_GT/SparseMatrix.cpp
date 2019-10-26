#include"SparseMatrix.h"

void SparseMatrix::setAt(unsigned row, unsigned col, double val) {
	rangeCheck(row, col);
	if (val == 0) return;
	Element *temp = new Element(row, col, val);
	if (size == 0) { 
		//insertAt(0, *temp);
		add(*temp);
		return;
	}
	for (int i = 0; i < this->size; i++) {
		if (this->storage[i].row == row && this->storage[i].col == col) {
			this->storage[i].val = val;
			return;
		}
		else if (this->storage[i].row == row && this->storage[i].col > col) {
			insertAt(i, *temp);
			return;
		}
		else if (this->storage[i].row > row) {
			insertAt(i, *temp);
			return;
		}
		else if (i == size - 1) {
			insertAt(i+1, *temp);
			//add(*temp);
			return;
		}
	}
	
	
}

double SparseMatrix::getAt(unsigned row, unsigned col) {
	rangeCheck(row, col);
	for (int i = 0; i < this->size; i++) {
		if (this->storage[i].row == row && this->storage[i].col == col) {
			return this->storage[i].val;
		}
	}
	
	return 0;
	
}

SparseMatrix* SparseMatrix::transpose() {
	SparseMatrix* result = NULL;
	result = new SparseMatrix(this->ncol, this->nrow);
	for (int i = 0; i < this->size; i++) {
		result->setAt(this->storage[i].col, this->storage[i].row, this->storage[i].val);
	}
	
	return result;
}

double SparseMatrix::trace() {
	if (nrow != ncol)
		throw "TraceOfNoneSquareMatrix";
	double result = 0;
	for (int i = 0; i < this->nrow; i++) {
		result += getAt(i, i);
	}
	return result;
}

SparseMatrix* SparseMatrix::add(const SparseMatrix& b) {
	

	/*SparseMatrix test = SparseMatrix(b);
	
	result = new SparseMatrix(this->nrow, this->ncol);
	for (int i = 0; i < this->nrow; i++) {
		for (int j = 0; j < this->ncol; j++) {
			double temp = getAt(i, j) + test.getAt(i, j);
			if (temp != 0)result->setAt(i, j, temp);
		}
	}*/

	if (nrow != b.nrow || ncol != b.ncol)
		throw "MismatchedDimensions";

	SparseMatrix* result = NULL;
	result = new SparseMatrix(this->nrow, this->ncol);
	int i = 0, j = 0;
	while (i < size && j < b.size) {
			if (storage[i].row == b.storage[j].row) {
				if (storage[i].col == b.storage[j].col) {
					double kq = storage[i].val + b.storage[j].val;
					if (kq!=0) result->setAt(storage[i].row, storage[i].col, kq);
					i++;
					j++;
				}
				else if (b.storage[j].col > storage[i].col) {
					result->setAt(storage[i].row, storage[i].col, storage[i].val);
					i++;
				}
				else {
					result->setAt(b.storage[j].row, b.storage[j].col, b.storage[j].val);
					j++;
				}
			}
			else if (b.storage[j].row > storage[i].row) {
				result->setAt(storage[i].row, storage[i].col, storage[i].val);
				i++;
			}
			else {
				result->setAt(b.storage[j].row, b.storage[j].col, b.storage[j].val);
				j++;
			}	
		
	}

	while (i < size) {
		result->setAt(storage[i].row, storage[i].col, storage[i].val);
		i++;
	}
		
	while (j < b.size) {
		result->setAt(b.storage[j].row, b.storage[j].col, b.storage[j].val);
		j++;
	}
	
	return result;
}

SparseMatrix* SparseMatrix::multiplyPointWise(const SparseMatrix& b) {
	if (nrow != b.nrow || ncol != b.ncol)
		throw "MismatchedDimensions";

	SparseMatrix test = SparseMatrix(b);
	
	SparseMatrix* result = NULL;
	result = new SparseMatrix(this->nrow, this->ncol);
	/*for (int i = 0; i < this->nrow; i++) {
		for (int j = 0; j < this->ncol; j++) {
			double temp = getAt(i, j) * test.getAt(i, j);
			if (temp != 0)result->setAt(i, j, temp);
		}
	}*/
	int i = 0, j = 0;
	while (i < size && j < b.size) {
		if (storage[i].row == b.storage[j].row) {
			if (storage[i].col == b.storage[j].col) {
				double kq = storage[i].val * b.storage[j].val;
				if (kq != 0) result->setAt(storage[i].row, storage[i].col, kq);
				i++;
				j++;
			}
			else if (b.storage[j].col > storage[i].col) {
				i++;
			}
			else {
				j++;
			}
		}
		else if (b.storage[j].row > storage[i].row) {
			i++;
		}
		else {
			j++;
		}

	}

	return result;
}