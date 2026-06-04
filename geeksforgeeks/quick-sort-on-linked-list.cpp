#define NULL 0
struct node {
    int data;
    struct node* next;
};

struct node* partition(struct node* head, struct node** first,
                       struct node** second) {
    struct node* pivot = head;
    struct node *fh = NULL, *ft = NULL;
    struct node *sh = NULL, *st = NULL;
    head = head->next;
    while (head != NULL) {
        if (head->data > pivot->data) {
            if (sh == NULL) {
                sh = head;
                st = head;
            } else {
                st->next = head;
                st = head;
            }
        } else {
            if (fh == NULL) {
                fh = head;
                ft = head;
            } else {
                ft->next = head;
                ft = head;
            }
        }
        head = head->next;
    }
    if (ft) ft->next = NULL;
    if (st) st->next = NULL;
    *first = fh;
    *second = sh;
    return pivot;
}

struct node* quicksort_rec(struct node* head) {
    if (head == NULL) return NULL;
    struct node *first = NULL, *second = NULL;
    struct node* pivot = partition(head, &first, &second);
    first = quicksort_rec(first);
    second = quicksort_rec(second);
    pivot->next = second;
    if (first == NULL) {
        return pivot;
    }
    struct node* p = first;
    while (p->next) {
        p = p->next;
    }
    p->next = pivot;
    return first;
}

void quickSort(struct node** headRef) {
    struct node* head = quicksort_rec(*headRef);
    *headRef = head;
}
