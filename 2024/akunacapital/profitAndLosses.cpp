#include <unordered_map>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

struct Order {
    int timestamp;
    int stockId;
    bool buy;
    int quantity;
};

struct PriceUpdate {
    int timestamp;
    int stockId;
    int delta;
};

using namespace std;

auto profitsAndLosses(int initialPrice, const std::vector<Order> &orders, const std::vector<PriceUpdate> &feed) {
    unordered_map<int, vector<pair<int, int>>> feed_map;
    // unordered_map<int, deque<pair<int, int>>> order_map;

    unordered_map<int, int> profit_map;

    for (auto update : feed) {
        if (feed_map.find(update.stockId) == feed_map.end()) {
            feed_map[update.stockId] = vector<pair<int, int>>();
        }
        // cout << "push ts=" << update.timestamp << "  push delta=" << update.delta << endl;
        feed_map[update.stockId].push_back({update.timestamp, update.delta});
    }


    for (auto order: orders) {
        if (profit_map.find(order.stockId) == profit_map.end()) {
            profit_map[order.stockId] = 0;
        }

        int price = initialPrice;
        for (const auto &[timestamp, delta] : feed_map[order.stockId]) {
            cout << "ts=" << timestamp << "  order.ts=" << order.timestamp << "  delta=" << delta << endl;
            if (timestamp <= order.timestamp) {
                price += delta; // apply all price changes
                cout << "id=" << order.stockId << " delta=" << delta << " ts=" << order.timestamp << endl;
            } else {
                break;
            }
        }
        cout << order.timestamp << "  " << price << endl;

        profit_map[order.stockId] += order.buy ? -order.quantity * price : order.quantity * price;
    }
    vector<pair<int,int>> res;
    for (const auto &[id, profit] : profit_map) {
        res.push_back({id, profit});
    }
    return res;
}

int main(){
    vector<Order> orders;
    vector<PriceUpdate> updates;

    orders.push_back(Order{0,2,true,15});
    orders.push_back(Order{4,1,false,30});
    orders.push_back(Order{6,1,true,10});
    orders.push_back(Order{10,2,true,5});
    orders.push_back(Order{15,4,false,100});

    updates.push_back(PriceUpdate{3,1,4});
    updates.push_back(PriceUpdate{5,1,-1});
    updates.push_back(PriceUpdate{8,2,2});
    updates.push_back(PriceUpdate{12,3,-5});

    const auto result = profitsAndLosses(10, orders, updates);
    for (auto &&element: result) {
        auto [a,b] = element;
        int stockId = a;
        int profit = b;
        cout << "stockId=" << stockId << "  profit=" << profit << endl;
    }
}
