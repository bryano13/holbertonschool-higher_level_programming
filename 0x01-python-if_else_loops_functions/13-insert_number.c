#include "lists.h"

/**
 * insert_node - Inserts an integer in a determinated node
 * @head: head of the list
 * @number: number to add
 * Return: List
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;
	
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (temp != NULL)
	{
		if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			break;
		}
		if (temp->next == NULL)
		{
			temp->next = new;
			break;
		}
		temp = temp->next;
	}

	return (new);
}
