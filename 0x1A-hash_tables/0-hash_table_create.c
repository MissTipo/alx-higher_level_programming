#include "hash_tables.h"

/**
 * hash_table_create - Creates a new hash table
 * @size: the size of the array
 *
 * Return: Null if an error occurs, otherwise the
 *         the pointer to the hash table
 *
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int idx = 0;
	hash_table_t *ht = malloc(sizeof(hash_table_t));
	hash_node_t **arr = malloc(sizeof(hash_node_t *) * size);

	if (ht == NULL)
		return (NULL);
	if (arr == NULL)
		return (NULL);

	for (; idx < size; idx++)
		arr[idx] = NULL;
	ht->size = size;
	ht->array = arr;

	return (ht);
}

