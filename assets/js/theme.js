const themeToggleBtn = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('theme');

// Apply saved theme on load
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
}

// Toggle theme on click
themeToggleBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    let theme = document.documentElement.getAttribute('data-theme');

    if (theme === 'blue') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'grey');
    } else {
        document.documentElement.setAttribute('data-theme', 'blue');
        localStorage.setItem('theme', 'blue');
    }
});
