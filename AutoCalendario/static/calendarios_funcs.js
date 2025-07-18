function openModal(strDia, strMes, strAno) {
    // # Verificar e corrigir formato da data
    if (strDia.length != 2)
    {
        strDia = '0' + strDia
    }

    if (strMes.length != 2)
    {
        strMes = '0' + strMes
    }

    const modalBody = document.getElementById('dateModal')
    
    //# Show date options
    modalBody.innerHTML = `
    <div class="modal-content">
        <span class="close" onclick="closeModal('dateModal')">&times;</span>

        <h3 id="modal-date">Opções para dia ${strDia}/${strMes}</h3>

        <div class="button-options">
            <div>
                <button onclick="addParadas('${strDia}/${strMes}/${strAno}')">Adicionar parada</button>

                <div id="add-forms"></div>
            </div>
            
            <div>
                <button onclick="excluirParada('${strDia}/${strMes}/${strAno}')">Excluir parada</button>

                <div id="excluir-forms"></div>
            </div>
        </div>
    </div>
    `

    document.getElementById('dateModal').style.display = 'block';
}

function closeModal(inst) {
    document.getElementById(inst).style.display = 'none';
}

function addParadas(data) {
    const botao_adicionar = document.getElementById('add-forms')
    
    //# Show data options
    botao_adicionar.innerHTML = `
    <form action="/adicionar" method="post" id="adicionar-send">
        <div>
            <span class="close" onclick="closeModal('adicionar-send')">&times;</span>

            <div id="add-forms">
                <div>
                    <input name="data" placeholder="Data (dd/mm/yyyy)" required value="${data}">
                </div>

                <select id="month-selector" name="instancia">
                    <option class="options">motivo1</option>

                    <option class="options">motivo2</option>
                </select>

                <div>
                    <input name="notas" placeholder="Notas (opcional)">
                </div>
            </div>

            <button>Adicionar</button>
        </div>
    </form>
    `

    document.getElementById('add-forms').style.display = 'block';
}

function excluirParada(data) {
    const botao_excluir = document.getElementById('excluir-forms')
    
    //# Show data options
    botao_excluir.innerHTML = `
    <div id="excluir-send">
    <span class="close" onclick="closeModal('excluir-send')">&times;</span>
    
    Excluir parada do dia ${data}?

        <div class="button-options">
            <button onclick="closeModal('excluir-send')">Cancelar</button>
            
            <form action="/excluir" method="post">
                <button name="data" value="${data}">Confirmar</button>
            </form>
        </div>
    </div>
    `

    document.getElementById('excluir-forms').style.display = 'block';
}

function calcParada(data) {
    const botao_calcular = document.getElementById('calc-forms')
    
    //# Show data options
    botao_calcular.innerHTML = `
    <form action="/calcular" method="post" id="calcular-send">
        <div>
            <span class="close" onclick="closeModal('calcular-send')">&times;</span>

             <br> <strong>${data}</strong>

            <div id="calc-forms">
                <select id="month-selector" name="instancia">
                    <option class="options">motivo1</option>

                    <option class="options">motivo2</option>
                </select>

                <div>
                    <input name="notas" placeholder="Notas">
                </div>
            </div>

            <button>Adicionar parada recomendada</button>
        </div>
    </form>
    `

    document.getElementById('calc-forms').style.display = 'block';
}

// Close modal when clicking outside the content
window.onclick = function (event) {
    const modal = document.getElementById('dateModal');
    if (event.target == modal) {
        closeModal();
    }
}