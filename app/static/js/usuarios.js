function confirmaExcluirUsuario(_id, nome){
    let span = document.getElementById("nome_usuario")
    let input = document.getElementById("id_usuario")
    let modal = new bootstrap.Modal(document.getElementById("modal-confirm"))

    input.value = _id
    span.innerText = nome
    modal.show()
}

function excluirUsuario(){
    let _id = document.getElementById("id_usuario")

    fetch("/excluir_usuario/" + _id.value,
    {
        method:"delete"
    }).then((response) => response.json()).then((data) => {
        if (data.sucesso === true)
            location.reload()
    })
}

document.addEventListener("DOMContentLoaded",function(){

})