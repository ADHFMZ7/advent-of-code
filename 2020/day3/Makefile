CC = clang++
CFLAGS = -std=c++20 -Wall -Werror

SRCS = main.cpp
EXEC = out 

$(EXEC): $(SRCS)
	$(CC) $(CFLAGS) $(SRCS) -o $(EXEC)

clean:
	rm -f $(EXEC)
