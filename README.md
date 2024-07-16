# MentConnect

# Introduction
<div style="display: flex; gap: 10px;">
        <img src="Screenshot%20from%202024-07-04%2009-09-59.png" alt="screenshort from app" width="400" height="200">
        <img src="discovering%20your%20path.png" alt="app questionaire" width="400" height="200">
</div>
<video width="500" height="300" controls>
        <source src="video%20explanation%20of%20app.webm" type="video/webm">
</video>
MentConnect is a platform designed to connect mentees with mentors, helping individuals find guidance and support in their professional journeys. Users can post blogs, like posts, send requests to mentors, and discover the right career paths. The platform was inspired by a need to bridge the gap between aspiring professionals and experienced mentors

# Inspiration
We all had a lot of ideas of what to build, especially me though, that was one of the reasons I joined the Alx program afterall, to be able to see my many ideas come to life, and after much deliberation we finally decided mentConnect was ito had so many questions about his dream career path but wasn't getting the right answers, I wanted more than anything to create a platform that would somehow match mentees with passionate mentors with relatable stories and incorporating that algorithm in our application would be our next key performance indicator.

We all had a lot of ideas of what to build, especially me though, that was one of the reasons I joined the Alx program afterall, to be able to see my many ideas come to life, and after much deliberation we finally decided mentConnect was it. Personally I had my reasons why I wanted to bring this home, I had a friend who had so many questions about his dream career path but wasn't getting the right answers, I wanted more than anything to create a platform that would somehow match mentees with passionate mentors with relatable stories and incorporating that algorithm in our application would be our next key performance indicator.

#Data Collection
After signUp a user can either choose a role as a men
tor or a mentee
Mentee Profiles: For a mentee a user is directed to a page that inludes picking a career path or discoverying a career path, on discoverying career paths mentees are redirected to a page where they can answer group of questions to enable the app suggests a career path for them based on predefined algorithmn, these informations are then stored in a database system used to personalize the users profile
Mentors: A user clicking a mentor option will prompt a dropdown section for picking a specialization, these informations are then stored in a database system used to personalize the users profile

[Deployed-website](https://www.itohan.tech/mentConnect/)
[Final projects's blog article](https://www.linkedin.com/posts/itohan-momodu-48b52723a_mentconnect-is-a-project-that-helps-mentees-activity-7216744807367360514-g2Ek?utm_source=share&utm_medium=member_desktop)

**Authors**:
- [Itohan Momodu](https://www.linkedin.com/in/itohan-momodu-48b52723a/)
- [Damilare Odunsi](https://www.linkedin.com/in/ogundahunsi-damilare/)
- [Eveshogweyore Alle](https://www.linkedin.com/in/ore-35787/)

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Itohan1/mentConnect.git
    cd mentConnect
    ```
2. *Set up environment variables**:
    (mentconnect_user=mentconnect_dev mentconnect_host=localhost mentconnect_db=mentconnect_db mentconnect_TYPE_STORAGE=db mentconnect_api_host=0.0.0.0 mentconnect_api_port=5000)

3. **Run the Flask application**:
    ```sh
    flask run
    ```

4. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000`

5. ## Usage

Once the application is running, you can:

- **Sign Up**: Create an account as a mentee or mentor.
- **Post Blogs**: Share your thoughts and insights with the community.
- **Like Posts**: Engage with content by liking posts.
- **Send Mentors Requests**: Connect with mentors by sending them requests.
- **Discover Career Paths**: Get guidance on finding the right career path

## Contributing

We welcome contributions to MentConnect! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

Please make sure to update tests as appropriate.

## Related Projects

Here are some related projects that might interest you:

- [Mentorship Platform](https://github.com/someuser/mentorship-platform)
- [Career Path Finder](https://github.com/anotheruser/career-path-finder)

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
