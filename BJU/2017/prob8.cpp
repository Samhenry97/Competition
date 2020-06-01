#include <iostream>
#include <string>

using namespace std;

bool validBoard(char **board, int n) {
	
	return true;
}

int main() {
	int n; cin >> n;

	while(n) {
		char board[n][n];
		int queenPos[n];
		for(int y = 0; y < n; y++) {
			queenPos[y] = 0;
		}
		for(int y = 1; y < n; y++) {
			for(int x = 0; x < n; x++) {
				board[y][x] = 'x';
			}
		}
		for(int y = 0; y < n; y++) {
			board[0][y] = '.';
		}

		int total = 0;
		bool end = true;
		while(end) {

			bool valid = true;
			for(int y = 0; y < n && valid; y++) {
				for(int x = 0; x < n && valid; x++) {
					if(board[y][x] == '.') {
						for(int tmp = 0; tmp < n && valid; tmp++) {
							if(tmp != x && board[y][tmp] == '.') {
								valid = false;
							}
							if(tmp != y && board[tmp][x] == '.') {
								valid = false;
							}
							if(tmp != x && tmp != y && board[tmp][tmp] == '.') {
								valid = false;
							}
						}
					}
				}
			}

			if(valid) {
				total += 1;
			}

			for(int i = n - 1; i >= 0; i--) {
				if(queenPos[i] == n - 1) {
					board[queenPos[i]][i] = 'x';
					queenPos[i] = 0;
					board[queenPos[i]][i] = '.';
					if(i == 0) end = false;
				} else {
					board[queenPos[i]][i] = 'x';
					queenPos[i]++;
					board[queenPos[i]][i] = '.';
					break;
				}
			}
		}

		cout << total << endl;

		cin >> n;
	}

	return 0;
}