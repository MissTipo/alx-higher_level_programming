#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: head of the node
 * Return: 0 if false, 1 if true
 */

int is_palindrome(listint_t **head)
{
	unsigned int list_len;
	listint_t *tmp;

	if (head == NULL || *head ==NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		list_len++;
	}
	return (0);
}
