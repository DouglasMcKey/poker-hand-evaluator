# PokerHandEvaluator

Welcome to Poker Hand Evaluator. A tool to quickly rank a five card poker hand.

This project was built with the following:
- [Angular CLI](https://github.com/angular/angular-cli) version 21.0.3.
- [Django](https://www.djangoproject.com) version 6
- [Python](https://www.python.org/downloads/release/python-3130/) version 3.13

---

## Development Servers

The project requires two servers:
- Angular - Manages the front end.
- Django - Manages the back end.
- 
To experience the application. Setup and run both the front-end and back-end servers.
Then navigate to the front-end server URL: `http://localhost:4200/`

### NOTE: See details below for server setup.

---

## Front-End Server Setup
### Node.js

Go to https://nodejs.org

Download the LTS (Long Term Support) version.
Run the installer and follow the instructions.

This will install:
- Node.js
- npm (package manager for Node.js)

#### Helpful Commands:

```bash
node -v
```

```bash
npm -v
```

---

### Angular

Install Angular.

```bash
npm install -g @angular/cli
```

#### Helpful Commands:

```bash
ng version
```

---

### Run the Front-End Server:

To start the front-end server. Navigate to the project's frontend folder:

`poker-hand-evaluator/front-end/`

and execute the following command:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`.


## Testing the Front-End

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

### No tests for the front-end have been developed just yet.

---

## Back-end Server Setup

Ensure that you have Python and PIP installed.

#### Helpful Commands:

```bash
python --version
```

```bash
pip --version
```

---

### pipenv
This project uses pipenv for the back-end virtual environment.

#### Install pipenv
```bash
pip install pipenv
```
---

#### Create and run virtual environment.
Navigate to the `backend` folder of the project.

Create the virtual environment:
```bash
pipenv sync
```

Run the back-end server in the virtual environment:
```bash
pipenv run python manage.py runserver
```

Confirm that the back-end server is running:
```bash
http://127.0.0.1:8000/
```
---

## Testing the Back-End
To execute unit tests on the backend, use one of the following command:
```bash
pipenv run python manage.py test api.tests.test_interfaces -v 2 --failfast
```

```bash
pipenv run python manage.py test
```
