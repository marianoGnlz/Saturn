function agruparNombre(){
    const $nombre = document.querySelector('div[name="Nombre"]');
    const $apellido = document.querySelector('div[name="Apellido"]');

    $nombre.classList += ' col';
    $apellido.classList += ' col'; 

    const $div = document.createElement('div');
    $div.classList = "form-row"

    $div.appendChild($nombre);
    $div.appendChild($apellido);

    const $dni = document.querySelector('div[name="Dni"]');
    const $form = document.querySelector('form');

    $form.insertBefore($div,$dni);

}

function agruparSexo(){
    const $sexo = document.querySelector('div[name="Sexo"]');
    const $listli = document.querySelectorAll('li');
    $listli.forEach((li) => {
        const $div = document.createElement('div');
        $div.classList = 'form-check form-check-inline';
        $div.appendChild(li);
        $sexo.appendChild($div);
    });
    $listli[0].remove();
    
}

agruparNombre();
agruparSexo();