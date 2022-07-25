# ProyectoFinal

Comision 37190 CODERHOUSE PYTHON.

Creamos esta pagina web en entre: Agustin Sanchez, Gabriel Salazar y Jessica Nava.

Se tomó como base uno de los MVT anteriores realizados y a ese mismo le agregamos todo lo solicitado como proyecto final, decidimos elegir uno de entre los tres mvt entregados con anterioridad seleccionando el que creímos mas apto para agregar los nuevos requirimientos, por lo cual debajo voy a estar describiendo lo que cada uno realizó para este proyecto final:

    -Agustin Sanchez realizó la parte de login, log out y register.
    -Gabriel Salazar realizó la parte del CRUD(create, read, delete and update).
    -Jessica Nava realizó la parte de Avatar, Blog, About y la modificación de la barra de navegación.

La funcionalidad de la pagina trata acerca de un servicio veterinario en el cuál puedes agregar la información (nombre, raza, edad) de tu mascota (se cuenta con las opciones de perro, gato y ave) para que tus mascotas tengan un servicio de veterinario por turno.

La pagina cuenta con las opciones para registrarse como nuevo usuario, un login para usuarios con una cuenta previamente hecha así como la opción de editar el perfil podiendo agregar o modificar nombre, apellido, email o contraseña y logout para cerrar sesión, también te da la opción de volver a iniciar sesión una vez cerrada. Para el registro se colocó como campos username y password, teniendo una doble verificación de password.

La aplicación cuenta con un sistema de CRUD para poder eliminar o editar el animal que está cargado a la base de datos, en este caso solo lo colocamos para el menú gatos donde puedes ver el listado de gatos registrados, editarlos o eliminarlos.

Tambien cuenta con un blog para poder realizar publicaciones sencillas en la pagina.

Algunos de los problemas que se nos presentaron fue que para la creacion del usuario, al no tener un avatar ese nuevo usuario la pagina web rompe al querer ir al inicio, por lo que el admin debe agregarle una imagen como avatar para que no suceda esto al querer ir a la opción de inicio, en el video se muestra a detalle un usuario con avatar puede entrar al inicio sin que rompa a diferencia de uno que sin avatar.

También se tuvo problemas con la barra de navegación que un inicio al ingresar a alguna otra url no nos dejaba volver a alguna otra opción del menú, se tenía que escribir de nuevo en la barra del navegador AppCoder para regresar al inicio y cambiar a otro menú, ya sea que estabamos en la solapa de blog y no podiamos ingresar a registrarse, iniciar sesion o cualquier otra, finalmente lo logramos solucionar modificando las etiquetas en la plantilla de padre y creando nuevos apartados para el mismo en el CSS.