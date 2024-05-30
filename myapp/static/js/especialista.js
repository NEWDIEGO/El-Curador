let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5] },
        { orderable: false, targets: [3, 4, 5, 6] },
        { searchable: false, targets: [6] }
    ],
    language: {
        "sProcessing": "Procesando...",
        "sLengthMenu": "Mostrar _MENU_ registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "Buscar:",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": "Siguiente",
            "sPrevious": "Anterior"
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        },
        "buttons": {
            "copy": "Copiar",
            "colvis": "Visibilidad"
        }
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await list_HorariosAtencion();

    dataTable = $('#datatable-HorariosAtencion').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
}

const list_HorariosAtencion = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/Lista_HorariosAtencion/")
        const data = await response.json();

        let content = ``;
        data.HorariosAtencion.forEach((HorariosAtencion, index) => {
            content += `
            <tr>
                <td>${HorariosAtencion.id_horario_atencion}</td>
                <td>${HorariosAtencion.dia_semana}</td>
                <td>${HorariosAtencion.fecha}</td>
                <td>${HorariosAtencion.hora_inicio}</td>
                <td>${HorariosAtencion.hora_fin}</td>
                <td>${HorariosAtencion.duracion_cita}</td>
                <td>
                <input class="btn btn-sm btn-primary" type="button" value="Notificar" onClick="verLista()"></input>
            </td>
            </tr>
            `
        })
        document.getElementById('tablebody_HorariosAtencion').innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
}

window.addEventListener("load", async () => {
    await initDataTable();
})

function verPerfil() {
    window.location.href = '/Especialista/Perfil/';
}

function verLista() {
    window.location.href = '/Especialista/Lista_de_espera/';
}

function CerrarSesion() {
    window.location.href = '//';
}
