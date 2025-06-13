document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const loaderContainer = document.querySelector('.loader-container');
  const patternTypeSelect = document.getElementById("pattern_type");
  const sidesContainer = document.getElementById("sides-container");

  const MINIMUM_DISPLAY_TIME = 1500;
  let clickedButton = null;

  // Handle showing/hiding sides input
  function updateSidesVisibility() {
    if (patternTypeSelect.value === "polygon") {
      sidesContainer.style.display = "block";
    } else {
      sidesContainer.style.display = "none";
    }
  }
  if (patternTypeSelect && sidesContainer) {
    patternTypeSelect.addEventListener("change", updateSidesVisibility);
    updateSidesVisibility();
  }

  // Track which button was clicked → to send correct 'action' to Flask
  form.querySelectorAll('button[type="submit"]').forEach(button => {
    button.addEventListener('click', () => {
      clickedButton = button;
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    loaderContainer.classList.remove('hidden');
    const startTime = Date.now();

    const elapsed = Date.now() - startTime;
    const remainingTime = MINIMUM_DISPLAY_TIME - elapsed;

    setTimeout(() => {
      // Add hidden 'action' input so Flask gets action=generate or action=mystery
      if (clickedButton) {
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'action';
        hiddenInput.value = clickedButton.value;
        form.appendChild(hiddenInput);
      }

      loaderContainer.classList.add('hidden');
      form.submit(); // Normal POST → Python handles both generate & mystery
    }, Math.max(remainingTime, 0));
  });
});