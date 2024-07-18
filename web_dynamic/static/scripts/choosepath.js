document.addEventListener("DOMContentLoaded", async () => {
    const careerPathsButton = document.getElementById("careerPathsButton");
    const careerPathsDropdown = document.getElementById("career-paths");
    const careerPathButtons = document.querySelectorAll(".career-path");
    const selectedCareerPathElement = document.getElementById("selectedCareerPath");
    const getStartedButton = document.getElementById("getStarted");

    const signupId = await getSignFromCookie();

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
            selectedCareerPathElement.textContent = careerPath;
            await saveConclusion(careerPath, signupId);
        });
    });

    async function loadSelectedCareerPath() {
        const savedCareerPath = await getChosenPathFromCookie();
        if (savedCareerPath) {
            selectedCareerPathElement.textContent = savedCareerPath;
        } else {
            console.error('No saved career path found.');
        }
    }

    loadSelectedCareerPath();

    getStartedButton.addEventListener("click", async () => {
        const savedConclusion = await getChosenPathFromCookie();
        if (savedConclusion) {
            window.location.href = `main-app.html?signupId=${signupId}`;
        } else {
            alert("You must complete the quiz to get started.");
        }
    });

    async function saveConclusion(careerPath, signupId) {
        const data = {
            career_name: careerPath
        };
        const response = await fetch(`https://www.itohan.tech/api/v1/signs/${signupId}/chosenpaths`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            console.error('Failed to save conclusion to the backend');
        }
    }

    async function getSignFromCookie() {
        try {
            const response = await fetch(`https://www.itohan.tech/api/v1/signcookie`, {
                method: 'GET',
                credentials: 'include'
            });

            if (!response.ok) {
                console.error('Failed to fetch sign from cookie:', response.status);
                return null;
            }

            const result = await response.json();
            console.log('Sign data:', result);
            return result.id;
        } catch (error) {
            console.error('Error fetching sign from cookie:', error);
            return null;
        }
    }

    async function getChosenPathFromCookie() {
        try {
            const response = await fetch(`https://www.itohan.tech/api/v1/chosencookie`, {
                method: 'GET',
                credentials: 'include'
            });

            if (!response.ok) {
                console.error('Failed to fetch chosen_path from cookie:', response.status);
                return null;
            }

            const result = await response.json();
            console.log('Chosen data:', result);
            return result.career_name;
        } catch (error) {
            console.error('Error fetching chosen_path from cookie:', error);
            return null;
        }
    }

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
    };
});

