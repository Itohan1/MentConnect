document.addEventListener("DOMContentLoaded", () => {
    const careerPathsButton = document.getElementById("careerPathsButton");
    const careerPathsDropdown = document.getElementById("career-paths");
    const careerPathButtons = document.querySelectorAll(".career-path");
    const selectedCareerPathElement = document.getElementById("selectedCareerPath");

    const signupId = localStorage.getItem("signupId");

    if (!signupId) {
        console.error('No signup ID found. Please sign up first.');
        return;
    }

    careerPathsButton.addEventListener("click", () => {
        careerPathsDropdown.classList.toggle("show");
    });

    careerPathButtons.forEach(button => {
        button.addEventListener("click", async () => {
            const careerPath = button.getAttribute("data-path");

            const response = await fetch(`http://localhost:5000/api/v1/signs/${sign_id}/chosenpaths`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ chosen_path: careerPath })
            });

            if (response.ok) {
                localStorage.setItem("selectedCareerPath", careerPath);
                selectedCareerPathElement.textContent = careerPath;
            } else {
                console.error('Failed to save career path to the backend');
            }
        });
    });

    function loadSelectedCareerPath() {
        const savedCareerPath = localStorage.getItem("selectedCareerPath");
        if (savedCareerPath) {
            selectedCareerPathElement.textContent = savedCareerPath;
        }
    }

    loadSelectedCareerPath();
});

window.onclick = function(event) {
    if (!event.target.matches('#careerPathsButton')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
