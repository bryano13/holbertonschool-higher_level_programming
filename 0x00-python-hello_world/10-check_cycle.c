#include "lists.

/**
 * check_cycle - checks if there is a cycle
 * @list: list to examinate
 * Return: 1 if true, 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *current;

	head = list;
	current = list;

	while (head && current && current->next)
	{
		current = current->next->next;
		if (head == current)
			return (1);

		head = head->next;		
	}

	return (0);
}
