document.addEventListener("DOMContentLoaded", function() {
    const timerElement = document.getElementById("timer");
    let timeLeft = 60; // 60 seconds for each question

    function updateTimer() {
        if (timeLeft > 0) {
            timeLeft -= 1;
            timerElement.textContent = `Time left: ${timeLeft} seconds`;
        } else {
            alert("Time's up!");
            // Implement what happens when time is up (e.g., submit the answer automatically)
        }
    }

    if (timerElement) {
        setInterval(updateTimer, 1000); // Update the timer every second
    }
});
