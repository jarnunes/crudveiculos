class JSUtils {
    static isJSONEmpty(json) {
        return json == null || Object.keys(json).length === 0;
    }

    static existsElement(idElement) {
        return document.contains(document.getElementById(idElement))
    }

    static setStyleDisplayById(idElement, styleDisplay) {
        if (this.existsElement(idElement)) {
            document.getElementById(idElement).style.display = styleDisplay
            return true;
        }
        return false;
    }

    static removeById(elementId) {
        if (this.existsElement(elementId)) {
            document.getElementById(elementId).remove()
            return true;
        }
        return false;
    }

    static appendChild(tagName, elementId, classList, html, idContainer, appendToBody = false) {
        try {
            let childElement = document.createElement(tagName);
            childElement.id = elementId
            if (classList != null) {
                childElement.classList.add(...classList)
            }
            childElement.innerHTML = html
            if (idContainer != null && this.existsElement(idContainer)) {
                document.getElementById(idContainer).appendChild(childElement)
            }
            if (appendToBody && idContainer === null) {
                document.body.appendChild(childElement)
            }
        } catch (e) {
            throw new Error(e)
        }
    }
}

class AjaxUtils {
    static refresh(idElement) {
        $(`#${idElement}`).load(window.location.href + ` #${idElement}`);
    }

    static refreshContainer() {
        this.refresh('container')
    }

}

class DjangoUtils {
    static getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (const element of cookies) {
                const cookie = element.trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}


class ModalUtils {

    static openModal(idModal) {
        $(`#${idModal}`).modal('show');
    }

    static closeModal(idModal) {
        $(`#${idModal}`).modal('hide');
    }

    static closeAndRemoveModal(idModal, idContainerModal) {
        this.closeModal(idModal);
        JSUtils.removeById(idContainerModal);
    }

    static appendChildModalToBody(idContainerModal, idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName) {
        let divContainerModal = document.createElement('div')
        divContainerModal.id = idContainerModal
        divContainerModal.innerHTML = this.baseContainer(idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName)
        document.body.appendChild(divContainerModal)
    }

    /**
     *
     * @param idModal String
     * @param idForm String
     * @param titleModal String
     * @param modalBody htmlContent
     * @param cancelFuncName functionName();
     * @param confirmFuncName functionName();
     * @returns {string}
     */
    static baseContainer(idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName) {
        return `<div class="modal fade" id="${idModal}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
                    data-focus-on="input:first">
                    <form id="${idForm}" name="${idForm}">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 id="title_modal" class="modal-title">${titleModal === null ? '' : titleModal}</h5>
                                </div>
                                <div class="modal-body">${modalBody}</div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" href="#${idModal}"
                                     ${cancelFuncName == null ? '' : 'onclick="' + cancelFuncName + '"'}>Cancelar</button>
                                    <button type="button" class="btn btn-primary" onclick="${confirmFuncName}">Confirmar</button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>`
    }
}