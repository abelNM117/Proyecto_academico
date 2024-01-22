// (function() {
//     var timeout = {{ SESSION_TIMEOUT }}; // Obtén el tiempo de inactividad desde la configuración de Django
//     var timer;
  
//     function resetTimer() {
//       clearTimeout(timer);
//       timer = setTimeout(logout, timeout * 1000);
//     }
  
//     function logout() {
//       // Realizar acciones de cierre de sesión, como redirigir al usuario a la página de cierre de sesión
//       window.location.href = "{% url 'logout' %}";
//     }
  
//     function init() {
//       resetTimer();
  
//       // Escucha eventos relevantes para detectar la actividad del usuario
//       window.addEventListener("mousemove", resetTimer);
//       window.addEventListener("keypress", resetTimer);
//       window.addEventListener("scroll", resetTimer);
//       // Agrega otros eventos según sea necesario para tu aplicación
  
//       // También puedes usar jQuery para escuchar eventos si está incluido en tu proyecto
//       // $(window).on("mousemove keypress scroll", resetTimer);
//     }
  
//     init();
//   })();
  