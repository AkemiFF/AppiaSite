var button = document.getElementById("contact_btn");
var button_off = document.getElementById("contact_btn_off");
var status = 0;
button.addEventListener("click", function () {
    if (status == 0) {
        form_contact_switch_on();
        status = 1;
    } else {

        form_contact_switch_off();
        status = 0;
    }

})

button_off.addEventListener("click", function () {
    form_contact_switch_off();
    status = 0;

})
function form_contact_switch_on() {
    var button = document.getElementById("contact_btn");
    var container = document.getElementById("contact_form");
    container.style.display = "block";
    button
}

function form_contact_switch_off() {
    var container = document.getElementById("contact_form");
    container.style.display = "none";
}