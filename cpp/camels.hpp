#include <vector>
#include "linked_list.hpp"

enum color { WHITE, YELLOW, ORANGE, GREEN, BLUE };

class Track {
public:
    Track(int length);
    int first_place();
    int last_place();
    void apply_dice_roll(int color, int value);
    void undo_dice_roll(int color, int value);
    int* simulate_leg();

private:
    int length;
    std::vector<LinkedList<int> > grid;
    std::vector<int> available_dice;
    void simulate_leg(int *counts);
};
