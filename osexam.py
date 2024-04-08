import os

# Example 1: Running a command
# This example shows how to run a command using os.system()
# In this case, we're running the "dir" command to list the files in the current directory
os.system("dir")

# Example 2: Running a command with arguments
# This example shows how to run a command with arguments using os.system()
# In this case, we're running the "echo %cd%" command to print the current working directory
os.system("echo %cd%")

# Example 3: Storing the command output
# This example shows how to store the output of a command using os.system()
# In this case, we're running the "cd" command followed by the "echo %cd%" command to get the current working directory
# The output of the command is stored in the variable "output"
output = os.popen("cd && echo %cd%").read()
print(output)