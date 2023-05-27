let password_field = document.querySelector('#password')

// eye toggle section --------------------
let eye = document.querySelectorAll('.eye')
let eyeon = document.querySelector('.eyeon')
let eyeoff = document.querySelector('.eyeoff')

// 1 for show, 2 for hide
toggle_flag = 1
eye.forEach(element => {
    element.addEventListener('click', () => {
        if (toggle_flag == 1) {
            eyeon.classList.remove('active')
            eyeoff.classList.add('active')
            password_field.setAttribute('type', 'password')
            toggle_flag = 0
        } else {
            eyeon.classList.add('active')
            eyeoff.classList.remove('active')
            password_field.setAttribute('type', 'text')
            toggle_flag = 1
        }
    })
});


// password check section ------------ not useful for login page
let password_length = document.querySelector('.length')
let password_number = document.querySelector('.number')
let password_case = document.querySelector('.case')
let number_check = 0
let case_check = 0
let length_check = 0

let password_flag = false
function password_status() {
    let password = password_field.value
    if (/[0-9]/.test(password)) {
        password_number.style.color = 'green'
        number_check = 1

    } else {
        password_number.style.color = 'red'
        number_check = 0
    }

    if (/[a-z]/.test(password) && /[A-Z]/.test(password)) {
        password_case.style.color = 'green'
        case_check = 1
    } else {
        password_case.style.color = 'red'
        case_check = 0
    }

    if (password.length > 6) {
        password_length.style.color = 'green'
        length_check = 1
    } else {
        password_length.style.color = 'red'
        length_check = 0
    }

    if(number_check && case_check && length_check){
        password_flag = true
    }else{
        password_flag = false
    }
}

// form validation section ----------------
function validate_form() {
    return password_flag
}
