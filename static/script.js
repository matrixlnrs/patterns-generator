document.addEventListener('DOMContentLoaded', function () {
  // select main DOM elements
  const form = document.querySelector('form');
  const loaderContainer = document.querySelector('.loader-container');
  const patternTypeSelect = document.getElementById('pattern_type');
  const repsInput = document.getElementById('reps');
  const sidesContainer = document.getElementById('sides-container');
  const rotInput = document.getElementById('rot');
  const rotValueDisplay = document.getElementById('rot-value');

  const MINIMUM_DISPLAY_TIME = 500;
  let clickedButton = null;

  // show/hide the side parameter input depending on selected pattern type
  function updateSidesVisibility() {
    const pattern = patternTypeSelect.value;
    sidesContainer.style.display = pattern === 'polygon' ? 'block' : 'none';

    patternTypeSelect.addEventListener('change', updateSidesVisibility);
  }

  // fill the background of the slider based on its value
  function updateSliderBackground(input) {
    const val = ((input.value - input.min) / (input.max - input.min)) * 100;
    input.style.setProperty('--value', `${val}%`);
  }
  
  function initializeRotationSlider() {
    if (!rotInput || !rotValueDisplay) return;

    rotInput.addEventListener('input', () => {
      rotValueDisplay.textContent = `${rotInput.value}°`;
      updateSliderBackground(rotInput);
    });

    rotValueDisplay.textContent = `${rotInput.value}°`;
    updateSliderBackground(rotInput);
  }

  // keep track of which submit button is clicked
  form.querySelectorAll('button[type="submit"]').forEach(button => {
    button.addEventListener('click', () => {
      clickedButton = button;
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const selectedPattern = patternTypeSelect.value;
    const repetitions = parseInt(repsInput.value, 10);

    // prevent too many fractal repetitions
    if (selectedPattern === 'fractal' && repetitions > 7) {
      alert("WARNING: More than 7 repetitions on a fractal are not allowed due to long rendering time. Please choose 7 or fewer.");
      return;
    }

    loaderContainer.classList.remove('hidden');
    const startTime = Date.now();

    // add hidden input to indicate which button triggered the form
    if (clickedButton) {
      const hiddenInput = document.createElement('input');
      hiddenInput.type = 'hidden';
      hiddenInput.name = 'action';
      hiddenInput.value = clickedButton.value;
      form.appendChild(hiddenInput);
    }

    // ensure loader is visible for at least 500ms
    const elapsed = Date.now() - startTime;
    const remainingTime = MINIMUM_DISPLAY_TIME - elapsed;

    setTimeout(() => {
      form.submit();
    }, Math.max(remainingTime, 0));
  });

  // initialize modal for viewing history
  document.getElementById('open-history-btn').addEventListener('click', () => {
    const modal = document.getElementById('history-modal');
    const list = document.getElementById('history-list');

    fetch('/history')
      .then(response => response.json())
      .then(data => {
        list.innerHTML = '';

        data.forEach(entry => {
          const li = document.createElement('li');
          const img = document.createElement('img');

          img.src = entry.image_url;
          img.alt = 'Generated pattern';
          img.classList.add('history-img');

          li.appendChild(img);
          list.appendChild(li);
        });
      
        modal.style.display = 'block';
      });
  });

  // close history modal
  document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('history-modal').style.display = 'none';
  });

  updateSidesVisibility();
  initializeRotationSlider();
});