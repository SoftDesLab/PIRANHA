# Phishing Identifier and Remote Access Network or Hacking APIs
![GitHub Logo](https://github.com/SoftDesLab/PIRANHA/blob/JulkipliOMY/User_Interface/Pics_readme/logo.jpg) <br />
A program that detects phishing websites with machine learning by Python.

## Table of Contents

- [Getting Started](#getting-started) <br />
  - [Project Features](#project-features) <br />
- [Overview](#overview) <br />
  - [Requirements](#requirements) <br />
    - [Python Packages](#python-packages) <br />
    - [Graphical User Interface Packages](#graphical-user-interface-packages) <br />
    - [Database Packages](#database-packages) <br />
 - [User Manual](#user-manual) <br />
 - [Target Audience](#target-audience) <br />
 - [Focus Areas](#focus-areas) <br />
    - [Scenarios](#scenarios) <br />
    - [Languages](#languages) <br />
 - [User Stories](#user-stories) <br />
 - [System Architecture](#system-architecture) <br />
 - [Sample Screenshots](#sample-screenshots) <br />
 - [Authors](#authors) <br />
  
## Getting Started
The program focuses on Detecting Phishing Websites using Machine Learning to accurately detect the Phishing Websites. Phishing Websites targets the human vulnerabilities rather than the software vulnerabilities. It is the process of attracting online users in order to acquire the user’s sensitive information such as password and usernames. The program was developed using the Python programming language, the students programmed a machine learning algorithm in order to detect the phishing websites. The users of this program can use it to become aware on these phishing websites and protect their sensitive information by detecting phishing websites. 

**Keywords: Phishing, Phishing Websites, Detection, Machine Learning.**

### Project Features
This repository contains a program that has three features, listed as follows:
  1. Detects phishing websites, most especially, those of e-commerce websites,
  2. Displays a list of blacklisted phishing websites, and
  3. Illustrates a brief description about the program and the developers behind it.

## Overview
The students created a program that detects phishing websites using machine learning algorithm that checks whether the website is phishing or a safe website. The students used their knowledge that they obtained in the subject CPE106L and created a project that detects phishing websites with the use of machine learning algorithm, phishing websites are then stored in a file so that the program can comprehend and compare the differences between a phishing website and a non-phishing website. 

### Requirements
* **Any IDE (Integrated Development Enviroment Software)**, in this case, the developers used Visual Studio (VS) Code. <br />
To download, open your browser, head over to https://code.visualstudio.com/, and choose the software appropriate for your platform (Windows, Mac, or Linux).

* **Python** <br />
  Python is a high-level, general-purpose programming language with a reference implementation that compiles source code into bytecode before being executed on a process virtual machine.
  If you don't have Python already installed, run the following commands to install Python3 and pip3, the package manager for Python, into your Linux installation.
  ```
  $ sudo apt update
  $ sudo apt install python3 python3-pip3
  ```
  And to verify, run:
  ```
  $ python3 --version
  ```
### Definitions, Acronyms, and Abbreviations
* **Phishing** is a fraudulent attempt to acquire an individual’s sensitive data such as username, password, banking and credit card details.
* **Phishing Websites** tricks people into believing that they are on a legitimate website to steal your personal identifiable information.
* **Machine Learning** is an application of an artificial intelligence (AI) that helps programs to automatically learn from experience without being programmed by the user.
* **Human vulnerability** in cybersecurity, is the vulnerable link of humans to the information security chain since they tend to make mistakes such as clicking malicious links in phishing websites.
* **Software vulnerability** is a weakness in the software in an operating system (OS).
* **Detection** the ability of identifying the presence of something that is obscure.
* **Blacklist** is a list of things that are identified as deceitful and should be kept away from.
  
##### Python Packages:
* **Pandas** <br />
  Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure    is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables. <br />
  - To install pandas using pip, type in the terminal:
    ```
    $ pip install pandas 
    ```
    
* **Numpy** <br />
  Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and        tools for working with these arrays. <br />
  - To install numpy using pip, type in the terminal: 
    ```
    $ pip install numpy
    ```
    
* **Random** <br />
  Random is a built-in module that you can use to make random numbers. Some of its features are securing random generator using a secrets module which generates secure tokens, security keys, and URL, set the state of a random generator, generate random strings and passwords, and etc.
  
* **SKLearn** <br />
  Scikit-learn is a free built-in machine learning library for Python. It features various algorithms like support vector machine, random forests, and k-neighbours, and it also supports Python numerical and scientific libraries like NumPy and SciPy. <br />
  - To install SciKit-Learn, type in the terminal:
    ```
    $ pip3 install -U scikit-learn
    ```
    **Modules used in the program:**
    ```
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    ```
    
#### Graphical User Interface Packages:
* **PyQt5** <br />
  PyQt5 is one of the most used modules in building GUI apps in Python and that's due to its simplicity as you will see. Another great feature that encourages developers to use PyQt5 is the PyQt5 designer which makes it so easy to develop complex GUI apps in a short time. <br />
  - To install PyQt5 on Ubuntu, type in the terminal:
    ```
    $ pip3 install --user pyqt5  
    $ sudo apt-get install python3-pyqt5  
    $ sudo apt-get install pyqt5-dev-tools
    $ sudo apt-get install qttools5-dev-tools
    ```
    **Modules used in the program:**
    ```
    from PyQt5 import QtCore, QtGui, QtWidgets
    ```
    
#### Database Packages:
* **DBManager** <br />
  DBManager is the most powerful application for data management. With builtin support for MySQL, PostgreSQL, Interbase/Firebird, SQLite, DBF tables, MSAccess, MSSQL Server, Sybase, Oracle and ODBC database engines, it also brings you new features which make it the most advanced application.
  
* **SQLite 3** <br />
  SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle. <br />
  - To install SQLite 3 on Ubuntu, type in the terminal: 
    ```
    $ sudo apt-get install sqlite3
    ```
    
## User Manual
<img src="https://github.com/SoftDesLab/PIRANHA/blob/JulkipliOMY/User_Interface/Pics_readme/How.gif">

The user manual present the step-b-step procedure on how to use the P.I.R.A.N.H.A program focusing on website detection using Scikit-learn machine learning library.

**Instructions:**
  1. Install all the required packages as seen under the Requirements section.
  2. Clone the P.I.R.A.N.H.A repository to sync to your local machine.
     ```
     $ git clone https://github.com/SoftDesLab/P.I.R.A.N.H.A..git
     ```
  3. After cloning the repository, unzip the file folder to use.
  4. Add the folder to your IDE (Visual Studio Code, NetBeans, Sublime Text...).
  5. Go to the main.py and insert the path of the Application_Layer to run the python scripts.
     ```
     sys.path.insert(0, "[Path of Application_Layer]")
     ```
  6. Debug and run the program.
  7. A GUI platform will be displayed; the program has three pages that represents each functionality:
  
 * **Home** <br />
   The home page serves as the starting point of the program. It presents the main capability of the program which is to scan the
   suspicious website entered by the suer. Once, the website has been scanned by the feature_extraction.py. The Tfidvectorizer's
   purpose is to convert a collection of data to a matrix of TF-IFF or features in the prediction function then after that the
   program convers the url into streams of tokens which are then separated by word and punctuation then return the prediction to
   test the dataset and predict the probability of the URL in a categorical dependent varible which is in binary through Logistic 
   Regression if it is safe or not. Then, the status of the suspicious website will be displayed.
    
 * **Blacklist** <br />
   The blacklist page serves as to where the proven phishing websites are added to the dataset. the list of captured phishing websites
   are presented in a table once the user refresh since it is in a real-time basis. In addition, a bar graph is presented to showcase
   the number of websites in a dataset to interpret where the machine learning program is basing on.
  
* **About Us** <br/>
   The About us page is where the insights of the developers involved in the Team page while an overview of the program in the Project Page.
   
## Target Audience
For this repository, our target audience are Data Analysts, students and teachers of Computer Engineering, Computer Science, and Information Technology. As our content in this repository, the Detection of Phishing Websites and the list of Black listed websites.

## Focus Areas
This repository aims to give understanding on how Detecting Phishing Websites works.

### Scenarios
We aim to have scenarios that helps the users to be aware of Phishing Websites. This program helps user to distinguish whether the Website is a Phishinhg Website or a real website.

### Languages
The language that our program uses is SQL (Structured Query Language) is a database management language for relational databases. The programming language that the program uses is the Python programming language which is an interpreted, object-oriented, high-level programming language with dynamic semantics.

## User Cases
1. Actors
     * **Customer User** <br />
     
         - The customer are the users who will benefit from the program. The actions that they can perform are to scan any website link,           store the phishing website link to the blacklist, view the bar graph of fraud and safe sites and show the information about             the program and its authors.
     * **Software Developer** <br />
     
         - The software developers created the program using machine learning algorithm to determine whether the site is safe or not.              They are also the one who manages the database of the application and the listed phishing websites in the blacklist.
2. List of Use Cases
     * **Customer User Cases** <br />
     
       - Scan link
         - The user will enter a suspicious website, then the application will scan the website. The URL is converted into different                data through functions in the program and is tested in a categorical dependent variable that is in binary using linear                  regression to determine if the site is safe or not.
       - Display Blacklist
         -	If the user has identified that the website is a phishing website, then the user can add it to the blacklist to feed the                 dataset. The list of these data is displayed in a table once the user clicks the refresh button because it is in a real-time             basis. The user can also view the graph which presents all the websites entered in the database.
       - Show Program and Developers Information
         - The user can view the insights of the team who created the program and its background.
     * **Software Developer Case** <br />
     
       - Manage Stored Data
         - The developers manages the database of the application. They can create, read, update and delete the database of the website             list.
  
## System Architecture
* **Case Diagram**
![UML Case Diagram-1](https://user-images.githubusercontent.com/40769687/80790810-5e494d80-8bc2-11ea-8e95-67beebe3434e.png)
* **Classes Diagram**

![UML PIRANHA](https://user-images.githubusercontent.com/40769687/80791010-f1828300-8bc2-11ea-82b4-f4bbc75fa7ef.png)

## Sample Screenshots
## Authors
* **Leaders:** <br />
  * *Garcia, Joshua Ron G.* (https://github.com/peculiarNoobie)
  * *Julkipli, Omar Mukhtar Y.* (https://github.com/OmarJulkipli)
* **Members:** <br />
  * *Abarquez, Arnett Johneill M.* (https://github.com/Arnett0822)
  * *Alde, Regina Bianca A.* (https://github.com/alderegina)
  * *Apelo, Mary Lee D.* (https://github.com/mary18lee)
  * *Gonzales, Joshua C.* (https://github.com/Joshinobi)
  * *Ronquillo, Dominic Narciso T.* (https://github.com/DominicRonquillo)
