document.getElementById('toggle-div').addEventListener('click', function () {
  const buzzer = document.getElementById('buzzer-sound');
  document.body.classList.toggle('blue-background');
  buzzer.currentTime = 0;
  buzzer.play();
  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ip: clientIp })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
