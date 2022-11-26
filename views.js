function login() {
    var form = document.createElement("form");
    var styleForm = form.style;
    styleForm.border = "solid 1px";
    
    if (main.clientWidth < 500){
        styleForm.width = main.clientWidth;
        styleForm.height = main.clientHeight;
    }

    main.innerHTML = "";
    main.innerHTML = form;
}