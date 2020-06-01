#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

typedef pair<ll, ll> pii;

ll n, p, s, l, k;
map<pii, pii> links;
ll cur = -1;
ll idx[10];
bool done[10];
ll doneCount;

ll index(pii &val) {
    ll ret = (ll) val.second * (ll) n;
    if(val.second % 2 == 0) {
        return ret + val.first;
    } else {
        return ret + (n - 1 - val.first);
    }
}

pii point(ll idx) {
    ll y = idx / n;
    if(y % 2 == 0) {
        return { idx % n, y };
    } else {
        return { n - 1 - idx % n, y };
    }
}

void move(ll amt) {
    pii loc = point(idx[cur] + amt);
    while(links.find(loc) != links.end()) {
        loc = links[loc];
    }
    idx[cur] = index(loc);
    if((ll) idx[cur] >= (ll) n * (ll) n) {
        done[cur] = true;
        doneCount++;
    }
}

bool nextPlayer() {
    if(doneCount == p) { return false; }
    cur++;
    if(cur >= p) cur = 0;
    while(done[cur]) {
        cur++;
        if(cur >= p) cur = 0;
    }
    return true;
}

void visit(const pii &link) {
    if(links.find(links[link]) != links.end()) {
        visit(links[link]);
        links[link] = links[links[link]];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> p >> s;
    fill(idx, idx + p, -1);
    for(ll i = 0; i < s; i++) {
        ll x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        x1--; y1--; x2--; y2--;
        links[{x1, y1}] = {x2, y2};
    }
    cin >> l;
    for(ll i = 0; i < l; i++) {
        ll x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        x1--; y1--; x2--; y2--;
        links[{x1, y1}] = {x2, y2};
    }
    for(auto &link : links) {
        visit(link.first);
    }
    cin >> k;

    while(k-- && nextPlayer()) {
        ll a, b; cin >> a >> b;
        move(a + b);
    }

    for(ll i = 0; i < p; i++) {
        if(done[i]) {
            cout << i + 1 << " winner" << endl;
        } else {
            pii loc = point(idx[i]);
            cout << i + 1 << " " << loc.first + 1 << " " << loc.second + 1 << endl;
        }
    }
    
    return 0;
}