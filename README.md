# Reto-Procesamiento
 Miembros del equipo:
 
  - Manel Díaz

  - Ruben Alsasua

  - Eneko Saez

 Enlace a github: https://github.com/ManelDiaz/RetoCaptaci-n

 Pasos seguidos:

    Para poder desarrollar el proyecto se han seguido los siguientes pasos: 

      1. Para empezar, se instalaron las configuraciones iniciales incluyéndolas en los archivos requirements.txt
         
      2. Se realizaron las configuraciones necesarias y se levantaron los difernetes contenedores: generador, procesamiento, 
        validación y visualizacion. Se levantaron usando Docker

      3. Se realizó la configuración en Python del los diferentes servicios: generador, procesamientoy validación. 

      4. Se integró la base de datos de mongoDB en los contenedores. 

      5. En la parte de validación se implemnetó la un código que descartaba acaqullos generadores que tuvieran más potencia de 4000 
         
      6. Conectar la base de datos MongoDb con la aplicación MongodbCompass, para poder visualizar los datos de forma más clara.
      
   Instrucciones de uso:

    Para poder ejecutar el proyecto sería necesario clonar el repositorio mediante el comando 'git clone'. Después, es necesario levantar los contenedores 
    ejecutando el comando 'docker-compose up -d' en la terminal de WSL. 

    A continuación los datos se estarían generando y accediendo al siguiente url se puden visualizar los datos generados: http://localhost:8000/datos/. 

    Además, en la siguiente url, se abre la interfaz de FstApi con la cual es posible hacer get y post de los datos generados para almacenados en la db: 
    http://localhost:8000/docs. 

    En la siguiente url: http://localhost:8000/media_produccion/, se puede visualizar la media de potecia que tienen los generadores. 

    Por ultimo, tambien es posible ver la base de datos de mongodb mediante la línea de comandos mediante los siguientes comandos:
      1. docker exec -it mongodb mongosh --quiet
      2. use admin
      3. db.auth("admin", "admin")
      4. use parque_eolico
      5. db.datos_generadores.find().pretty()
    Para conectar la base de datos a la aplicación MongoDBCompass, es necesario utiliza el siguiente comando: mongodb://admin:admin@127.18.0.2:27017/parque_eolico?authSource=admin
   
   Posibles vías de mejora:
   
- Implementar monitorización en tiempo real de los servicios mediante logs y métricas, sin utilizar interfaces gráficas.
- Implementación de autentificación y seguridad. 
     
   Problemas encontrados:
   
- Se decició utilizar una solución alternativa para monitorización en tiempo real, pero no pudo implementarse correctamente debido a imprevistos en la conexión con la base de datos.
- Problemas con la integración de MongoDB como base de datos, debido a un error que salía en el conexionado de Docker y MongoDB. 

    Alternativas posibles:
    
- Emplear Prometheus para recolectar métricas y Alertmanager para gestionar alertas.
- Evaluar el uso de bases de datos relacionales, como PostgreSQL, para mejorar la robustez y la comunicación entre contenedores.
- Implementar autenticación basada en JWT y aplicar políticas de seguridad adicionales.
- Revisar y optimizar la configuración de red de Docker para mejorar la conexión a la base de datos.



