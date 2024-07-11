document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mentor-button').addEventListener('click', () => {
        sendRole('mentor');
    });

    document.getElementById('mentee-button').addEventListener('click', () => {
        sendRole('mentee');
    });

    document.getElementById('submit-specialization').addEventListener('click', () => {
	    submitSpecialization();
    });
});

async function sendRole(role, isMentee = false) {
    const signId = await getSignId();
    if (!signId) {
        console.error('Sign ID not available');
        alert('Failed to select role');
        return;
    }

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
		    window.location.href = 'discover.html';
        } else {
            console.error('Failed to store role');
            alert('Failed to select role');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
}

async function getSignId() {
    const signId = getCookie('sign_id');
    if (!signId) {
	    console.error('Sign ID not found in cookies');
	    return null;
    }
    try {
        const response = await fetch(`https://www.itohan.tech/api/v1/signs/${signId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        if (response.ok) {
            const result = await response.json();
            return result.sign_id;
        } else {
            console.error('Failed to fetch sign_id');
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
function getcookie(name) {
	let cookieArr = document.cookie.split(";");
	for (let i = 0; i < cookieArr.length; i++) {
		let cookiePair = cookieArr[i].split("=");
		if (name === cookiePair[0].trim()) {
			return decodeURIComponent(cookiePair[1]);
		}
	}
	return null;
}
async function submitSpecialization() {
	const signId = await getSignId();
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
	}

	try {
            const response = await fetch(`https://www.itohan.tech/api/v1/signs/${signId}/specializations`, {
               method: 'POST',
               headers: {
                   'Content-Type': 'application/json'
               },
               body: json.stringify(data)
            });
	    if (response.ok) {
                const result = await response.json();
		console.log(result);
		alert('Specialization selection successful!');
	    } else {
	        console.error('Failed to store specialization');
		alert('Failed to select specialization');
            }
        } catch (error) {
		console.error('Error:', error);
		alert('An error occured');
	}
}
