document.addEventListener("DOMContentLoaded", async () => {
    const questions = document.querySelectorAll(".question");
    const conclusionElement = document.getElementById("conclusion");
    const getStartedButton = document.getElementById("getStarted");

    let responses = {};
    const signupId = await getSignFromCookie();

    if (!signupId) {
        console.error('No signup ID found. Please sign up first.');
        return;
    }

    const conclusions = {
        creative_office_money: "You should consider a career in Graphic Design.",
        analytical_outdoors_growth: "You might enjoy a career in Environmental Science.",
        helping_home_impact: "A career in Social Work might be a good fit for you.",
    };

    questions.forEach(question => {
        const buttons = question.querySelectorAll(".answer");

        buttons.forEach(button => {
            button.addEventListener("click", () => {
                const questionId = question.getAttribute("data-question");
                const answer = button.getAttribute("data-answer");

                responses[questionId] = answer;

                if (Object.keys(responses).length === questions.length) {
                    const responseKey = Object.values(responses).join("_");
                    if (conclusions.hasOwnProperty(responseKey)) {
                        const conclusion = conclusions[responseKey];
                        conclusionElement.textContent = conclusion;
                        saveConclusion(conclusion, signupId);
                    } else {
                        conclusionElement.textContent = "We couldn't determine a specific career path based on your answers.";
                    }
                }
            });
        });
    });

    async function saveConclusion(conclusion, signupId) {
        const data = {
		career_name: conclusion
	}
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

    async function loadConclusion() {
        const savedConclusion = await getChosenPathFromCookie();

        if (savedConclusion) {
            conclusionElement.textContent = savedConclusion;
        }
    }

    loadConclusion();

    getStartedButton.addEventListener("click", async () => {
        const savedConclusion = await getChosenPathFromCookie();
        if (savedConclusion) {
            window.location.href = `main-app.html?signupId=${signupId}`;
        } else {
            alert("You must complete the quiz to get started.");
        }
    });
});

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
