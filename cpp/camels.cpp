#include "camels.hpp"

int NUM_CAMELS = 5;
std::vector<int> DICE_VALS = {1, 2, 3};

Track::Track(int length) {
    for (int i = 0; i < length; i++) {
        grid[i] = LinkedList<int>();
    }

    for (int i = 0; i < 5; i++) {
        grid[0].append(i);
        available_dice.push_back(i);
    }
}

int Track::first_place() {
    for (int i = length - 1; i >= 0; i--) {
        if (grid[i].size() != 0) {
            return grid[i].get_tail();
        }
    }
    return -1;
}

int Track::last_place() {
    for (int i = 0; i < length; i++) {
        if (grid[i].size() > 0) {
            return grid[i].get_head();
        }
    }
    return -1;
}

void Track::apply_dice_roll(int color, int value) {
    int camelSpace = -1; 
    for (unsigned space = 0; space < grid.size(); space++) {
        if (grid[space].contains(color)) {
            camelSpace = space;
        }
    }

    if (camelSpace == -1) {
        return;
    }

    int newCamelSpace = camelSpace + value;
    LinkedList<int> *camelStack = grid[camelSpace].cut(color);
    grid[newCamelSpace].concat(*camelStack);
}

void Track::undo_dice_roll(int color, int value) {
    int camelSpace = -1;
    for (unsigned space = 0; space < grid.size(); space++) {
        if (grid[space].contains(color)) {
            camelSpace = space;
        }
    }
    
    if (camelSpace == -1) {
        return;
    }

    int newCamelSpace = camelSpace - value;
    LinkedList<int> *camelStack = grid[camelSpace].cut(color);
    grid[newCamelSpace].concat(*camelStack);
}

int * Track::simulate_leg() {
    int *counts = new int[NUM_CAMELS];
    simulate_leg(counts);
    return counts;
}

void Track::simulate_leg(int *counts) {
    if (available_dice.size() > 0) {
        int lead = first_place();
        counts[lead] += 1;
    }

    for (unsigned color = 0; color < available_dice.size(); color++) {
        for (unsigned i = 0; i < available_dice.size(); i++) {
            apply_dice_roll(color, DICE_VALS[i]);
            simulate_leg(counts);
            undo_dice_roll(color, DICE_VALS[i]);
        }
    }
}