const products = [
    { name: 'Chocolate Cake' },
    { name: 'Vanilla cake' },
    { name: 'Icing cake' },
    { name: 'Cup cake' },
    { name: 'Mirror Glaze Cake' },


];

function searchProducts() {
    const searchTerm = document.getElementById('product-search').value.toLowerCase();
    const productRows = document.querySelectorAll('.product-row .box');
    productRows.forEach(product => {
        const productName = product.querySelector('h3').textContent.toLowerCase();
        product.style.display = productName.includes(searchTerm) ? 'block' : 'none';
    });
}

function showSuggestions() {
    const searchTerm = document.getElementById('product-search').value.toLowerCase();
    const suggestionsDiv = document.getElementById('suggestions');
    suggestionsDiv.innerHTML = '';

    if (searchTerm) {
        const filteredProducts = products.filter(product => product.name.toLowerCase().includes(searchTerm));
        filteredProducts.forEach(product => {
            const suggestionItem = document.createElement('div');
            suggestionItem.textContent = product.name;
            suggestionItem.onclick = () => {
                document.getElementById('product-search').value = product.name;
                searchProducts();
                suggestionsDiv.style.display = 'none'; 
            };
            suggestionsDiv.appendChild(suggestionItem);
        });
        suggestionsDiv.style.display = filteredProducts.length ? 'block' : 'none';
    } else {
        suggestionsDiv.style.display = 'none';
    }
}

