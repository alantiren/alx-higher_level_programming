#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *second_half, *mid_node;
	int is_palindrome = 1;

	slow = *head;
	fast = *head;
	prev_slow = NULL;

	/* Find the middle node of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/* If the number of nodes is odd, move slow pointer to the next node */
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the linked list */
	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);

	/* Compare the first half and reversed second half of the linked list */
	is_palindrome = compare_lists(*head, second_half);

	/* Restore the original linked list */
	reverse_list(&second_half);

	/* If the number of nodes is odd, link back the mid node */
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the linked list
 *
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 *
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;

		list1 = list1->next;
		list2 = list2->next;
	}

	if (list1 == NULL && list2 == NULL)
		return 1;

	return 0;
}
