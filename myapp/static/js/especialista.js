const list_HorariosAtencion = async () => {

    try {
        const response=await fetch("http://127.0.0.1:8000/Lista_HorariosAtencion/")
        const data = await response.json();
      
        let content=``
        ;
        data.HorariosAtencion.forEach((HorariosAtencion,index)=>{
            content+=`
            <tr>
            
            <td>${HorariosAtencion.id_horario_atencion}</td>
            <td>${HorariosAtencion.dia_semana}</td>
            <td>${HorariosAtencion.fecha}</td>

            </tr>
            `
        })
        tablebody_HorariosAtencion.innerHTML=content;
    } catch (ex) {
        alert(ex);
        
    }
}

window.addEventListener("load", async () => {
    await list_HorariosAtencion();
})