const btn_add_fila = document.getElementById("btn_add_fila")
 // OBSOLETA, ahora esta en el el .html de una btn_add_fila.addEventListener('click', añadir_fila)

document.querySelector('#tabla_recetada').addEventListener('click', (e) =>{
  sacar_fila(e.target);
});




//Sacar fila:

function sacar_fila(el){
  console.log(el)  
  if(el.classList.contains('delete')){
      
    el.parentElement.parentElement.remove();
    }
}