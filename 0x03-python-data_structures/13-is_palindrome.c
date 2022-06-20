#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a,
 * palindrome.
 * @head: double pointer to head of the list.
 *
 * Return: 1 if given list is a palindrome. 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int arr[10000];
	int i, n = 0;
	listint_t *traverse;

	if (head == NULL)
		return (0);

	/* copy numbers from linked list to arr */
	traverse = *head;
	while (traverse)
	{
		arr[n++] = traverse->n;
		traverse = traverse->next;
	}
	/* check if arr is a palindrome */
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - i - 1])
			return (0);
	}
	return (1);
}
