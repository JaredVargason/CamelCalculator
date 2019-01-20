#include <vector>

template<typename T>
struct Node {
    Node<T> *next;
    T data;

    Node<T>(T data);
};

template <typename T>
class LinkedList {
    private:
    Node<T> *head;    
    Node<T> *tail;
    LinkedList<T>(Node<T> node);
    public:
    LinkedList<T>();
    LinkedList<T>(T data);
    LinkedList<T>(std::vector<T> data);
    ~LinkedList<T>();
    void append(T data);
    void concat(LinkedList<T> list);
    bool contains(T item);
    LinkedList<T>* cut(T item);
    T get_head();
    T get_tail();
    bool remove(T item);
    int size();
};