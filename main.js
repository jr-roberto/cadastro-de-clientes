const main = document.querySelector("#main");

function telaLogin(){

    var form = document.createElement("form");
    form.textContent = 'Formulario de login';

    var idInputs = ["form-inp-usuario","form-inp-senha","form-btn-login"]

    for (var i = 0 ; i < 3 ; i++){
        var input = document.createElement("input");
        var id = idInputs[i];

        if (id !== "form-btn-login"){
            
            input.setAttribute("id",id);
            input.setAttribute("type","text");

        
        } else {

            input.setAttribute("id",id);
            input.setAttribute("type","submit");
        }

        form.insertBefore(input,null);
    }

    main.insertBefore(form,null);

}