/* global bootstrap: false */
(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
        new bootstrap.Tooltip(tooltipTriggerEl)
    })
})()

/**
 * Função para enviar requisições ao back com o número da paginação ao clicar em algum botão do menu de navegação da tabela de resultados
 * @param page
 */
function navigate(page) {
    fetch(`listar?page=${page}`, {
        method: 'GET',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    })
        .then(res => {
            let newurl = res['url'];
            window.history.pushState({path: newurl}, '', newurl);
            AjaxUtils.refreshContainer();
        })
}


// show/hide navitagion
let btn = document.getElementById('btnMenu')
let nav = document.querySelector('div.base-container > nav')

btn.addEventListener('click', () => {
    nav.classList.toggle('display-hide')
})
