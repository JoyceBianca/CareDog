function sendData() {
    const nome = document.getElementById('nome').value; // Captura o valor do input
    const senha = document.getElementById('senha').value;
    
    const xhr = new XMLHttpRequest(); // Cria uma nova instância de XMLHttpRequest
    xhr.open('GET', `/loginUsuario?nome=${nome}&senha=${email}`, true); // Configura a requisição GET com o valor do input na URL
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('result').innerText = xhr.responseText; // Atualiza o elemento 'result' com a resposta
        }
    };
    xhr.send(); // Envia a requisição
}