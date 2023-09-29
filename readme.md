# Aplicación Web de Mensajería
Este repositorio contiene el código fuente de una aplicación web de mensajería similar a Discord.

### Usos
Se proporciona una API REST que permite a la interfaz de usuario interactuar con la base de datos y acceder a las funcionalidades de la aplicación. 
Dentro de las funcionalidades del sistema encontramos:

- **Registro e Inicio de Sesión**: Los usuarios pueden registrarse y luego iniciar sesión en la aplicación.

- **Exploración de Servidores y Canales**: Los usuarios pueden crear o unirse a servidores y crear canales dentro de esos servidores.

- **Interacción en Chats**: Los usuarios pueden participar en conversaciones en los canales, enviando y recibiendo mensajes.

- **Perfil de Usuario**: Los usuarios pueden actualizar sus datos personales y su imagen de perfil en su perfil de usuario.


### Componentes
La aplicación está diseñada utilizando el framework Flask de Python. Sigue el patrón de diseño Modelo-Vista-Controlador (MVC) y utiliza MySQL como base de datos, debes configurar las credenciales de la base de datos en database.py. A continuación, se describen los principales componentes:

- **Controladores** (Controllers): Los controladores son responsables de manejar las solicitudes HTTP entrantes y coordinar la lógica de la aplicación. Están ubicados en el directorio controllers.

- **Modelos** (Models): Los modelos representan la estructura de los datos de la aplicación y gestionan la interacción con la base de datos MySQL. Están ubicados en el directorio models.

- **Rutas** (Routes): Las rutas definen las URL y los métodos HTTP para acceder a las diversas funcionalidades del backend. Están ubicadas en el directorio routes.

- **Base de Datos** (MySQL): La aplicación utiliza MySQL como base de datos para almacenar y recuperar información, incluyendo datos de usuarios, servidores, canales y mensajes. La configuración de la base de datos se encuentra en config.py


# Developers

German Aguirre
Daniela Farfan
Mariana Loyola
Fabricio Garcia
