document.addEventListener("DOMContentLoaded",function(){

    let my_form = document.getElementById("novo-usuario")

    let conf_senha = document.getElementById("confirmasenha")
    let senha = document.getElementById("senha")

    conf_senha.addEventListener("keypress", (event)=>{
        event.preventDefault()
        conf_senha.classList.remove("is-invalid")

        conf_senha.value += event.key

        console.log(event.key)

        if(conf_senha.value === senha.value){
            conf_senha.classList.add("is-valid")
            conf_senha.classList.remove("is-invalid")
        }else{
            conf_senha.classList.add("is-invalid")
        }
    })


    my_form.addEventListener("submit", (event)=>{
        event.preventDefault()

        let formData = new FormData()
        formData.append('usuario', my_form.usuario.value)
        formData.append('email', my_form.email.value)
        formData.append('senha', my_form.senha.value)

        if (conf_senha.value === senha.value) {
            fetch("/novo-usuario",
            {
                body:formData,
                method: "post"
            }).then((response) => response.json()).then((data) => {
                console.log(data)
                if(data.sucesso === true){
                    console.log(data.msg)

                }else{
                    console.log(data.msg)
                }
            })
        }
    })
})