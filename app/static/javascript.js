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

$(document).ready(function(){
    var baseUrl = window.location.origin + '/emprestimo';
    var baseUrl_livro = window.location.origin + '/';
    var filter = $('#filter');
    var filterAlf = $('#filterAlf');
    var filter_livro = $('#filter_livro')
    var filterAlf_livro = $('#filterAlf_livro');

    $(filter).change(function() {
       var filter = $(this).val();
       console.log(filter)
       window.location.href = baseUrl + '?filter=' + filter;
    });

    $(filter_livro).change(function() {
       var filter_livro = $(this).val();
       console.log(filter_livro)
       window.location.href = baseUrl_livro + '?filter_livro=' + filter_livro;
    })

    $(filterAlf).change(function() {
       var filterAlf = $(this).val();
       console.log(filterAlf)
       window.location.href = baseUrl + '?filterAlf=' + filterAlf;
    });

    $(filterAlf_livro).change(function() {
       var filterAlf_livro = $(this).val();
       console.log(filterAlf_livro)
       window.location.href = baseUrl_livro + '?filterAlf_livro=' + filterAlf_livro;
    });

});