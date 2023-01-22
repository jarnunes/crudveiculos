let dialogoConfirmarExclusaoVeiculo = (id, marca) => {
    let idModal = `modal_${id}`;
    let msg = `Confirmar a exclusão do veículo <strong>${marca}</strong>?`
    ModalUtils.appendChildModalToBody(`containerModal_${id}`, idModal, 'formModal', null, msg, enableDisableDeleteElement,
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
            AjaxUtils.refresh('cardsContainer');
            AjaxUtils.refresh('messages');
            afterDoAction();
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
function navigate(page, ...callbacks) {
    let parameters = JSUtils.getQueryParameters();
    parameters.set('page', page);

    // function called to return next values
    callbacks.forEach(callback => callback(parameters))
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
        applyCssOnSelectedElements()
    })
}

/*------------------*/
const selectedClass = 'selected-card'
const disabledClass = 'disabled'
let lista = []
let navigatorList = document.getElementsByClassName('page-link')
Array.from(navigatorList).forEach(item => {
    item.addEventListener('click', () => {
        applyCssOnSelectedElements()
    })
})

let counter = 0

function applyCssOnSelectedElements() {
    counter++
    if (lista.length === 0) {
        lista = []
    }
    setTimeout(() => {
        lista.forEach(element => {
            if (JSUtils.existsElement(element) && !document.getElementById(element).classList.contains(selectedClass)) {
                toggleSelected(element)
            } else {
                if (counter < 100)
                    applyCssOnSelectedElements()
            }
        })
    }, 50)
}

function selectCard(element) {
    if (lista.includes(element)) {
        let index = lista.indexOf(element)
        lista.splice(index, 1)
    } else {
        lista.push(element)
    }
    toggleSelected(element)
    enableDisableEditElement()
    enableDisableDeleteElement()
    enableDisableExport()
}

function selectUnselectAll(elementList) {
    if (containsAll(elementList, lista)) {
        lista.forEach(element => {
            toggleSelected(element)
            lista = []
        })
    } else {
        lista = elementList
        applyCssOnSelectedElements()
    }
    enableDisableDeleteElement()
    enableDisableExport()
}


function containsAll(firstArray, secondArray) {
    return firstArray.every(v => secondArray.includes(v))
}

function toggleSelected(idElement) {
    if (JSUtils.existsElement(idElement)) {
        let element = document.getElementById(idElement)
        element.classList.toggle(selectedClass)
    }
}

function enableDisableEditElement() {
    let editElement = document.getElementById('editAction')
    if (lista.length === 1) {
        editElement.classList.remove(disabledClass)
    } else {
        editElement.classList.add(disabledClass)
    }
}

function enableDisableDeleteElement() {
    let deleteElement = document.getElementById('deleteAction')
    if (lista.length > 0) {
        deleteElement.classList.remove(disabledClass)
    } else {
        deleteElement.classList.add(disabledClass)
    }
}

function enableDisableExport() {
    let exportElement = document.getElementById('exportAction')
    if (lista.length > 0) {
        exportElement.classList.remove(disabledClass)
    } else {
        exportElement.classList.add(disabledClass)
    }
}

function changeViewDisplay() {
    let classGrid = 'bi-grid'
    let classList = 'bi-view-list'
    let classCardGrid = ['row-cols-1', 'row-cols-md-2', 'row-cols-lg-3', 'g-3']

    let elements = document.getElementsByClassName('car-info-card')
    Array.from(elements).forEach(element => {
        console.log(element.classList)
    })

    let elementIcon = document.getElementById('changeViewId')
    if (elementIcon.classList.contains(classGrid)) {
        elementIcon.classList.remove(classGrid)
        elementIcon.classList.add(classList)
    } else {
        elementIcon.classList.remove(classList)
        elementIcon.classList.add(classGrid)
    }

    let cardsContainer = document.getElementById('cardsContainer')
    classCardGrid.forEach(className => {
        cardsContainer.classList.toggle(className)
    })
}

function editVeiculo() {
    if (lista.length === 1) {
        window.location.href = `/veiculos/editar/${lista[0]}`
        afterDoAction()
    }
}

function deleteVeiculoAction() {
    if (lista.length === 1) {
        let idVeiculo = lista[0]
        let url = `veiculo/obter_marca/${idVeiculo}`
        fetch(url, {
            method: 'GET',
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            }
        })
            .then(res => res.json())
            .then(json => {
                dialogoConfirmarExclusaoVeiculo(idVeiculo, json.marca)
            })
            .catch(err => console.log(err))
    } else {
        let url = `veiculo/delete_all`
        fetch(url, {
            method: 'POST',
            credentials: "same-origin",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": DjangoUtils.getCookie("csrftoken"),
            },
            body: JSON.stringify({'ids': lista.join()})
        }).then(res => res.json())
            .then(json => {
                AjaxUtils.refresh('cardsContainer');
                AjaxUtils.refresh('messages');
                afterDoAction();
                enableDisableExport()
            })
    }
}

function afterDoAction() {
    lista = []
    enableDisableEditElement()
    enableDisableDeleteElement()
}
