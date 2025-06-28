document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const loaderContainer = document.querySelector('.loader-container');
  const patternTypeSelect = document.getElementById("pattern_type");
  const repsInput = document.getElementById("reps");
  const sidesContainer = document.getElementById("sides-container");

  const MINIMUM_DISPLAY_TIME = 500;
  let clickedButton = null;

  function updateSidesVisibility() {
    const pattern = patternTypeSelect.value;
    if (pattern === "polygon") {
      sidesContainer.style.display = "block";
    } else {
      sidesContainer.style.display = "none";
    }
  }

  patternTypeSelect.addEventListener("change", updateSidesVisibility);
  updateSidesVisibility();

  // détecter le bouton cliqué
  form.querySelectorAll('button[type="submit"]').forEach(button => {
    button.addEventListener('click', () => {
      clickedButton = button;
    });
  });

  form.addEventListener('submit', function (e) {
    const selectedPattern = patternTypeSelect.value;
    const repetitions = parseInt(repsInput.value, 10);

    if (selectedPattern === "fractal" && repetitions > 7) {
      e.preventDefault();
      alert("WARNING: More than 6 repetitions on a fractal are not allowed due to the fact that it will take too long. Please choose 7 or fewer repetitions");

      return;
    }


    loaderContainer.classList.remove('hidden');
    const startTime = Date.now();

    if (clickedButton) {
      const hiddenInput = document.createElement('input');
      hiddenInput.type = 'hidden';
      hiddenInput.name = 'action';
      hiddenInput.value = clickedButton.value;
      form.appendChild(hiddenInput);
    }

    const elapsed = Date.now() - startTime;
    const remainingTime = MINIMUM_DISPLAY_TIME - elapsed;

    setTimeout(() => {
      form.submit();
    }, Math.max(remainingTime, 0));
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const rotInput = document.getElementById('rot');
  const rotValueDisplay = document.getElementById('rot-value');

  // mettre à jour la valeur affichée quand on déplace le slider
  rotInput.addEventListener('input', function () {
    rotValueDisplay.textContent = `${rotInput.value}°`;
  });

  function updateSliderBackground(input) {
  const val = (input.value - input.min) / (input.max - input.min) * 100;
  input.style.setProperty('--value', `${val}%`);
}

  // Pour le rot
  rotInput.addEventListener('input', function () {
    rotValueDisplay.textContent = `${rotInput.value}°`;
    updateSliderBackground(rotInput);
  });

  // Initialisation au chargement
  updateSliderBackground(rotInput);


  // initialiser au chargement
  rotValueDisplay.textContent = `${rotInput.value}°`;
});