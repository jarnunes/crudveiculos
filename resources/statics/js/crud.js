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
            AjaxUtils.refreshContainer();
        })
}