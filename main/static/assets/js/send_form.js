    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    const form = document.getElementById('productForm');
    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const description = document.getElementById('description').value;
        const price = document.getElementById('price').value;

        const response = await fetch('/api/products/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,  // Отправляем CSRF-токен в заголовке
            },
            body: JSON.stringify({
                name: name,
                description: description,
                price: parseFloat(price),
            }),
        });

        if (response.ok) {
            fetchProducts();
        } else {
            alert('Error adding product');
        }
    });

    async function fetchProducts() {
        const response = await fetch('/api/products/');
        const products = await response.json();
        const tbody = document.querySelector('#productTable tbody');
        tbody.innerHTML = '';
        products.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `<td style="width: 33%">${product.name}</td><td style="width: 33%"><div style="word-break: break-all">${product.description}</div></td><td style="width: 33%">${product.price}</td>`;
            tbody.appendChild(row);
        });
    }

    fetchProducts();