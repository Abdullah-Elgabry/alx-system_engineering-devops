#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>


/**
 * infinite_while - this func will make an endless loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - this func will init a 5 process
 * Return: 0
 */
int main(void)
{
	pid_t pid;

	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (EXIT_SUCCESS);
}
