const SERVER_URL = 'http://localhost:5000';

function submitform() {
    let number = document.getElementById('number').value;
    let message = document.getElementById('message');
    message.style.color = "initial"
    if (!number || isNaN(number)) {
        message.innerHTML = 'Please Enter a Valid Number';
        message.style.color = "red";
        return;
    }
    if (!Number.isInteger(Number.parseFloat(number))) {
        message.innerHTML = 'Please Enter a Valid Integer';
        message.style.color = "red";
        return;
    }
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
            if (data.result == 'High' || data.result == 'Low')
                message.innerHTML = `Number ${data.integer} is ${data.result}er than 100`;
            else
                message.innerHTML = `Number ${data.integer} is ${data.result} to 100`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}