function login() {
    var form = document.createElement("div");
    var styleForm = form.style;
    form.setAttribute("id","form-login");
    styleForm.position = "absolute";
    styleForm.width = "50vw";
    styleForm.height = "60vh";
    styleForm.left = "50%";styleForm.top = "50%";
    styleForm.transform = "translate(-50%,-50%)"
    styleForm.background = "#000";
    form.innerHTML = "ismenia S2"
    styleForm.fontSize = "40px";
    styleForm.color = "#fff";

    main.insertBefore(form,null);
}