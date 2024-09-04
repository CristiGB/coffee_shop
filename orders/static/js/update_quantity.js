$(document).ready(function() {


        $('.edit-quantity').on('click', '.fa-circle-minus', function() {
            var $container = $(this).closest('.edit-quantity');
            var $productTotalPrice = $container.siblings('.product-total-price');
            var $quantityDiv = $container.find('.product_order-quantity');
            var quantity = parseInt($quantityDiv.text());
            var productId = $container.data('product-id'); 

            if (quantity > 1) { 
                quantity--;
                updateQuantity(productId, quantity, $quantityDiv, $productTotalPrice);
            }
        });

        $('.edit-quantity').on('click', '.fa-circle-plus', function() {
            var $container = $(this).closest('.edit-quantity');
            var $productTotalPrice = $container.siblings('.product-total-price');
            var $quantityDiv = $container.find('.product_order-quantity');
            var quantity = parseInt($quantityDiv.text());
            var productId = $container.data('product-id');

            quantity++;
            updateQuantity(productId, quantity, $quantityDiv, $productTotalPrice);
        });

        function updateQuantity(productId, quantity, $quantityDiv, $productPrice) {
            $.ajax({
                url: updateQuantityUrl,
                type: "POST",
                data: {
                    'product_id': productId,
                    'quantity': quantity,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response) {
                    if (response.success) {
                        $quantityDiv.text(response.new_quantity);
                    $productPrice.text('$ ' + response.total_price);
                    $('.total-price').each(function(){
                        var $totalPriceElement = $(this);
                        $totalPriceElement.text('$ ' + response.order_total);
                    });
        
                    } else {
                        alert(response.error);
                    }
                },
                error: function(xhr, errmsg, err) {
                    alert('Error: ' + errmsg);
                }
            });
        }
    });
