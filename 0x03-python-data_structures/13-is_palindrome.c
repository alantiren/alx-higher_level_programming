#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
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

if (fast != NULL) // odd number of nodes, skip the middle one
{
slow = slow->next;
}
second_half = reverse_listint(&slow);
listint_t *tmp = second_half;
listint_t *current = *head;
while (second_half != NULL)
{
if (current->n != second_half->n)
{
is_palindrome = 0;
break;
}
current = current->next;
second_half = second_half->next;
}
reverse_listint(&tmp); // restore the second half
prev_slow->next = tmp; // reconnect the first half and the restored second half
return (is_palindrome);
}
