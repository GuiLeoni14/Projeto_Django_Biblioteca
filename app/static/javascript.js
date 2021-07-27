(function(win,doc){
    'use strict';
    //Vericamos  se realmente ira deletar o dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseje mesmo deletar? ')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }


    //Ajax no form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status == 200 && ajax.readyState == 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação foi feita com sucesso!'
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                    //console.log('Cadastro feito com sucesso!');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);

function funcao_pdf()
    {
        var pegar_dados = document.getElementById('dados').InnerHTMl;
        var janela = window.open('','','width=800, heigth=600');
        janela.document.write('<html><head>');
        janela.document.write('<title>PDF</title></head>');
        janela.document.write('<body');
        janela.document.write(pegar_dados);
        janela.document.write('</body></html>');
        janela.document.close();
        janela.print();
    }