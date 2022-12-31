const main = document.getElementById('main');

eel.expose(load_table);
function load_table(){
    eel.table_user()((output)=>{
        main.innerHTML = JSON.stringify(output)
    })
}

function novo_usuario(){
    var form = document.getElementById('form-cadastrar');
    var nome_usuario = form.querySelector('#nome_usuario').value;
    var senha = form.querySelector('#senha').value;

    if ( nome_usuario=='' || senha=='' ){
        main.innerHTML = 'Preenher todos os campos!'
    }else{
        
        eel.novo_cadastro(nome_usuario,senha)();

        main.innerHTML = `Usuario : ${nome_usuario} | Senha : ${senha}`;
    }
}