Reto 01 Calculadora de sumas.

Descripción.
El programa lo que hara es de un archivo o cualquier valor que ingresemos limpiara valores que no sean acorde a ellos, ya sea truncar numeros, separarlos correctamente, limpiar valores que contengan caracteres no validos, ignorar espacios en blanco, etc.

Intrucciones de uso.
Para usarlo puedes ejecutarlo y colocar valores de manera manual por medio del comando
"python main.py" y con ello colocaras cualquier valor que quieras limpiar un ejemplo seria:

"15.6"

El programa te devolvera el valor como: "15"
Esto es gracias a la funcion de truncar los valores.

Ahora ya sea que quieras ejecutar algun archivo solo con el comando seria:
"Get-Content nombredetuarchivo.txt | python main.py"

Los valores que contengas ahi mismo el programa te los devolvera por completo limpios.

Y si deseas que ese resultado se guarde solo ejecuta el comando:
Get-Content nombredetuarchivo.txt | python main.py > nuevonombredearchivo.txt

Solo que al final tu decides que nombre colocarle al nuevo txt.

Ejemplo de entrada y salida.
Ahora como ejemplo sera el archivo de entrada.txt:

=== ENTRADA ===
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15  
0,0,0
-1,-2,-3
abc,def
3.99
-0.5,0.5
,1,2,
100

El programa nos da como resultado los valores por completo limpios:

0
6
10
0
6
19
8
30
0
-6
0
3
0
3
100


Autor.
Guzmán Meza José Daniel
