(function() {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
      btn.addEventListener("click",(evento)=>{
        const confirmacion=confirm("¿Seguro de eliminar el usuario?");
        if (!confirmacion) {
          evento.preventDefault();
        }
      });
    });
})();

