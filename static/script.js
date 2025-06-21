document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const loaderContainer = document.querySelector('.loader-container');
  const patternTypeSelect = document.getElementById("pattern_type");
  const sidesContainer = document.getElementById("sides-container");

  const MINIMUM_DISPLAY_TIME = 500;
  let clickedButton = null;

  // manage the display of the number of sides
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

  // detect which button is clicked
  form.querySelectorAll('button[type="submit"]').forEach(button => {
    button.addEventListener('click', () => {
      clickedButton = button;
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    loaderContainer.classList.remove('hidden');
    const startTime = Date.now();

    if (clickedButton) {
      const hiddenInput = document.createElement('input');
      hiddenInput.type = 'hidden';
      hiddenInput.name = 'action';
      hiddenInput.value = clickedButton.value;
      form.appendChild(hiddenInput);
    }

    // force a minimum delay for smooth display of the loader
    const elapsed = Date.now() - startTime;
    const remainingTime = MINIMUM_DISPLAY_TIME - elapsed;

    setTimeout(() => {
      form.submit();
    }, Math.max(remainingTime, 0));
  });
});