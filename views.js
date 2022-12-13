function login() {
    var form = document.createElement("div");
    var styleForm = form.style;
    form.setAttribute("id","form-login");
    form.innerHTML = "Click - me";
    styleForm.fontSize = "50px";
    styleForm.textAlign = "center";
    styleForm.top = "20px";
    styleForm.position = "absolute";
    styleForm.width = "50vw";
    styleForm.height = "60vh";
    styleForm.left = "50%";styleForm.top = "50%";
    styleForm.transform = "translate(-50%,-50%)"
    styleForm.background = "#000";

    main.insertBefore(form,null);
}