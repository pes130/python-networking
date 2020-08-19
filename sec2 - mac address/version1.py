#!/usr/bin/python3
import subprocess
subprocess.call("ls", shell=True)

subprocess.call(["ls","-l"])

# USar call está heredado de python 2, ahora se usa run, que te permite interactuar con la salida
# Devuelve una instancia de CompletedProcess, con info sobre el proceso como el código de salida y la salida
print("Con run")
completed = subprocess.run(["ls","-l"])
print("Return code:",completed.check_returncode)

# PUedes usar el parámetro shell=True para que subprocess genere un proceso intermedio que luego ejecuta el comando.
# Esto significa que las variables y otras características especiales de shell se procesan en la cadena de comando antes de ejecutar el comando

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

# Capturar la salida de un proceso
completed = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)