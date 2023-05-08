#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

/**
 * struct listptr_s - singly linked list of pointers
 * @ptr: pointer to a data element
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listptr_s
{
void *ptr;
struct listptr_s *next;
} listptr_t;

/* Print Functions */
size_t print_listint(const listint_t *h);
size_t print_listptr(const listptr_t *h, void (*print_func)(void *));
void print_string(void *str);
void print_char(void *ch);

/* Manipulation Functions */
listint_t *add_nodeint(listint_t **head, const int n);
listptr_t *add_nodeptr(listptr_t **head, void *ptr);
listint_t *add_nodeint_end(listint_t **head, const int n);
listptr_t *add_nodeptr_end(listptr_t **head, void *ptr);
void free_listint(listint_t *head);
void free_listptr(listptr_t *head, void (*free_func)(void *));
void free_string(void *str);
void free_char(void *ch);

/* Advanced Functions */
size_t listint_len(const listint_t *h);
listint_t *find_listint_loop(listint_t *head);
listint_t *reverse_listint(listint_t **head);
void print_listint_safe(const listint_t *head);
size_t free_listint_safe(listint_t **h);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
