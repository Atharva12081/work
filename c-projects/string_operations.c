/*
 * File: string_operations.c
 * Description: Implementation of string manipulation functions
 * Author: Atharva
 * Date: 2025-02-05
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LENGTH 1000

// Function prototypes
int stringLength(const char *str);
void stringCopy(char *dest, const char *src);
void stringConcat(char *dest, const char *src);
int stringCompare(const char *str1, const char *str2);
void stringReverse(char *str);
int isPalindrome(const char *str);
void stringToUpper(char *str);
void stringToLower(char *str);
int countWords(const char *str);
char* removeWhitespace(const char *str);
void reverseWords(char *str);

int stringLength(const char *str) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

void stringCopy(char *dest, const char *src) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

void stringConcat(char *dest, const char *src) {
    int destLen = stringLength(dest);
    int i = 0;
    while (src[i] != '\0') {
        dest[destLen + i] = src[i];
        i++;
    }
    dest[destLen + i] = '\0';
}

int stringCompare(const char *str1, const char *str2) {
    int i = 0;
    while (str1[i] && str2[i]) {
        if (str1[i] != str2[i]) {
            return str1[i] - str2[i];
        }
        i++;
    }
    return str1[i] - str2[i];
}

void stringReverse(char *str) {
    int len = stringLength(str);
    int start = 0, end = len - 1;
    
    while (start < end) {
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
}

int isPalindrome(const char *str) {
    int len = stringLength(str);
    int start = 0, end = len - 1;
    
    while (start < end) {
        if (str[start] != str[end]) {
            return 0;
        }
        start++;
        end--;
    }
    return 1;
}

void stringToUpper(char *str) {
    int i = 0;
    while (str[i]) {
        str[i] = toupper(str[i]);
        i++;
    }
}

void stringToLower(char *str) {
    int i = 0;
    while (str[i]) {
        str[i] = tolower(str[i]);
        i++;
    }
}

int countWords(const char *str) {
    int count = 0;
    int inWord = 0;
    
    while (*str) {
        if (isspace(*str)) {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            count++;
        }
        str++;
    }
    return count;
}

char* removeWhitespace(const char *str) {
    int len = stringLength(str);
    char *result = (char*)malloc(len + 1);
    int j = 0;
    
    for (int i = 0; i < len; i++) {
        if (!isspace(str[i])) {
            result[j++] = str[i];
        }
    }
    result[j] = '\0';
    return result;
}

void reverseWords(char *str) {
    int len = stringLength(str);
    int start = 0;
    
    stringReverse(str);
    
    for (int i = 0; i <= len; i++) {
        if (str[i] == ' ' || str[i] == '\0') {
            int end = i - 1;
            while (start < end) {
                char temp = str[start];
                str[start] = str[end];
                str[end] = temp;
                start++;
                end--;
            }
            start = i + 1;
        }
    }
}

int main() {
    char str1[MAX_LENGTH] = "Hello";
    char str2[MAX_LENGTH] = "World";
    char str3[MAX_LENGTH];
    
    printf("String length of '%s': %d\n", str1, stringLength(str1));
    
    stringCopy(str3, str1);
    printf("Copied string: %s\n", str3);
    
    stringConcat(str1, " ");
    stringConcat(str1, str2);
    printf("Concatenated string: %s\n", str1);
    
    char palindrome[] = "racecar";
    if (isPalindrome(palindrome)) {
        printf("%s is a palindrome\n", palindrome);
    } else {
        printf("%s is not a palindrome\n", palindrome);
    }
    
    char testStr[] = "Hello World";
    stringToUpper(testStr);
    printf("Uppercase: %s\n", testStr);
    
    stringToLower(testStr);
    printf("Lowercase: %s\n", testStr);
    
    printf("Word count: %d\n", countWords(testStr));
    
    char *noSpace = removeWhitespace(testStr);
    printf("Without whitespace: %s\n", noSpace);
    free(noSpace);
    
    return 0;
}

