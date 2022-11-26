function login() {
    var form = document.createElement("form");
    var styleForm = form.style;
    styleForm.background = "blue";
    
    if (main.clientWidth < 500){
        styleForm.width = main.clientWidth;
        styleForm.height = main.clientHeight;
    }

    main.innerHTML = "";
    main.insertBefore(form,null);
}