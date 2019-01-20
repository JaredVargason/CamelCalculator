#include "linked_list.hpp"

template <typename T>
LinkedList<T>::LinkedList() {
    head = nullptr;
    tail = nullptr;
}

template <typename T>
LinkedList<T>::LinkedList(T data) {
    Node<T> *n = new Node<T>(data);
    head = n; 
    tail = n;
}

template <typename T>
LinkedList<T>::LinkedList(std::vector<T> data) {
    if (data.size() > 0) {
        return;
    }

    Node<T> *currentNode, *nextNode;
    currentNode = new Node<T>(data[0]);
    head = currentNode;

    for (unsigned i = 1; i < data.size(); i++) {
        nextNode = new Node<T>(data[i]);
        currentNode->next = nextNode;

        currentNode = nextNode;
    }

    tail = currentNode;
}

template <typename T>
LinkedList<T>::~LinkedList() {
    while (head != nullptr) {
        Node<T> *temp = head;
        head = head->get_next();
        delete(temp);
    }
}

template <typename T>
void LinkedList<T>::append(T data) {
    Node<T> *n = new Node<T>(data);

    if (head == nullptr) {
        head = n;
    }

    tail->set_next(n);
    tail = n;
}

template<typename T>
void LinkedList<T>::concat(LinkedList<T> list) {
    if (head == nullptr) {
        head = list.head;
    }
    else {
        tail->next = list.head;
    }
    tail = list.tail;

    list.head = nullptr;
    delete(list);
}

template<typename T>
bool LinkedList<T>::contains(T item) {
    Node<T> *ptr = this.head;
    while (ptr != nullptr) {
        if (ptr->data == item) {
            return true;
        }
        ptr = ptr->get_next();
    } 
    return false;
}

template<typename T>
LinkedList<T>* LinkedList<T>::cut(T item) {
    Node<T> *ptr = head;
    if (head == nullptr) {
        return nullptr;
    }

    //if item is at head
    if (head->data == item) {
        LinkedList<T> *newList = new LinkedList<T>(head);
        head = nullptr;
        tail = nullptr;
        return newList;
    }

    //if item is in middle or end
    while (ptr->next != nullptr) {
        if (ptr->next->data == item) {
            LinkedList<T> *temp = new LinkedList<T>(ptr->next);
            tail = ptr;
            return temp;
        }
    }

    //if not found, return nullptr 
    return nullptr;
}

template<typename T>
T LinkedList<T>::get_head() {
    return head->data;
}

template<typename T>
T LinkedList<T>::get_tail() {
    return tail->data;
}

template<typename T>
bool LinkedList<T>::remove(T item) {
    Node<T> *ptr = head;
    if (ptr == nullptr) {
        return nullptr;
    }

    //first item is removed
    if (ptr->data == item) {
        head = ptr->next;
        T data = ptr->data;
        delete(ptr);
        return true;
    }

    //other item removed
    while (ptr->next != nullptr) {
        if (ptr->next->data == item) {
            Node<T> *temp = ptr->next;
            ptr->next = temp->next;
            T data = temp->data;

            if (tail == temp) {
                tail = ptr;
            }
            delete(temp);
            return true;
        }
    }

    return false; 
}

template <typename T>
int LinkedList<T>::size() {
    int count = 0;
    Node<T> *ptr = &head;
    while (ptr != nullptr) {
        ptr = ptr.get_next();
        count++;
    }
    return count;
}
