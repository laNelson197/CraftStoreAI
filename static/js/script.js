document.getElementById('show-products-btn').addEventListener('click', function() {
    // Send a request to fetch all products
    fetch('/get_all_products')
        .then(response => response.json())
        .then(products => {
            const productsListDiv = document.getElementById('products-list');
            productsListDiv.innerHTML = '';

            if (products.length > 0) {
                // Loop through the products and create an HTML list
                let productHTML = '<ul>';
                products.forEach(product => {
                    productHTML += `
                        <li>
                            <strong>${product.product_name}</strong><br>
                            Description: ${product.product_description}<br>
                            Price: $${product.price}<br>
                        </li>
                    `;
                });
                productHTML += '</ul>';
                productsListDiv.innerHTML = productHTML;
            } else {
                productsListDiv.innerHTML = '<p>No products found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
});
