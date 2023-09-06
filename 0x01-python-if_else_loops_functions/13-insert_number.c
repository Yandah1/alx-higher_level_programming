#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: Pointer to the pointer to the head
 * @number: The number to be inserted
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = (listint_t *)malloc(sizeof(listint_t));

	if (new == NULL) 
	{
		printf("Memory allocation failed\n");
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	} else {
		listint_t *current = *head;

		while (current->next != NULL && number > current->next->n)
		{
			current = current->next;
		}

		new->next = current->next;
		current->next = new;
	}

	return (new);
}
