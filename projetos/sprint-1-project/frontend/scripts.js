const tableElement = document.querySelector('#main-table')
const clientsQuantityElement = document.querySelector('#clients-quantity')
const clientsNotExistsElement = document.querySelector('#clients-not-exists')
const registerClientDialogElement = document.querySelector("#register-client-dialog")
const addClientButtonElement = document.querySelector("#add-client-button")
const cancelClientRegisterElement = document.querySelector("#cancel-register-client-button")

const registerClientFormElement = document.querySelector("#register-client-form")

const API_URL = 'http://172.28.238.47:5000' // host with wsl


async function fetchAllClients() {
    try {
        const response = await fetch(`${API_URL}/clients`, {
            method: 'GET'
        })

        const data = await response.json()

        fillTableElementWithData(data.clients)

        console.log(data)
    } catch (err) {
        alert('Error ao buscar clientes')
    }

}

async function registerNewClient(formElement) {
    try {
        const formData = new FormData(formElement)

        for (input of formData) {
            console.log(input)
        }

        await fetch(`${API_URL}/clients`, {
            method: 'POST',
            body: formData
        })


        fetchAllClients()
        registerClientDialogElement.close();
        console.log(data)
    } catch (err) {
        alert('Error ao registrar cliente')
    }

}

async function fetchClientsQuantity() {
    try {
        const response = await fetch(`${API_URL}/clients/quantity`, {
            method: 'GET'
        })

        const data = await response.json()

        fillClientsQuantity(data.count)
        verifyIfExistsClients()

        console.log(data)
    } catch (err) {
        alert('Error ao buscar a quantidade de clientes')
    }
}

async function deleteClientById(clientId) {
    try {
        const response = await fetch(`${API_URL}/clients/${clientId}`, {
            method: 'DELETE'
        })

        await response.json()

        fillClientsQuantity(data.count)

        console.log(data)
    } catch (err) {
        alert('Error ao deletar clientes')
    }
}

function verifyIfExistsClients() {
    const tbody = tableElement.querySelector("tbody");
    const hasRows = tbody.querySelectorAll("tr").length > 0;

    if (!hasRows) {
        clientsNotExistsElement.classList.add('show')
    } else {
        clientsNotExistsElement.classList.remove('show')
    }
}

async function handleDeleteClient(clientTableRow) {
    console.log(clientTableRow)
    if (window.confirm("Confirmar deleção do cliente ?")) {
        const clientIdElement = clientTableRow.closest('tr').querySelector('td[data-client-id]')

        console.log(clientIdElement.innerText)

        if (!clientIdElement.innerText) {
            alert('Não foi possivel deletar o cliente. Id não encontrado !')
        }

        await deleteClientById(Number(clientIdElement.innerText))
        clientTableRow.remove()
        verifyIfExistsClients()
    }
}

function fillTableElementWithData(clients) {
    clients.forEach(client => {
        const elementHTML = `  
        <tr>
            <td data-client-id>${client.id}</td>
            <td>${client.name}</td>
            <td>${client.email}</td>
            <td>${client.phone}</td>
            <td>${client.document}</td>
            <td><i class="fa-solid fa-trash" onclick="handleDeleteClient(this)"></i></td>
        </tr>`

        tableElement.querySelector('tbody').insertAdjacentHTML('afterbegin', elementHTML)
    })
}

function fillClientsQuantity(count) {
    clientsQuantityElement.innerText = count
}

//listeners

addClientButtonElement.addEventListener("click", function () {
    registerClientDialogElement.showModal();
});


cancelClientRegisterElement.addEventListener("click", function () {
    registerClientDialogElement.close();
});

registerClientFormElement.addEventListener('submit', event => {
    event.preventDefault()
    registerNewClient(event.target)
})

// init data
Promise.all(fetchAllClients(), fetchClientsQuantity())
