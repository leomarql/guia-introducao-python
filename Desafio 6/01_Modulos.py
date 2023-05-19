
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Printar o Sistema Operacional que voce esta usando:
# YOUR CODE HERE
print("Sistema operacional: ", sys.platform)

# Printar a versão de Python que voce esta usando:
# YOUR CODE HERE
print("Versao do python: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Printar a process Id atual
# YOUR CODE HERE
print("Process ID: ", os.getpid())

# Printar o atual diretório:
# YOUR CODE HERE
print("Atual diretorio: ", os.getcwd())

# Printar o nome da maquina
# YOUR CODE HERE
print("Nome da maquina: ", os.uname().nodename)
