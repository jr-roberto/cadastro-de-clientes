function login() {
    var form = document.createElement("div");
    var styleForm = form.style;
    form.setAttribute("id","form-login");
    styleForm.width = "450px";
    styleForm.height = "400px";

    main.insertBefore(form,null);
}