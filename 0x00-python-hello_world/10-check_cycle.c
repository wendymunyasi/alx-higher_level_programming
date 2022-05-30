#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle.
 * @list: pointer to the of linked list.
 *
 * Only these functions are allowed: write, printf, putchar,
 * puts, malloc, free
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
