const SERVER_URL = 'http://localhost:5000';

function submitform() {
    let number = document.getElementById('number').value
    fetch(`${SERVER_URL}/check`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'number': number
            })
        })
        .then(response => response.json())
        .then(data => {
            let message = document.getElementById('message');
            if (data.result == 'High' || data.result == 'Low')
                message.innerHTML = `Number ${data.integer} is ${data.result}er than 100`;
            else
                message.innerHTML = `Number ${data.integer} is ${data.result} to 100`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}