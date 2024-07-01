document.addEventListener('DOMContentLoaded', (event) => {
    const userIcon = document.getElementById('userIcon');
    const dropdownContent = document.getElementById('dropdownContent');

    userIcon.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdownContent.classList.toggle('show');
    });

    window.addEventListener("click",(e) => {
        if (!e.target.matches(".user-icon")) {
            if (dropdownContent.classList.contains("show")) {
                dropdownContent.classList.remove("show");
            }
        }
    });
});