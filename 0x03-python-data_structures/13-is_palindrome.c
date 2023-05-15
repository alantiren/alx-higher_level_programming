#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *node = *head;
listint_t *next;

while (node)
{
next = node->next;
node->next = prev;
prev = node;
node = next;
}
*head = prev;
return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev_slow = *head;
listint_t *second_half = NULL;
int is_palindrome = 1;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
slow = slow->next;
}
second_half = reverse_listint(&slow);
listint_t *tmp = second_half;
listint_t *node = *head;
while (second_half != NULL)
{
if (node->n != second_half->n)
{
is_palindrome = 0;
break;
}
node = node->next;
second_half = second_half->next;
}
reverse_listint(&tmp);
prev_slow->next = tmp;
return (is_palindrome);
}
