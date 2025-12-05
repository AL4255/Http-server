
#include <stdio.h>      // Standard input/output functions (printf, etc.)
#include <stdlib.h>     // Standard library (exit, malloc, etc.)
#include <string.h>     // String manipulation functions (strlen, strcpy, etc.)
#include <unistd.h>     // UNIX standard functions (close, read, write, etc.)
#include <sys/socket.h> // Socket functions (socket, bind, listen, accept)
#include <netinet/in.h> // Internet protocol family structures
#include <sys/wait.h>   // For wait() function to handle child processes
#include <signal.h>     // For signal handling (cleaning up zombies)
