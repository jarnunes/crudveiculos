let dialogoConfirmarExclusaoVeiculo = (id, marca) => {
    let idModal = `modal_${id}`;
    let msg = `Confirmar a exclusão do veículo <strong>${marca}</strong>?`
    ModalUtils.appendChildModalToBody(`containerModal_${id}`, idModal, 'formModal', null, msg, null,
        `deleteVeiculo(${id})`);
    ModalUtils.openModal(idModal);
}

function deleteVeiculo(idVeiculo) {
    let id = idVeiculo;
    fetch(`deletar/${id}`, {
        method: 'DELETE',
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": DjangoUtils.getCookie("csrftoken"),
        }
    }).then(res => res.json())
        .then(data => {
            let idModal = `modal_${id}`;
            ModalUtils.closeAndRemoveModal(idModal, `containerModal_${id}`);
            AjaxUtils.refresh('cleanContainer');
        })
}

//Search
let search = document.getElementById('inputSearch')
search.addEventListener('keypress', (e) => {
    if (e.code === 'Enter') {
        const searchValue = e.target.value;
        const queryString = `search=${searchValue}`
        getVeiculos(queryString);
    }
})

// navigation
function navigate(page) {
    let parameters = JSUtils.getQueryParameters();
    parameters.set('page', page);
    getVeiculos(parameters);
}

function getVeiculos(queryString) {
    const url = `listar${queryString === null ? '' : '?' + queryString}`
    fetch(url, {
        method: 'GET',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    }).then(res => {
        let newurl = res['url'];
        window.history.pushState({path: newurl}, '', newurl);
        AjaxUtils.refresh('cleanContainer');
    })
}
