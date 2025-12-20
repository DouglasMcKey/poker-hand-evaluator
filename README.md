# PokerHandEvaluator

Welcome to Poker Hand Evaluator. A tool to quickly rank a five card poker hand.

This project was built with the following:
- [Angular CLI](https://github.com/angular/angular-cli) version 21.0.3.
- [Django](https://www.djangoproject.com) version 6

---

## Development Servers

The project requires two servers:
- Angular - Manages the front end.
- Django - Manages the back end.

---

### Run the Front-End Server:

To start the front-end server. Navigate to the project's frontend folder:

`poker-hand-evaluator/front-end/`

and execute the following command:
```bash
ng serve
```

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

#### Helpful Commands:

```bash
npm install -g @angular/cli
```

```bash
ng version
```

---

---
---

---



Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
