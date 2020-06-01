#include <iostream>

using namespace std;

int** &moveLeft(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[y][2 - x] == 0) {
				input[y][2 - x] = input[y][3 - x];
				input[y][3 - x] = 0;
			}
		}
	}
	return input;
}

int** &addLeft(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[y][x] == input[y][x + 1]) {
				input[y][x] = input[y][x + 1] * 2;
				input[y][x + 1] = 0;
			}
		}
	}
	return input;
}

int** &moveUp(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[2 - x][y] == 0) {
				input[2 - x][y] = input[3 - x][y];
				input[3 - x][y] = 0;
			}
		}
	}
	return input;
}

int** &addUp(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[x][y] == input[x + 1][y]) {
				input[x][y] = input[x + 1][y] * 2;
				input[x + 1][y] = 0;
			}
		}
	}
	return input;
}

int** &moveRight(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[y][x + 1] == 0) {
				input[y][x + 1] = input[y][x];
				input[y][x] = 0;
			}
		}
	}
	return input;
}

int** &addRight(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[y][3 - x] == input[y][2 - x]) {
				input[y][3 - x] = input[y][2 - x] * 2;
				input[y][2 - x] = 0;
			}
		}
	}
	return input;
}

int** &moveDown(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[3 - x][y] == 0) {
				input[3 - x][y] = input[2 - x][y];
				input[2 - x][y] = 0;
			}
		}
	}
	return input;
}

int** &addDown(int** &input) {
	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 3; x++) {
			if(input[2 - x][y] == input[3 - x][y]) {
				input[3 - x][y] = input[2 - x][y] * 2;
				input[2 - x][y] = 0;
			}
		}
	}
	return input;
}

int main() {
	int cur;
	int **grid = new int*[4];
	for(int i = 0; i < 4; i++) {
		grid[i] = new int[4];
	}

	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 4; x++) {
			cin >> grid[y][x];
		}
	}

	int dir;
	int temp = 0;
	cin >> dir;
	switch(dir) {
		case 0 : moveLeft(moveLeft(addLeft(moveLeft(moveLeft(moveLeft(grid)))))); break;
		case 1 : moveUp(moveUp(addUp(moveUp(moveUp(moveUp(grid)))))); break;
		case 2 : moveRight(moveRight(addRight(moveRight(moveRight(moveRight(grid)))))); break;
		case 3 : moveDown(moveDown(addDown(moveDown(moveDown(moveDown(grid)))))); break;
	}

	for(int y = 0; y < 4; y++) {
		for(int x = 0; x < 4; x++) {
			cout << grid[y][x] << " ";
		}
		cout << "\n";
	}

	return 0;
}