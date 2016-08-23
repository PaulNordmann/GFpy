#!/usr/bin/env python
from numpyExtend import getNonZeroInRow;
from numpyExtend import getNonZeroInColumn;
from numpyExtend import changeRow;
from numpyExtend import changeColumn;
from numpyExtend import getBrightMatrix;
from numpyExtend import setRow;

class GF:
	def __init__(self, gf):
		self.galoisField = gf;

	def add(self, a, b):
		if isinstance(a,int) and isinstance(b,int):
			return (a + b) % self.galoisField;
		
		if isinstance(a, list) and isinstance(b, list):
			r = [];
			for i in range(len(a)):
				r.append(self.add(a[i], b[i]));
			return r;

		raise NameError('Wrong Input');
	
	def matrix_rank(self, originalMatrix):
		matrix = getBrightMatrix(originalMatrix);
		column=0;
		zeroRows = [];
		# es gibt mehr spalten als Zeilen,
		# deswegen jede Spalte quer bis zum Zeilenende runter
		while column < matrix.shape[0]:
			columns = getNonZeroInColumn(matrix, column, column);
			# es muss mindestens ein eins geben, und zwar die auf dem quer Vektor
			if columns == []:
				rows = getNonZeroInRow(matrix, column, column);
				# wenn es keine weitere eins in der Zeile gibt, ist der Zeilenvektor ein Nullvektor
				if rows == []:
					zeroRows.append(column);
					column+=1;
					continue;

				changeColumn(matrix, column, rows.pop());
				
				continue;

			columns.pop(0);

			#alle weiteren werden aufsummiert
			for i in columns:
				sumRow = self.add(matrix[column].tolist()[0], matrix[i].tolist()[0]);
				matrix = setRow(matrix, i, sumRow);
			
			column+=1;

		return column - len(zeroRows);
