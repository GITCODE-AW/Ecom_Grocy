// phone number validation section ---------------
let phone_validation_flag = false
let phone_validate_signal = document.getElementById("phone_validate_signal")
let phone = document.getElementById('phone_s')

function phone_validation() {
    if (phone.value.length == 10) {
        phone_validation_flag = true
        phone_validate_signal.style.color = 'green'
    } else {
        phone_validation_flag = false
        phone_validate_signal.style.color = 'red'
    }

    phone_validate_signal.innerHTML = `${phone.value.length}`

}

// form validation using above sectin flags
function Account_validation() {
    return phone_validation_flag
}