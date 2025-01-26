# SpendWise

Welcome to SpendWise, A tracking tool to your expenses!

![Expense Tracker Image](jakub-zerdzicki-ykgLX_CwtDw-unsplash.png)

## Overview
SpendWise is a web-based expense tracker designed to help users manage their finances efficiently. The platform offers secure user registration and login, allowing users to add, view, edit, and delete transactions. With SpendWise, users can generate detailed reports to analyze their spending patterns and make informed financial decisions. The project is built using Django, and it incorporates responsive design, real-time notifications, and secure access control to enhance user experience and data security.

## Table of Contents
- [User Experience Design Process](#user-experience-design-process)
    - [Link to User Stories in GitHub Projects](#link-to-User-Stories-in-GitHub-Projects)
    - [Wireframes](#wireframes)
- [Design Rationale](#design-rationale)
- [Reasoning For Any Final Changes](#Reasoning-for-any-final-changes)
- [Key Features](#key-features)
    - [User Registration and Login](#user-registration-and-login)
- [Deployment](#deployment)
    - [Platform](#platform)
    - [High Level Deployment Steps](#high-level-deployment-steps)
    - [Verification and Validation](#verification-and-validation)
    - [Security Measures](#security-measures)
- [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
    - [Code Generation](#code-generation)
    - [Debugging](#debugging)
    - [Performance and UX Optimisation](#performance-and-ux-optimisation)
    - [Automated Unit Testing](#automated-unit-testing)
    - [Overall Impact](#overall-impact)
- [Testing Summary](#testing-summary)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)


<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## User experience Design Process

- **Link to User Stories in GitHub Projects:**
- [Kanban Project board.](https://github.com/users/Navya-K-N-24/projects/7)

- **Wireframes**
![Homepage Wireframe across various devices](https://github.com/Navya-K-N-24/SpendWise/blob/fffc237c72fb0b3131fc0ec2bc60be79395bc355/Wireframe%20Homepage.png)
- The wireframes were created using Balsamiq Wireframes to map out the structure of the site on mobile, tablet, and desktop views. This guided the development of the site and ensured that the interface suited users on various devices.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
- **Design Rationale**
  - The layout is clean and minimalistic to make navigation intuitive for all users.
  - The color scheme ensures adequate contrast for readability, addressing accessibility guidelines (WCAG).
  - Typography choices prioritize readability across devices and assistive technologies.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
- **Reasoning For Any Final Changes**
  - Changes were made to improve usability, such as adjusting button sizes for mobile devices and ensuring keyboard accessibility across all interactive elements.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
## Key Features
- **Feature 1:** User Registration and Login 
  - Users can register with a secure password and log in to access their personalized dashboard.
  - **Inclusivity Notes:** 
    - The registration and login forms are designed to be accessible for keyboard navigation.
    - Field labels are clear and include descriptive error messages to assist users with visual impairments or cognitive challenges.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
## Deployment
- **Platform** Heroku
- **High-Level Deployment Steps** 
  1. Code was pushed to the GitHub repository linked with Heroku.
  2. A Procfile was created to specify the WSGI server (gunicorn).
  3. Environment variables for sensitive data, such as the database URL, were configured in Heroku.

- **Verification and Validation**
  - The deployed application was tested to ensure it matched the local development version in functionality.
  - Accessibility checks were performed using browser developer tools to verify keyboard navigation and color contrast compliance.

- **Security Measures**
  - Environment variables were used to store sensitive data, such as the database URL.
  - DEBUG mode was disabled in production to prevent exposure of sensitive information.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
## AI Implementation and Orchestration

### Use Cases and Reflections:

  - **Code Creation:** 
    - Strategic use of AI accelerated prototyping and coding processes. 
    - Examples: Prompts were used to generate alternative solutions for form validations.

  - **Debugging:** 
    - AI tools resolved syntax errors and optimized logic, making the codebase easier to maintain.
  - **Performance and UX Optimization:** 
    - Improvements included faster page load times and enhanced user experience through AI-recommended layout adjustments.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** 
    - Mobile, tablet, and desktop devices using Chrome, Firefox, and Edge.
  - **Features Tested:** 
    - Registration and login functionality.
    - Navigation and layout responsiveness.
  - **Results:** 
    - All features performed as expected.
- **Automated Testing:**
  - Tools Used: Django TestCase.
  - Features Covered: 
    - User authentication
    - Basic CRUD operations
  - Adjustments Made: 
    - Test cases were refined to handle edge cases, ensuring better coverage for accessibility.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
## Future Enhancements
- Add features to track income and savings alongside expenses.
- Introduce graphs and charts for better visualization of spending patterns.
- Improve accessibility further by adding voice input support for transaction entries.
<p align="right"><a href="#top">Back to top</a></p>
<hr/>
## Credits
- **Image Credits:**
Expense Tracker <a href="https://unsplash.com/@jakubzerdzicki?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jakub Żerdzicki</a> on <a href="https://unsplash.com/photos/a-person-is-writing-on-a-piece-of-paper-ykgLX_CwtDw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- **Wireframes:** 
    - Created using Balsamiq Wireframes

- **Images**
    -Hero image - Photo by <a href="https://unsplash.com/@mike_cho?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mike Cho</a> on <a href="https://unsplash.com/photos/a-tablet-computer-sitting-on-top-of-a-bed-next-to-a-cell-phone-zO8Crw8SoUM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      
      
<p align="right"><a href="#top">Back to top</a></p>
<hr/>