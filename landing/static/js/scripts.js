$(document).ready(function () {
    var form = $('#form_byuing');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var nbr = $('#number').val();
        console.log(nbr);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product');
        var name = submit_btn.data('name');
        var price = submit_btn.data('price');


        $('.basket-items ul').append('<li>'+name+', ' + nbr + 'шт. ' + 'по ' + price + 'usd ' +
            '<a class="delete-item" href="">x</a>'+ '</li>');
    });

        $(document).on('click', '.delete-item', function (e) {
            e.preventDefault();
            $(this).closest('li').remove();
        })


});