#include <deque>
#include <vector>

int computeDifference(std::vector<int>& deck) {
    int mscore = 0;
    int ascore = 0;
    std::deque<int> queue(deck.begin(), deck.end());

    bool draw_front = true;
    bool is_m = true;

    while (!queue.empty()) {
        int top = 0;
        if (draw_front) {
            top = queue.front();
            queue.pop_front();
        } else {
            top = queue.back();
            queue.pop_back();
        }

        if (is_m) {
            mscore += top;
        } else {
            ascore += top;
        }

        if (top % 3 == 0) {
            draw_front = !draw_front;
        }

        is_m = !is_m;
    }

    return mscore - ascore;
}
