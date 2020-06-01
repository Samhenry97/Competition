#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <vector>
#include <string>

using namespace std;

string decide(vector<vector<char> > &board) {
	string ans = "Legal Game, ";
	char win = -1;
	bool tie = false;
	int i = 0;
	bool won = false;
	for(int y = 0; y < board.size(); y++) {
		for(int x = 0; x < board[y].size(); x++) {
			char cur = board[y][x];
			if(cur != -1 && !tie) {
				switch(i) {
					case 0 :
						if(board[y][x + 1] == cur && board[y][x + 2] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} else if(board[y + 1][x] == cur && board[y + 2][x] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} else if(board[y + 1][x + 1] == cur && board[y + 2][x + 2] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} break;
					case 1 : 
						if(board[y + 1][x] == cur && board[y + 2][x] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} break;
					case 2 : 
						if(board[y + 1][x] == cur && board[y + 2][x] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} else if(board[y + 1][x - 1] == cur && board[y + 2][x - 2] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} break;
					case 3 : 
						if(board[y][x + 1] == cur && board[y][x + 2] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						}
					case 4 : break;
					case 5 : break;
					case 6 : 
						if(board[y][x + 1] == cur && board[y][x + 2] == cur) {
							if(win == cur) win = cur;
							else tie = true;
							won = true;
						} break;
					case 7 : break;
					case 8 : break;
				}
			}
			i++;
		}
	}
	if(!won) {
		ans += "No winner";
	} else if(tie) {
		ans += "No winner";
	} else {
		ans += win;
		ans += " won";
	}
	return ans;
}

int main() {
	int a, b;
	bool x = true;
	bool illegal = false;
	vector<vector<char> > board(3, vector<char>(3,-1));
	while(cin >> a >> b) {
		if(a == 0 || b == 0) {
			if(illegal) {
				cout << "Illegal Game" << endl;
			} else {
				cout << decide(board) << endl;
			}
			for(int y = 0; y < board.size(); y++) {
				for(int x = 0; x < board[x].size(); x++) {
					board[y][x] = -1;
				}
			}
			x = true;
			illegal = false;
		} else if(!illegal) {
			if(board[a - 1][b - 1] == -1) {
				board[a - 1][b - 1] = x ? 'X' : 'O';
			} else {
				illegal = true;
			}
			x = !x;
		}
	}

	return 0;
}