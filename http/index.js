document.getElementById('cep').addEventListener('blur', async (e) => {
    const response = await fetch(`https://brasilapi.com.br/api/cep/v2/${e.target.value}`)
    const data = await response.json()

    document.getElementById('logradouro').value = data.street
    document.getElementById('cidade').value = data.city
    document.getElementById('estado').value = data.state
})

document.getElementById('voltar').onclick = (e) => {
    e.preventDefault()
    window.location.href = "http://127.0.0.1:5500/http/index.html"
}

document.getElementsByTagName("body").addEventListener("onload", () => carregarTabela())

function criaMascara(mascaraInput) {
    const maximoInput = document.getElementById(`${mascaraInput}Input`).maxLength;
    let valorInput = document.getElementById(`${mascaraInput}Input`).value;
    let valorSemPonto = document.getElementById(`${mascaraInput}Input`).value.replace(/([^0-9])+/g, "");

    const mascaras = {
      cpf: valorInput.replace(/[^\d]/g, "").replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4"),
      telefone: valorInput.replace(/[^\d]/g, "").replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3"),
    };

    if(valorInput.length === maximoInput) {
        document.getElementById(`${mascaraInput}Input`).value = mascaras[mascaraInput]
    } else {
        document.getElementById(`${mascaraInput}Input`).value = valorSemPonto;
    }
};

async function carregarTabela() {
    fetch("http://localhost:5000/listarPessoas")
        .then(response => response.json())
        .then(data => console.log(data))
    
}