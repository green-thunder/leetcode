#include <stdio.h>
#include <stdlib.h>

typedef struct HashNode {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

#define TABLE_SIZE 1000

HashNode* hashTable[TABLE_SIZE];

int hashFunction(int key) {
    if (key < 0) {
        key = -key;
    }
    return key % TABLE_SIZE;
}

void insert(int key, int value) {
    int hashIndex = hashFunction(key);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = hashTable[hashIndex];
    hashTable[hashIndex] = newNode;
}

int search(int key) {
    int hashIndex = hashFunction(key);
    HashNode* current = hashTable[hashIndex];
    while (current != NULL) {
        if (current->key == key) {
            return current->value;
        }
        current = current->next;
    }
    return -1;
}

void freeHashTable() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        HashNode* current = hashTable[i];
        while (current != NULL) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
        hashTable[i] = NULL;
    }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 0;
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int index = search(complement);
        if (index != -1) {
            *returnSize = 2;
            int* result = (int*)malloc(2 * sizeof(int));
            result[0] = index;
            result[1] = i;
            return result;
        }
        insert(nums[i], i);
    }
    return NULL;
}

int main() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable[i] = NULL;
    }

    int nums[] = {1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 41};
    int target = 51;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;

    int* result = twoSum(nums, numsSize, target, &returnSize);

    if (returnSize == 2) {
        printf("Indices: [%d, %d]\n", result[0], result[1]);
        free(result);
    } else {
        printf("No two indices found.\n");
    }

    freeHashTable();

    return 0;
}
