document.addEventListener("DOMContentLoaded", () => {
    const signupForm = document.getElementById("signupForm");

    signupForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const formData = new FormData(signupForm);
        const data = {
            firstname: formData.get("firstname"),
            surname: formData.get("surname"),
            age: formData.get("age"),
            email: formData.get("email"),
            password: formData.get("password")
        };
        try {
            const response = await fetch(`https://www.itohan.tech/api/v1/signs/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                const result = await response.json();
                alert("Sign Up successful!");
                window.location.href = "Role.html";
            } else {
		    console.log(response);
                console.error('Sign Up failed');
                alert("Sign Up failed!");
            }
        } catch (error) {
            console.error('Error:', error);
            alert("An error occurred!");
        }
    });
});

