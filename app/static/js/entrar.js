document.addEventListener("DOMContentLoaded",function(){

    let my_form = document.getElementById("form-login")

    my_form.addEventListener("submit", (event)=>{
        event.preventDefault()

        let formData = new FormData()
        formData.append('email', my_form.email.value)
        formData.append('senha', my_form.senha.value)

        fetch("/login",
        {
            body:formData,
            method: "post"
        }).then((response) => response.json()).then((data) => {
            console.log(data)
            if (data.sucesso === true)
                window.location = "/perfil"
        })

    })

})