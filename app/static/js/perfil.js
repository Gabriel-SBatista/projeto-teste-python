document.addEventListener("DOMContentLoaded",function(){

    let btn_editar = document.getElementById("editar")
    let my_form = document.getElementById("editar-usuario")

    btn_editar.addEventListener("click", (event)=>{

        let usuario = document.getElementById("usuario")
        let email = document.getElementById("email")
        let botao = document.getElementById("salvar")

        botao.classList.remove("invisivel")
        usuario.readOnly = false
        email.readOnly = false
    })

    my_form.addEventListener("submit", (event)=>{

        let json = {
            "usuario": my_form.usuario.value,
            "email": my_form.email.value
        }

        fetch("/editar",
        {
            body: JSON.stringify(json),
            method: "put",
            headers: { 'Content-Type': 'application/json' }
        }).then((response) => response.json()).then((data) => {
            console.log(data)
            if (data.sucesso === true)
              location.reload()
            else
               console.log("Deu nao!")
        })
    })
})