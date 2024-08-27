const inputAuthor = document.getElementById('id_author');
const textAreaComment = document.getElementById('id_text');
const inputTitle = document.getElementById('id_title');
const textAreaBody = document.getElementById('id_body');

document.addEventListener('DOMContentLoaded', () => {
    inputAuthor ? inputAuthor.placeholder = "Seu Nome": null;
    textAreaComment? textAreaComment.placeholder = "Seu comentario": null;
    
    inputTitle? inputTitle.placeholder = "Titulo do Post": null;
    textAreaBody? textAreaBody.placeholder = "Corpo do Post": null;
} )
