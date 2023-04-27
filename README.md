# Table of contents
* [Purpose](#purpose)
* [User Experience](#user-experience)
  * [User Stories](#user-stories) 
  * [Design](#design)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features Left To Implement](#features-left-to-implement)
* [Technologies](#technologies)
* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

# Milestone Project 4 - Guild Wars 2 Blog
## Purpose

This website was created to complete the fourth Milestone Project for Code Insitute's Full Stack Software Developer course. I built this from the ground up using knowledge I gained from the previous modules. The objective of this project is to showcase my ability to create a true Full Stack application using the Django framework. The full list of technologies used can be found in the technologies section further down.

Users of this website are able to create, read, update and delete posts regarding any subject in the gaming industry.

You can find the link to the live website right [here]
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![image](am i responsive image)

***

# User Experience
## User Stories
### First Time User Goals
<details><summary>First Time User Goals</summary>

* As a First Time User, I clearly understand the main objective of the website.
* As a First Time User, I can easily navigate through the website.
* As a First Time User, I can register an account to gain full access to the website.
* As a First Time User, I can view more from the game.
* As a First Time User, I can choose a post I would like to inspect further.
</details>
<details><summary>Frequent User Goals</summary>

* As a Frequent User, I can log in to gain access to my account.
* As a Frequent User, I can comment on a blog post with my thoughts on the subject.
* As a Frequent User, I can like a post to show that I enjoyed it.
* As a Frequent User, I can change aspects of my personal account details.
* As a Frequent User, I can change my password incase their is a security risk.
</details>

<details><summary>Admin User Goals</summary>

* As an Admin, I can create, read, update and delete posts so that I can manage my blog content.
* As an Admin, I can create draft posts so that I can finish writing the content later.
* As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
</details>

***
## Design

<details>
<summary>Wireframes</summary>

* Home Page Desktop + Mobile:

![landing-page-wireframe](media/home-page-wireframe.jpg)

* Create a Post:

![post-content-wireframe](media/create-post-wireframe.jpg)

* Edit Profile:

![add-post-wireframe](media/edit-profile-wireframe.jpg)

* Log In:

![log-in-wireframe](media/login-wireframe.jpg)

</details>

<details><summary>Imagery</summary>
The images you are greeted to when entering the website are of varying style. Most of the photos you will see are uploaded by the user, but the header image will always be as shown below. This is also used as the placeholder image when a user chooses to not upload a photo to their post.

![Imagery](header image)
</details>

<details><summary>Color Scheme</summary>
Three colors are used in this website, these being #000000, #FFFFFF and #FF0030. The background, text and foreground colors have a sufficient contrast ratio to aid with accessibility.

</details>

# Features
## Existing Features
<details><summary>Home Page</summary>
 
The first thing users are greeted to is the Home Page. This is where you will find everything to navigate the website.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I clearly understand the main objective of the website.
```
![image](media/home-page-snip.jpg)
 
</details>

<details><summary>Navigation Bar</summary>
 
Featured at the top of all pages is the nav bar, holding the Guild Wars 2 thumbnail logo and all links to the home page, register and login page.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can easily navigate through the website.
```
![image](media/nav-bar-snip.jpg)

Using Bootstrap I have used .navbar-toggler class to make the nav bar more user friendly on smaller screens.

![image](media/mobile-nav-snip.jpg)

</details> 

<details><summary>Footer</summary>
 
Featured at the bottom of all pages is the footer, holding links to places where Guild Wars 2 is featured, Facebook, The games website and their youtube account.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can view more from the game.
```
![image](media/footer-snip.jpg)
 
</details>

<details><summary>Post Detail</summary>
 
When one of the posts on the home page is clicked, the user is taken to post detail view. Here the user can see the author, date/time posted and the content itself (one thing I have noticed is that Daylight savings isn't taken into account).

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can choose a post I would like to inspect further.
```
![image](media/post-detail-snip.jpg)
 
</details>

<details><summary>Like/Unlike</summary>
 
Just below the post itself, two icons are visible. One of these being a clickable Like button that can only be interacted with when the user has logged in. The second icon shows the amount of comments the post has recieved.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can like a post to show that I enjoyed it.
```

</details>

<details><summary>Post Comments</summary>
 
At the bottom of the post is the comments section, where the user is able to write and post a comment on the blog post.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can comment on a blog post with my thoughts on the subject.
```
![image](media/comment-snip.jpg)

When the user has posted a comment, an alert replaces the text field letting them know that their comment is awaiting inspection and approval.

The purpose of this is to fulfill the following user story:
```
As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
```
 
</details>

<details><summary>Add Post</summary>
 
This page of the website allows the user to create their own blog post. I implemented a rich text editor which allows the user to add a bit more style to their post. For security reasons I have to give the user staff privileges to be able to post, which is common practice in other professional websites. This is to ensure that not just anyone off the internet can find my website and post questionable things.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can create my own blog post and post it on the website.
```
![image](media/create-new-post-snip.jpg)

</details>

<details><summary>Edit/Delete Post</summary>
 
If the user is the author of the post, two buttons appear on the post detail section giving them the ability to edit or delete the post. This is to aid the user in correcting issues with the post, or just to delete it and start again fresh.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can edit or delete my own posts.
```

![image](media/edit-delete-snip.jpg)

When the user clicks the delete button they are taken to a new page with a warning, making sure they are aware that they are about to permanently delete the post. This is so if they change their mind and want to keep it, they can.

![image](media/delete-post-snip.jpg)

</details>

<details><summary>Register</summary>
 
If the visitor likes the website, they are able to register an account. This enables the user to be able to like and comment on posts.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can register an account to gain full access to the website.
```
![image](media/register-snip.jpg)

</details>

<details><summary>Log In</summary>
 
When the user returns to the website to see if any more blog posts have been created, they are able to log back in.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can log in to gain access to my account.
```
![image](media/log-in-snip.jpg)

</details>

<details><summary>Edit Profile</summary>
 
This page of the website enables the user to edit specific things regarding their account. These being:
* Username
* Email
* First Name
* Last Name

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can change aspects of my personal account details.
```
![image](media/edit-profile-snip.jpg)

</details>

<details><summary>Change Password</summary>
 
Within the Edit Profile page the user also has the option to click a link to take them to a page allowing them to change their password. 

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can change my password incase their is a security risk.
```
![image](media/password-change-snip.jpg)

When the user has confirmed their new password, they are taken to a page informing them that the change was successful.

</details>

## Features Left to Implement

<details><summary>Password Reset</summary>
I would like to implement a password reset feature. This would send an email to the users associated email address with a temporary password. They would then use the temp password to gain access to their account and change their password manually.
</details>

<details><summary>Contact Us</summary>
I would like to eventually implement a Contact Us page to the website. Users would be able to send enquiries to me via a form.
</details>

<details><summary>Reply to comments</summary>
I would like to add a feature that allows the user to reply to comments on a post. This could be a reply in a thread format or something else entirely. This would add a personal touch to the comments section, enabling users to interact with one another.
</details>

***

# Technologies

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
* [Heroku](https://dashboard.heroku.com/)
    * Heroku is the site used to deploy the project.
* [GitHub](https://github.com/)
    * GitHub is the hosting site I used to store the code for the website.
* [GitPod](https://gitpod.io/)
    * GitPod is the Integrated Development Environment used to develop the website in a browser.
* [Font Awesome](https://fontawesome.com/)
    * Font Awesome icons are used for the social media links located in the Footer section of the website.
* [Google Fonts](https://fonts.google.com/)
    * Google fonts are used in the project to import the **Pangolin** font.
* [Am I Responsive?](http://ami.responsivedesign.is/)
    * Am I Responsive is used to generate the website mock up.
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
    * The built in developer tools in Google Chrome are used to test CSS styles, inspect page elements and help with debugging problems with the layout of the website.
* [Stack Overflow](https://stackoverflow.com/)
    * Stack Overflow was the primary source for help regarding issues.
* [W3 Schools](https://www.w3schools.com/)
    * W3 Schools was one of the websites used for resolving issues with code.

***

# Testing

## Validator Testing

### Code Validation

To ensure all code for the Guild Wars 2 blog was correct, validation through various validators was performed. The results are listed below.

* HTML Validation

  All HTML code was checked with the [W3C Markup Validation Service](https://validator.w3.org/).

   <details>
   <summary>Home Page</summary>

   ![image](media/base-html-validator-pass.jpg)

   </details>
   <details>
   <summary>Add Post</summary>

    One error returned. As seen in the code below, I have had to use {{ form.as_p }} to get the rich text editor to function correctly. As of right now I am unsure of a solution.

   ![image](media/Add-post-validator-error.jpg)

   </details>
   <details>
   <summary>Sign Up</summary>

   ![image](media/register-validator-pass.jpg)

   </details>
   <details>
   <summary>Log In</summary>

   ![image](media/log-in-validator-pass.jpg)

   </details>
   <details>
   <summary>Edit Profile</summary>

   ![image](media/edit-profile-validator-pass.jpg)

   </details>
   <details>
   <summary>Log Out</summary>

   ![image](media/log-out-validator-pass.jpg)

   </details>
   
* CSS Validation

  All CSS code was checked with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

   <details>
   <summary>CSS Results</summary>

   ![image](media/css-validator-pass.jpg)

   </details>
   
* Python Validation

  All Python code was checked with the [PEP8 Online Service](http://pep8online.com/).

  <details>
  <summary>admin.py</summary>

  ![image]

  </details>
  <details>
  <summary>apps.py</summary>

  ![image]

  </details>
  <details>
  <summary>forms.py</summary>

  ![image]

  </details>
  <details>
  <summary>models.py</summary>

  ![image]

  </details>
  <details>
  <summary>urls.py</summary>

  ![image]

  </details>
  <details>
  <summary>views.py</summary>

  ![image]

  </details>

* Accessibility

  The websites accessibility was tested with lighthouse in the Dev tools.

  <details>
  <summary>Lighthouse Summary</summary>

  ![image](media/lighthouse-homepage-score.jpg)

  </details>

## Manual Testing

  I tested that the website is responsive, functions well and looks good on all screen sizes using Google Dev Tools.

  <details><summary>Google Doc</summary>

  ![image](media/manual-test-page-1.jpg)
  ![image](media/manual-test-page-2.jpg)

  there are more tests that I completed and I can make the spreadsheet available to those who wish to see it.

  </details>

***

## Bugs



***

# Deployment

 This project was deployed using Code Institute's mock terminal for Heroku.
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy

***

# Credits
