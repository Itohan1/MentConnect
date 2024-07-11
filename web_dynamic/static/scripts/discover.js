document.addEventListener("DOMContentLoaded", () => {
    const questions = document.querySelectorAll(".question");
    const conclusionElement = document.getElementById("conclusion");
    const getStartedButton = document.getElementById("getStarted");

    let responses = {};
    const signupId = localStorage.getItem("signupId");

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
        localStorage.setItem("careerConclusion", conclusion);

        const response = await fetch(`http://localhost:5000/api/v1/signup/${signupId}/chosenpath`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ conclusion })
        });

        if (!response.ok) {
            console.error('Failed to save conclusion to the backend');
        }
    }

    function loadConclusion() {
        const savedConclusion = localStorage.getItem("careerConclusion");
        if (savedConclusion) {
            conclusionElement.textContent = savedConclusion;
        }
    }

    loadConclusion();

    getStartedButton.addEventListener("click", () => {
        const savedConclusion = localStorage.getItem("careerConclusion");
        if (savedConclusion) {
            window.location.href = `main.html?signupId=${signupId}`;
        } else {
            alert("You must complete the quiz to get started.");
        }
    });
});
