# Reto-Procesamiento

Miembros del equipo:
- Manel Díaz
- Rubén Alsasua
- Eneko Sáez

Enlace a GitHub: https://github.com/rubenalsasua/Reto-Procesamiento

Pasos seguidos:
1. Para empezar, se instalaron las configuraciones iniciales incluyéndolas en los archivos requirements.txt.
2. Se realizaron las configuraciones necesarias y se levantaron los diferentes contenedores: generador, procesamiento, validación y visualización (usando Docker).
3. Se realizó la configuración en Python de los diferentes servicios: generador, procesamiento y validación.
4. Se integró la base de datos de MongoDB en los contenedores. Para almacenar los datos se creo una base de datos principal llamada parque_eolico y dentro de ella,
   se crearon 2 colecciones: datos_generadores(almacena todos los datos generados por los generadores) y datos_aggregados (almacena los datos procesados como
   agregaciones, media de cada metica por minuto). 
5. En la parte de validación se implementó un código que descartaba aquellos generadores que tuvieran más potencia de 4000.
6. Se conectó la base de datos MongoDB con la aplicación MongoDBCompass para visualizar los datos de forma más clara.

Instrucciones de uso:
- Clonar el repositorio con el comando `git clone`.
- Levantar los contenedores ejecutando `docker-compose up -d` en la terminal de WSL.
- Acceder a los datos generados en: http://localhost:8000/datos/.
- Acceder a la interfaz de FastAPI en: http://localhost:8000/docs para realizar operaciones GET y POST.
- Consultar la media de potencia en: http://localhost:8000/media_produccion/.
- Visualizar la base de datos de MongoDB ejecutando:
  1. `docker exec -it mongodb mongosh --quiet`
  2. `use admin`
  3. `db.auth("admin", "admin")`
  4. `use parque_eolico`
  5. `db.datos_generadores.find().pretty()` para ver los datos generados por los generadores.
  6. `db.datos_aggregados.find().pretty()` para ver los datos agregados 
- Conectar la base de datos a MongoDBCompass usando:
  `mongodb://admin:admin@127.18.0.2:27017/parque_eolico?authSource=admin`

Posibles vías de mejora:
- Implementar monitorización en tiempo real de los servicios mediante logs y métricas, sin interfaces gráficas.
- Implementar autenticación y seguridad.

Problemas encontrados:
- Se decidió utilizar una solución alternativa para monitorización en tiempo real, pero no se implementó correctamente debido a imprevistos en la conexión con la base de datos.
- Problemas con la integración de MongoDB, debido a un error en el conexionado de Docker y MongoDB.

Alternativas posibles:
- Emplear Prometheus para recolectar métricas y Alertmanager para gestionar alertas.
- Evaluar el uso de bases de datos relacionales, como PostgreSQL, para mejorar la robustez y la comunicación entre contenedores.
- Implementar autenticación basada en JWT y aplicar políticas de seguridad adicionales.
- Utilizar Grafana para visualizar mejor los datos.



