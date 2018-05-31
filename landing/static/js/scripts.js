$(document).ready(function () {
    var form = $('#form_byuing');
    console.log(form);

    function cartUpdating (product_id,nbr, is_delete ) {
         var data = {};
            data.product_id = product_id;
            data.nbr = nbr;
            var csrf_token = $('#form_byuing [name= "csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            if (is_delete){
                data["is_delete"] = true;
            }

            var url = form.attr("action");
         console.log(data);
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log('OK');
                    console.log(data.products_total_nbr);
                    if (data.products_total_nbr || data.products_total_nbr === 0) {
                        $('#basket_total_nbr').text("(" + data.products_total_nbr + ")");
                        console.log(data.products);
                        $('.basket-items ul').html("");
                        $.each(data.products, function (k, v) {
                            $('.basket-items ul').append('<li>' + v.name + ', ' + v.nbr + 'шт. ' + 'по ' + v.price_per_item + 'usd ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+ '' +
                            '</li>');
                    });
                }
            },
                error:function () {
                    console.log('error')
            }

        });
    }

        form.on('submit', function (e) {
            e.preventDefault();
            console.log('123');
            var nbr = $('#number').val();
            console.log(nbr);
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product');
            var name = submit_btn.data('name');
            var price = submit_btn.data('price');

            cartUpdating(product_id,nbr, is_delete=false)



    });

        $(document).on('click', '.delete-item', function (e) {
            e.preventDefault();
            product_id = $(this).data("product_id");
            nbr = 0;
            cartUpdating(product_id, nbr, is_delete=true)
        })


});