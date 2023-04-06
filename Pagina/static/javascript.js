const btn_add_fila = document.getElementById("btn_add_fila")
 // OBSOLETA, ahora esta en el el .html de una btn_add_fila.addEventListener('click', añadir_fila)

document.querySelector('#tabla_recetada').addEventListener('click', (e) =>{
  console.log(e.target);
  sacar_fila(e.target);
});

/*

function añadir_fila(){
    var fila = document.getElementsByClassName('oculto')[0];
    fila.classList.remove('oculto')
}
*/


/*
function añadir_fila2(){
    const tabla = document.getElementById('tabla_recetada')

    const row = document.createElement('tr')

    /* 
    row.innerHTML = `
    <td>
      <select class="form-select form-select-lg">
        <option selected disabled>Selecciona un ingrediente</option>
        
        {% for i in lista_productos %}
        <option value="{{i}}">"{{i}}"</option>
        "{{ i }}"
        {% endfor %}
      </select>
    </td>
    <td>
      <input id="Ing_Cant" type="number" class="contenedor">
    </td>
        <td class="alert alert-danger" id="btn_sacar_fila">
          <a href="#" class="delete">
            X
          </a>  
        </td>
    `
    
    
    row.innerHTML = '<td><select class="form-select form-select-lg"><option selected disabled>Selecciona un ingrediente</option>{% for i in lista_productos %}<option value="{{i}}">"{{i}}"</option>"{{ i }}"{% endfor %}</select></td><td><input id="Ing_Cant" type="number" class="contenedor"></td><td class="alert alert-danger" id="btn_sacar_fila">X</td>'
    tabla.appendChild(row);
}
 
*/
function sacar_fila(el){
  console.log(el)  
  if(el.classList.contains('delete')){
      el.parentElement.parentElement.classList.add('oculto');
    }
    //var fila = btn_sacar_fila.parentElement;
}


//Sacar fila:

