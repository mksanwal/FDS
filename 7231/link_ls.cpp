#include <iostream>
#include <cstring>
#include <stack> // Include for using stack
using namespace std;

class node {
private:
    char name[10];
    long prn;
    node* next;

public:
    node() : prn(0), next(nullptr) {
        strcpy(name, "");
    }

    friend class list;
};

class list {
private:
    node* president;
    node* secretary;
    int count;

public:
    list() : president(nullptr), secretary(nullptr), count(0) {}

    void gethead();
    void gettail();
    void addmember();
    void display_count();
};

void list::gethead() {
    president = new node;
    cout << "Enter Name of President: ";
    cin >> president->name;
    cout << "Enter PRN of President: ";
    cin >> president->prn;
    president->next = nullptr;
    count++;
}

void list::gettail() {
    secretary = new node;
    cout << "Enter the name of the secretary: ";
    cin >> secretary->name;
    cout << "Enter PRN of secretary: ";
    cin >> secretary->prn;
    secretary->next = nullptr;
    count++;
}

void list::addmember() {
    node* tmp = new node;
    cout << "Enter Member name: ";
    cin >> tmp->name;
    cout << "Enter PRN of Member: ";
    cin >> tmp->prn;
    tmp->next = nullptr;

    if (!president) {
        president = tmp;  // First member
        secretary = tmp;  // Set secretary to the first member
    } else if (tmp->prn < president->prn) {  // New president
        tmp->next = president;
        president = tmp;
    } else {
        node* current = president;
        node* previous = nullptr;

        while (current && current->prn < tmp->prn) {
            previous = current;
            current = current->next;
        }
        
        tmp->next = current;
        if (previous) {
            previous->next = tmp;
        }

        if (!current) { // Update secretary if added at the end
            secretary = tmp;
        }
    }
    count++; // Increment count only when member is successfully added
}

void list::display_count() {
    cout << "Member count: " << count << endl;
}

int main() {
    list a;
    a.gethead();
    a.gettail();

    int c = 0;
    while (true) {
        cout << "Enter Choice:\n1.Add Member\n2.Display No of Members\n3.Exit\n";
        cin >> c;
        switch (c) {
        case 1: a.addmember(); break;
        case 2: a.display_count(); break;
        case 3: return 0;
        default: cout << "Wrong choice\n"; break;
        }
    }
}

