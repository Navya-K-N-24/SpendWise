# SpendWise

Welcome to SpendWise, A tracking tool to your expenses!

![Expense Tracker Image](https://github.com/Navya-K-N-24/SpendWise/blob/5fa61b7c3b610e223bbe7c4e66c125063bdb4604/README%20image.jpg))

## Overview
SpendWise is a web-based expense tracker designed to help users manage their finances efficiently. The platform offers secure user registration and login, allowing users to add, view, edit, and delete transactions. With SpendWise, users can generate detailed reports to analyze their spending patterns and make informed financial decisions. The project is built using Django, and it incorporates responsive design, real-time notifications, and secure access control to enhance user experience and data security.

Live site: [https://spendwisenavya-47b3e163d0fa.herokuapp.com/](https://spendwisenavya-47b3e163d0fa.herokuapp.com/)

## Table of Contents
- [User Experience Design Process](#user-experience-design-process)
    - [Link to User Stories in GitHub Projects](#link-to-user-stories-in-github-projects)
    - [Wireframes](#wireframes)
    - [Design Rationale](#design-rationale)
    - [Reasoning For Any Final Changes](#reasoning-for-any-final-changes)
- [Key Features](#key-features)
    - [User Registration and Login](#feature-1-user-registration-and-login)
    - [Add Transaction](#feature-2-add-transaction)
    - [Edit Transaction](#feature-3-edit-transaction)
    - [Delete Transaction](#feature-4-delete-transaction)
    - [Role-Based Login and Registration](#feature-5-role-based-login-and-registration)
- [Deployment](#deployment)
    - [Platform](#platform)
    - [High-Level Deployment Steps](#high-level-deployment-steps)
    - [Verification and Validation](#verification-and-validation)
    - [Security Measures](#security-measures)
- [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
    - [Code Generation](#code-generation)
    - [Debugging](#debugging)
    - [Performance and UX Optimization](#performance-and-ux-optimization)
    - [Automated Unit Testing](#automated-unit-testing)
    - [Overall Impact](#overall-impact)
- [Testing Summary](#testing-summary)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## User Experience Design Process

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Link to User Stories in GitHub Projects
[Kanban Project board.](https://github.com/users/Navya-K-N-24/projects/7)

### Wireframes
![Homepage Wireframe across various devices](https://github.com/Navya-K-N-24/SpendWise/blob/fffc237c72fb0b3131fc0ec2bc60be79395bc355/Wireframe%20Homepage.png)
- The wireframes were created using Balsamiq Wireframes to map out the structure of the site on mobile, tablet, and desktop views. This guided the development of the site and ensured that the interface suited users on various devices.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Design Rationale
  - The layout is clean and minimalistic to make navigation intuitive for all users.
  - The color scheme ensures adequate contrast for readability, addressing accessibility guidelines (WCAG).
  - Typography choices prioritize readability across devices and assistive technologies.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Reasoning For Any Final Changes
  - Changes were made to improve usability, such as adjusting button sizes for mobile devices and ensuring keyboard accessibility across all interactive elements.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Key Features

### Feature 1: User Registration and Login 

  - Users can register by filling the required details and a secure password and log in to access their personalized dashboard.

  - **Implementation:** 
    - The registration and login forms are designed to be accessible for keyboard navigation.
    - Field labels are clear and include descriptive error messages to assist users with visual impairments or cognitive challenges.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 2: Add Transaction
 
  - Users can add transactions & track their expenses.

  - **Implementation:** 
    - The user can access the "Add Transaction" form from the main interface.

    - Enter Transaction Details.
      - The user can input the transaction date.
      - The user can input the amount spent.
      - The user can choose a category (e.g., groceries, entertainment).
      - The user can add a description or note about the transaction.
    
    - Validation
      - The form ensures all required fields are filled before submission.
      - The input is validated for the correct date format and numeric values for amount.

    - Save Transaction
      - After submitting the form, the transaction is saved to the database.
      - A confirmation message is displayed upon successful submission.
      - The newly added transaction is displayed in the transactions list.
    
    - Error Handling
      - If the user provides invalid data, appropriate error messages are shown next to the relevant form fields.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 3: Edit Transaction
 
  - Users can edit transactions & correct any mistakes.

  - **Implementation:** 

    - Navigate to Transactions:
      - Users can view the list of all transactions and identify the transaction they want to edit.

    - Initiate Edit:
      - Users can select a transaction from the list and click on the "Edit" button to modify its details.
    
    - Edit Form:
      - The edit form is pre-populated with the current details of the selected transaction.
      - Users can edit the following details:
        - Transaction Date
        - Amount Spent
        - Category
        - Description

    - Validation:
      - The form ensures that all required fields are filled out.
      - Input data is validated, ensuring proper formats (e.g., date format, numeric values for amounts).

    - Save Changes:
      - Users can save their changes to the transaction by submitting the form.
      - After saving, a confirmation message is displayed to inform the user that the changes have been successfully saved.
      - The transaction list is updated to reflect the modified details.

    - Cancel Changes:
      - Users can cancel editing without saving changes. In this case, the transaction details remain unchanged.

    - Error Handling:
      - Error messages are displayed next to the relevant form fields if any validation issues occur (e.g., missing required fields or incorrect data formats).

  **Steps to Edit a Transaction:**

    - 1. View the Transaction List: Access the list of transactions from the homepage.
    - 2. Select the Transaction: Click on the "Edit" button next to the transaction you want to edit.
    - 3. Edit the Form: Modify the details of the transaction in the provided form fields.
    - 4. Save Changes: Click "Save" to update the transaction. A confirmation message will appear.
    - 5. Cancel Changes: If you decide not to edit the transaction, click "Cancel" to return to the transaction list without saving changes.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 4: Delete Transaction
 
  - Users can Delete transactions so can remove incorrect or unwanted entries.
  - **Implementation:** 

    - Navigate to Transactions:
      - User can access the list of transactions.
      - User can identify the transaction to be deleted.

    - Initiate Delete:
      - User can select the transaction they want to delete.
      - User clicks on the "Delete" button for the selected transaction.
    
    - Confirmation:
      - User is prompted to confirm the deletion.
      - User can confirm or cancel the deletion.

    - Successful Deletion:
      - Transaction is removed from the list upon confirmation.
      - User receives a confirmation message after successful deletion.

    - Cancel Deletion:
      - User can cancel the deletion process.
      - No changes are made if deletion is canceled.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 5: Role-Based Login and Registration
 
  - Users can register and log in with role-based authentication, so can have different access levels (admin or user).

  - **As an admin**, User is able to perform administrative tasks.

  - **As a user**, User can add, edit, view, and delete transactions on dashboard.

  - **Implementation:** 

    - Created a custom user model (`CustomUser`) for role-based authentication, which includes two roles: **admin** and **user**.

    - Implemented the ability to register, log in, and redirect users based on their roles.

    - The login view checks the user's role and redirects accordingly (to the dashboard for a user and to an admin panel for an admin).

    - The user dashboard displays all the transactions for the logged-in user with management functionalities (add, edit, delete) for the user to perform.
      role.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Deployment
### Platform: Heroku
The web app is hosted on Heroku using Eco Dynos, and is deployed via the designated Github repository.

A request is made via the CI Database Maker, which generates a PostgreSQL database hosted on AWS, with the database credentials sent to the email address provided in the request.

### High-Level Deployment Steps 

The [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template) was used to create the GitHub repository, so that the website could be developed in the correct setup of Gitpod IDE.

The GitHub Copilot extension was also installed in my local client version of MS VS Code, which was also connected with the same GitHub repository and linked to Gitpod via SSH. This allows for AI pair programming in the initial stages of development to create certain sections faster.

The deployment process is as follows:
1. Login to your GitHub profile and go to [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template). **Use this template** and **Create a new repository**.
2. Open the Code Institute Gitpod IDE workspace. Open Gitpod workspace. Create the MVP.
3. Login to Heroku and create a new app using a unique name and select the correct region. Add Config Vars in Settings.
4. Install web server gunicorn and freeze requirements.
5. Create a new Procfile in the root directory and specify the running of the web app with process type as gunicorn in the Procfile.
6. Environment variables for sensitive data, such as the database URL, were configured in Heroku.
7. Add deployed apps to ALLOWED_HOSTS in settings.py, and set Debug = False. Add, commit and push to the Github repo.
8. In Heroku, go to Deploy tab, search for the correct Github repo and under manual deploy click **Deploy Branch**.
9. **View app** to verify that it is been deployed correctly. This deployed site can now be validated and tested e.g. in Chrome Dev Tools.
10. In the app's Resources tab, check that Eco Dynos are used and remove any unnecessary Add-ons.
11. Subsequent changes to the code will need to be pushed to the Github repo and manually deployed on Heroku.

### Verification and Validation
  - The deployed application was tested to ensure it matched the local development version in functionality.
  - Accessibility checks were performed using browser developer tools for color contrast compliance.

### Security Measures
  - Environment variables were used to store sensitive data, such as the database URL.
  - DEBUG mode was disabled in production to prevent exposure of sensitive information.

Validation of HTML/CSS, Lighthouse Audits, Bugs
#### HTML Validation
Add details of HTML validation:
<details>
  <summary>HTML Home page validation screenshots:</summary>
  <b>[Add screenshots](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/home_page_validation.PNG)</b>
</details>

<details>
  <summary>HTML About page validation screenshots:</summary>
  <b>[Add screenshots]([https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/home_page_validation.PNG](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/about_page_validation.PNG))</b>
</details>

<details>
  <summary>HTML Login page validation screenshots:</summary>
  <b>[Add screenshots]([[https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/home_page_validation.PNG](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/about_page_validation.PNG](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/login_page_validation.PNG)))</b>
</details>


#### Python Linter
- Used [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to check all Python code I have written meets the PEP8 standard and got no warnings. Results from linting one of the files (test_models.py) has been included below:<br>

<details>
  <summary>test_models.py:</summary>
    
  ![python_linter_example_test-models](https://github.com/user-attachments/assets/47a4c704-a8a4-4d10-8983-3498ca15d851)

</details>

#### Device Responsivness across Devices
SpendWise is designed to be fully responsive across all device sizes, ensuring an optimal user experience whether accessed on mobile, tablet, or desktop. The design follows a mobile-first approach, based on the hypothesis that the majority of users maange expenses on their smartphones.

To achieve this, the layout adapts seamlessly to different screen sizes using a combination of Bootstrap's grid system and Flexbox, applied strategically to maintain consistency and usability across devices.
![Responsivness across all devices](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/device_responsivness1.PNG)
![responsivness of all pages](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/device_responsivness2.PNG)

#### Lighthouse Audit
Chrome Dev Tools Lighthouse was used to audit the site for response time and accessibility. Testing was done during MVP development after deploying v1 Homepage with only the cards of published scrapbooks, allowing more time for bug fixes.<br>

Screenshots of Lighthouse Audit on the Homepage 

Mobile:
![image]([https://github.com/](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/lighthouse_testing_mobile.PNG))

Tablet:
![image]([https://github.com/](https://github.com/Navya-K-N-24/SpendWise/blob/c8f2490bb7646b83a8182a284f696a887a66daab/lighthouse_testing_tablet.PNG))

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## AI Implementation and Orchestration

Throughout this project, I relied on GitHub Copilot to streamline development and testing. This was my first time using AI tools so extensively, and it became an invaluable collaborator during the process.

- **Code Creation:** 
  - Reflection: Initially, I was hesitant about how much I could rely on Copilot, but I quickly saw its value in generating boilerplate code, like Django models and CRUD views. Using reverse and multi-step prompts gave me the confidence to explore alternative approaches, and it even taught me new techniques I hadn’t considered before. For instance, it suggested cleaner, more Pythonic ways to handle database queries that saved me time and effort.
  - Highlight: The iterative back-and-forth with Copilot felt like having a knowledgeable pair programmer by my side. This collaboration made me more thoughtful about how I structured my prompts, as clearer questions led to better answers.

- **Debugging:** 
  - Reflection: Debugging with Copilot was a learning experience in itself. It didn’t just find errors; it often suggested solutions that highlighted gaps in my understanding. I appreciated how it encouraged me to simplify complex logic, making the code easier to maintain and more accessible to anyone who might work on it in the future.

- **Performance and UX Optimization:** 
  - Reflection: One of my proudest moments came when I used Copilot to refine the Bootstrap styling. I wasn’t very confident in front-end design, but the AI helped bridge that gap. It suggested small, impactful changes, like improving button alignment and tweaking breakpoints, that made the application feel polished and professional. These adjustments also ensured that the app was truly responsive, which was a priority for me.

- **Automated Unit Testing:**
  - Reflection: Writing unit tests has always been a challenging aspect of development for me, but Copilot turned it into a manageable task. I used question-and-answer and multi-step prompts to generate a solid starting point for my test cases, which I could then refine to align with the project’s requirements. Seeing it anticipate edge cases—like invalid user input—made me more aware of the importance of writing comprehensive tests. This process deepened my understanding of Django’s testing framework and made me more confident in my ability to create robust applications.

### Overall Impact
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Testing Summary

### Automated Testing
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]

  - **Features Tested:** 
    - **Unit Tests**
      - Unit tests have been implemented for the following key features:
        - User Registration: Tests the registration functionality, ensuring that users can register with valid data and are redirected correctly.
        - User Login: Tests the login functionality, ensuring that users can log in successfully with valid credentials.
        - Transaction CRUD Operations: Tests the creation, updating, and deletion of transactions. Ensures that the CRUD operations work as expected, and data is properly saved 
          and modified in the database.

      - **Integration Tests**
        - Integration tests have been written to ensure end-to-end functionality, covering:
          - The interaction between different components (e.g., creating a transaction after a successful login).
          - Ensuring that the user flow works from registration to login to CRUD operations for transactions.

  - **Running Tests**
    - To run the tests for the application, use the following command:
    - python3 manage.py test tracker

  - **Testing Coverage**
    - **User Registration & Login:** Ensures that users can successfully register and log in with valid credentials.
    - **Transaction Operations:** Verifies that users can create, update, and delete transactions correctly.

  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]

### Manual Testing:
  - **Devices and Browsers Tested:** 
    - Mobile, tablet, and desktop devices using Chrome, Firefox, and Edge.
  - **Features Tested:** 
    - Registration and login functionality.
    - Navigation and layout responsiveness.
  - **Results:** 
    - All features performed as expected.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Future Enhancements
- Add Data Visualization to view a visual representation of expenses so the User can better understand the spending habits by Graphs or charts showing spending by category, date, or other criteria.
- Add Reports Generation to generate expense reports so that User can analyze their spending over a specific period

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Credits
- **Image Credits:**
  - **Expense Tracker README image**
      Photo by <a href="https://unsplash.com/@umbra_media?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Christopher Bill</a> on <a href="https://unsplash.com/photos/5-pieces-of-banknotes-on-yellow-and-white-textile-rrTRZdCu7No?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  - **Hero image**
      Photo by <a href="https://unsplash.com/@mike_cho?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mike Cho</a> on <a href="https://unsplash.com/photos/a-tablet-computer-sitting-on-top-of-a-bed-next-to-a-cell-phone-zO8Crw8SoUM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  - **About page images**
      - Photo by <a href="https://unsplash.com/@isaacmsmith?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Isaac Smith</a> on <a href="https://unsplash.com/photos/pen-om-paper-AT77Q0Njnt0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      - Photo by <a href="https://unsplash.com/@jakubzerdzicki?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jakub Żerdzicki</a> on <a href="https://unsplash.com/photos/a-person-is-writing-on-a-piece-of-paper-ykgLX_CwtDw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      - Photo by <a href="https://unsplash.com/@jakubzerdzicki?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Kenny Eliason</a> on <a href="https://unsplash.com/photos/a-person-is-writing-on-a-piece-of-paper-ykgLX_CwtDw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
        
- **Wireframes:** 
    - Created using Balsamiq Wireframes

#### Acknowledgements

Many thanks to:
* Code Institute team (Learning Facilitator - Dillon Mc Caffrey, SME Coach - Mark Briscoe, Coading Coach team - Ruairidh MacArthur & John Rearden, Slack channel members) for your patience in making me understand the concept and techniques while answering all my questions,
* Everyone from WECA group for being kind, supportive & helpful leading throughout learning of building this project,

<p align="right"><a href="#top">Back to top</a></p>
<hr/>
