function login() {
    var form = document.createElement("form");
    var styleForm = form.style;
    styleForm.background = "red";
    
    if (main.clientWidth < 500){
        styleForm.width = main.clientWidth;
        styleForm.height = "100px";
    }

    main.innerHTML = "";
    main.insertBefore(form,null);
}