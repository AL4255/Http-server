
#include <stdio.h>      // Standard input/output functions (printf, etc.)
#include <stdlib.h>     // Standard library (exit, malloc, etc.)
#include <string.h>     // String manipulation functions (strlen, strcpy, etc.)
#include <unistd.h>     // UNIX standard functions (close, read, write, etc.)
#include <sys/socket.h> // Socket functions (socket, bind, listen, accept)
#include <netinet/in.h> // Internet protocol family structures
#include <sys/wait.h>   // For wait() function to handle child processes
#include <signal.h>     // For signal handling (cleaning up zombies)


define PORT 8080       // Define the port our server will listen on
#define BUFFER_SIZE 1024 // Size of our read buffer

  // Signal handler to clean up zombie child processes
// When a child process dies, the OS sends SIGCHLD signal to parent
// This handler automatically calls wait() to clean up the zombie
void handle_sigchld(int sig) {
    // waitpid with WNOHANG means "clean up any dead children without blocking"
    // -1 means wait for ANY child process
    // Loop to handle multiple children that might have died
    while (waitpid(-1, NULL, WNOHANG) > 0);
}
