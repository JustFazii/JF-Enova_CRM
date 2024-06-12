document.addEventListener('DOMContentLoaded', function() {
    const refreshTokenBtn = document.getElementById('refresh-token');
    const timerElement = document.getElementById('timer');
    
    let timerInterval;
    const initialTime = 5 * 60; // 5 minutes in seconds
    let timeLeft = localStorage.getItem('timeLeft') ? parseInt(localStorage.getItem('timeLeft'), 10) : initialTime;
    let timerEnd = localStorage.getItem('timerEnd') ? parseInt(localStorage.getItem('timerEnd'), 10) : Date.now() + (timeLeft * 1000);
    
    function startTimer() {
      clearInterval(timerInterval);
      timerInterval = setInterval(() => {
        const now = Date.now();
        timeLeft = Math.round((timerEnd - now) / 1000);
        
        if (timeLeft <= 0) {
          clearInterval(timerInterval);
          timerElement.textContent = "00:00";
          localStorage.removeItem('timeLeft');
          localStorage.removeItem('timerEnd');
        } else {
          const minutes = Math.floor(timeLeft / 60);
          const seconds = timeLeft % 60;
          timerElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
          localStorage.setItem('timeLeft', timeLeft);
        }
      }, 1000);
    }
    
    refreshTokenBtn.addEventListener('click', function(event) {
      event.preventDefault();
      timeLeft = initialTime;
      timerEnd = Date.now() + (timeLeft * 1000);
      localStorage.setItem('timeLeft', timeLeft);
      localStorage.setItem('timerEnd', timerEnd);
      startTimer();
      eel.RefreshToken();
    });
    
    startTimer();
  });
  