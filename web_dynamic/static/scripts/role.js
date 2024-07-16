document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mentor-button').addEventListener('click', () => {
        sendRole('mentor');
    });

    document.getElementById('mentee-button').addEventListener('click', async () => {
        await sendRole('mentee');
        window.location.href = 'discover.html';
    });

    document.getElementById('submit-specialization').addEventListener('click', () => {
        submitSpecialization();
    });
});

async function sendRole(role, isMentee = false) {
    const signId = await getSignFromCookie();
    if (!signId) {
        console.error('Sign ID not available');
        alert('Failed to select role');
        return;
    }

    console.log('Sign ID retrieved:', signId);
    const data = {
        role: role,
        sign_id: signId
    };

    try {
        const response = await fetch(`https://www.itohan.tech/api/v1/signs/${signId}/roles`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result);
            alert('Role selection successful!');
            if (role === 'mentor') {
                document.getElementById('specialization-container').style.display = 'block';
            } else if (isMentee) {
		console.log('Redirecting to discover.html');
            }
        } else {
            console.error('Failed to store role');
            alert('Failed to select role');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
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

function getCookie(name) {
    console.log('Retrieving cookies:', document.cookie);
    let cookieArr = document.cookie.split(";");
    for (let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        if (name === cookiePair[0].trim()) {
            console.log(`Found cookie: ${name} = ${decodeURIComponent(cookiePair[1])}`);
            return decodeURIComponent(cookiePair[1]);
        }
    }
    console.log(`Cookie not found: ${name}`);
    return null;
}

async function submitSpecialization() {
    const signId = await getSignFromCookie();
    if (!signId) {
        console.error('Sign ID not available');
        alert('Failed to submit specialization');
        return;
    }

    const specialization = document.getElementById('specialization-dropdown').value;
    if (!specialization) {
        alert('Please select a specialization');
        return;
    }

    const data = {
        specialization: specialization,
        sign_id: signId
    };

    try {
        const response = await fetch(`https://www.itohan.tech/api/v1/signs/${signId}/specializations`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (response.ok) {
            const result = await response.json();
            console.log(result);
            alert('Specialization selection successful!');
            window.location.href = 'main-app.html';
        } else {
            console.error('Failed to store specialization');
            alert('Failed to select specialization');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
}

