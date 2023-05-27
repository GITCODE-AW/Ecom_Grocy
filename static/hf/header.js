let header_menu = document.querySelector('#header_menu')
let header_nav = document.querySelector('nav')
let header_search = document.querySelector('#header_search')
let searchbar = document.querySelector('.searchbar')

header_menu.onclick = ()=>{
    header_nav.classList.toggle('active')
    searchbar.classList.remove('active')
}

header_search.onclick = ()=>{
    searchbar.classList.toggle('active')
    header_nav.classList.remove('active')
}