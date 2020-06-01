#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Member {
	string rank;
	string first;
	string last;
	int rounds;
	string prim;
	string sec;
};

class MemberComp {
public:
	bool operator()(Member &first, Member &second) {
		return (first.rounds < second.rounds);
	}
};

class MemberComp2 {
public:
	bool operator()(Member &first, Member &second) {
		vector<string> data = {first.last, second.last};
		sort(data.begin(), data.end());
		return first.last != data[0];
	}
};

int main() {
	int s, m;
	int i = 1;
	while(cin >> s >> m) {
		if(s == 0 && m == 0) { break; }

		vector<string> skills;
		vector<Member> members;
		priority_queue<Member, vector<Member>, MemberComp> q;

		string sk;
		for(int i = 0; i < s; i++) {
			cin >> sk;
			skills.push_back(sk);
		}

		string data;
		getline(cin, data);
		for(int i = 0; i < m; i++) {
			getline(cin, data);
			int pos;
			int posNext = data.find(" ");

			Member member;
			member.rank = data.substr(0, posNext);
			pos = posNext + 1;
			posNext = data.find(" ", posNext + 1);
			member.first = data.substr(pos, posNext - pos);
			pos = posNext + 1;
			posNext = data.find(" ", posNext + 1);
			member.last = data.substr(pos, posNext - pos);
			pos = posNext + 1;
			posNext = data.find(" ", posNext + 1);
			member.rounds = stoi(data.substr(pos, posNext - pos));
			pos = posNext + 1;
			posNext = data.find(" ", posNext + 1);
			member.prim = data.substr(pos, posNext - pos);
			pos = posNext + 1;
			posNext = data.find(" ", posNext + 1);
			member.sec = data.substr(pos, posNext - pos);
			if(find(skills.begin(), skills.end(), member.prim) != skills.end() &&
				find(skills.begin(), skills.end(), member.sec) != skills.end()) {
				members.push_back(member);
				q.push(member);
			}
		}

		priority_queue<Member, vector<Member>, MemberComp2> q2;
		vector<Member> finals;
		int count = 0;
		while(!q.empty()) {
			Member m = q.top(); q.pop();
			auto it = find(skills.begin(), skills.end(), m.prim);
			if(it != skills.end()) {
				skills.erase(it);
				count++;
			}
			it = find(skills.begin(), skills.end(), m.sec);
			if(it != skills.end()) {
				skills.erase(it);
				count++;
			}

			if(count != 0) {
				q2.push(m);
			}
			count = 0;

			if(skills.empty()) { break; }
		}


		int rounds = 0;
		while(!q2.empty()) {
			Member m = q2.top(); q2.pop();
			finals.push_back(m);
			rounds += m.rounds;
		}

		cout << "Mission #" << i << " (" << rounds << " rounds):" << endl;
		for(int j = 0; j < finals.size(); j++) {
			Member m = finals[j];
			cout << m.rank << " " << m.last << endl;
		}

		i++;
	}

	return 0;
}