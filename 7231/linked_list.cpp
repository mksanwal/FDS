#include <iostream>
#include <cstring>
#include <stack> 
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
    void displaylist();
    void remove();
    void display_count();
    void display_reverse();
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

void list::displaylist() {
    node* current = president;
    while (current) {
        cout << "Name of the Member: " << current->name << endl;
        cout << "PRN of the Member: " << current->prn << endl;
        current = current->next;
    }
}

void list::remove() {
    long pno;
    cout << "Enter the PRN of the member to be removed: ";
    cin >> pno;

    if (president && president->prn == pno) {
        node* tmp = president;
        president = president->next;
        delete tmp;
        count--;
    } else {
        node* current = president;
        node* previous = nullptr;

        while (current && current->prn != pno) {
            previous = current;
            current = current->next;
        }

        if (current) {
            previous->next = current->next;
            if (current == secretary) {
                secretary = previous; // Update secretary if it was the last
            }
            delete current;
            count--;
        } else {
            cout << "Member Not found!" << endl;
        }
    }
}

void list::display_reverse() {
    node* current = president;
    if (!current) {
        cout << "No members to display!" << endl;
        return;
    }

    // Create a stack to reverse the display
    stack<node*> s;
    while (current) {
        s.push(current);
        current = current->next;
    }

    while (!s.empty()) {
        node* tmp = s.top();
        cout << "Name of the Member: " << tmp->name << endl;
        cout << "PRN of the Member: " << tmp->prn << endl;
        s.pop();
    }
}

int main() {
    list a;
    a.gethead();
    a.gettail();

    int c = 0;
    while (true) {
        cout << "Enter Choice:\n1.Add Member\n2.Delete Member\n3.Display No of Members\n4.Display Members\n5.Display in Reverse\n6.Exit\n";
        cin >> c;
        switch (c) {
        case 1: a.addmember(); break;
        case 2: a.remove(); break;
        case 3: a.display_count(); break;
        case 4: a.displaylist(); break;
        case 5: a.display_reverse(); break;
        case 6: return 0;
        default: cout << "Wrong choice\n"; break;
        }
    }
}

