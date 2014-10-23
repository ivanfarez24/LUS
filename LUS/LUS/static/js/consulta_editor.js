jQuery(document).ready(function($) {
    $( 'textarea#id_contenido' ).ckeditor();
    $( 'textarea#id_animacion' ).ckeditor();
    $( 'textarea#id_texto' ).ckeditor();
    // ALLOW <i></i>
    config.protectedSource.push(/<i[^>]*><\/i>/g);
} );