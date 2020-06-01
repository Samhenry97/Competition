#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int n) {
	if(n % 2 == 0 || n % 3 == 0 || n % 5 == 0) { return false; }
	for(int i = 3; i * i <= n; i += 2) {
		if(n % i == 0) return false;
	}
	return true;
}

void genPrimes(vector<int> &vals) {
	vals.push_back(7);
	for(int i = 9; i < 800000000; i += 2) {
		if((i - 1) % 1000000 == 0) { cout << i - 1 << " primes generated." << endl; }
		if(isPrime(i)) { vals.push_back(i); }
	}
}

int main() {
	vector<int> ugly;
	vector<int> primes;

	genPrimes(primes);

	cout << "Primes generated." << endl;

	int found = 1;
	int current = 2;
	ugly.push_back(1);
	while(found <= 1500) {
		if(found % 100 == 0) { cout << "Found " << found << endl; }
		bool isUgly = true;
		for(int j = 0; j < primes.size(); j++) {
			if(primes[j] > current) {
				break;
			}
			if(current % primes[j] == 0) { isUgly = false; break; }
		}
		if(isUgly && !(current % 2 == 0 || current % 3 == 0 || current % 5 == 0)) {
			isUgly = false;
		}
		if(isUgly) {
			ugly.push_back(current);
			found++;
		}
		current++;
	}

	for(int i = 0; i < ugly.size(); i++) {
		cout << i << ": " << ugly[i] << endl;
	}
	
	return 0;
}