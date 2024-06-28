// Seleciona o formulário pelo ID
const form = document.getElementById('CadastroAvancadoForm');

// Adiciona um listener para o evento submit do formulário
form.addEventListener('submit', function(event) {
    // Seleciona todos os inputs de tipo rádio com name="gender"
    const genderInputs = document.querySelectorAll('input[type="radio"][name="gender"]');
    let genderSelected = false;

    // Verifica se algum gênero foi selecionado
    genderInputs.forEach(function(input) {
        if (input.checked) {
            genderSelected = true;
        }
    });

    // Se nenhum gênero foi selecionado, mostra a mensagem de erro e impede o envio do formulário
    if (!genderSelected) {
        alert('Por favor, selecione um gênero antes de enviar o formulário.');
        event.preventDefault(); // Impede o envio do formulário
    }
});
