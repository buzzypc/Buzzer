document.getElementById('toggle-div').addEventListener('click', function () {
  const buzzer = document.getElementById('buzzer-sound');
  fetch('/reset', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ip: clientIp })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      document.body.classList.toggle('toggle-background');
      buzzer.currentTime = 0;
      buzzer.play();
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
