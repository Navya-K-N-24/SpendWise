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

  - **Inclusivity Notes:** 
    - The registration and login forms are designed to be accessible for keyboard navigation.
    - Field labels are clear and include descriptive error messages to assist users with visual impairments or cognitive challenges.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 2: Add Transaction
 
  - Users can add transactions & track their expenses.

  - **Inclusivity Notes:** 
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

  - **Inclusivity Notes:** 

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

**Screenshots:**
(You can add any relevant screenshots showing the transaction list, edit form, and the updated transaction list after editing.)

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

### Feature 4: Delete Transaction
 
  - Users can Delete transactions so can remove incorrect or unwanted entries.
  - **Inclusivity Notes:** 

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

**Screenshots:**
(You can add any relevant screenshots showing the transaction list, edit form, and the updated transaction list after editing.)

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Deployment
### Platform: Heroku
### High-Level Deployment Steps 
  1. Code was pushed to the GitHub repository linked with Heroku.
  2. A Procfile was created to specify the WSGI server (gunicorn).
  3. Environment variables for sensitive data, such as the database URL, were configured in Heroku.

### Verification and Validation
  - The deployed application was tested to ensure it matched the local development version in functionality.
  - Accessibility checks were performed using browser developer tools to verify keyboard navigation and color contrast compliance.

### Security Measures
  - Environment variables were used to store sensitive data, such as the database URL.
  - DEBUG mode was disabled in production to prevent exposure of sensitive information.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## AI Implementation and Orchestration

### Code Generation
  - Strategic use of AI accelerated prototyping and coding processes. 
  - Examples: Prompts were used to generate alternative solutions for form validations.

### Debugging
  - AI tools resolved syntax errors and optimized logic, making the codebase easier to maintain.

### Performance and UX Optimization
  - Improvements included faster page load times and enhanced user experience through AI-recommended layout adjustments.

### Automated Unit Testing
  - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

### Overall Impact
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

<p align="right"><a href="#top">Back to top</a></p>
<hr/>

## Testing Summary
### Manual Testing:
  - **Devices and Browsers Tested:** 
    - Mobile, tablet, and desktop devices using Chrome, Firefox, and Edge.
  - **Features Tested:** 
    - Registration and login functionality.
    - Navigation and layout responsiveness.
  - **Results:** 
    - All features performed as expected.

### Automated Testing:
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
  - **Expense Tracker README image**
      Photo by <a href="https://unsplash.com/@umbra_media?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Christopher Bill</a> on <a href="https://unsplash.com/photos/5-pieces-of-banknotes-on-yellow-and-white-textile-rrTRZdCu7No?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  - **Hero image**
      Photo by <a href="https://unsplash.com/@mike_cho?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mike Cho</a> on <a href="https://unsplash.com/photos/a-tablet-computer-sitting-on-top-of-a-bed-next-to-a-cell-phone-zO8Crw8SoUM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- **Wireframes:** 
    - Created using Balsamiq Wireframes

#### Acknowledgements

Many thanks to:
* Code Institute team (Fecilitator - Dillon,SME Coach - Mark, Coading Coach team - Roo & John, Slack channel members) for your patience in making me understand the concept and techniques while answering all my questions,
* Everyone from WECA group for being kind, supportive & helpful leading throughout learning of building this project,

<p align="right"><a href="#top">Back to top</a></p>
<hr/>
