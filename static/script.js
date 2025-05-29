document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('patternForm');
    const loader = document.getElementById('customLoader');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        loader.classList.remove('hidden');

        setTimeout(() => {
            form.submit();
        }, 1500);
    });
});
