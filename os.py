import os

#command_line = 'mkdir /opt/new_folder && chmod_R 777/opt/new_folder' 
#linea = str(command_line)
#os.system(linea)

#command_line = 'mkdir /home/labservidores/Documentos/new_folder'
#command_line2 = 'chmod -R 777 /home/labservidores/Documentos/new_folder/' 
#command_line3 = 'chown -R root: /home/labservidores/Documentos/new_folder' 
#linea = str(command_line +" && "+ command_line2 +" && "+ command_line3)
#os.system(linea)

comando = str(input("Digita el nombre de usuario: "))
command_line = 'sudo useradd '+comando
linea = str (command_line)
os.system(linea)
direccion = '/home/labservidores/Documentos/'+comando
direccion_actual = str ('sudo mkdir '+direccion)
os.system(direccion_actual)
permisos = ' sudo chown '+comando+ ':'+comando+" -R "+direccion
permisos_s = str (permisos)
os.system(permisos_s)
os.system('cat /etc/passwd')
os.system('ls -lh')
print ( "Creaste el usuario, proseguimos asignandolo a una carpeta en esta ruta")