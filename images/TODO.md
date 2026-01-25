# The 120-Step Road to Senior Engineer: Senteng Fashions Transformation

This is not just a to-do list. It is a curriculum. Completing these 120+ tasks simulates 2-3 years of industry experience packed into a high-intensity building period.

## Phase 1: Initiation & DevOps Foundations (The Setup)
1.  [ ] **Repo Init**: Initialize a new Git repository with a semantic versioning naming strategy.
2.  [ ] **Branching Strategy**: Create a `DEVELOPMENT.md` defining the Git Flow (main, develop, feature/*).
3.  [ ] **Monorepo Structure**: Set up the folder structure: `backend/` and `frontend/` roots.
4.  [ ] **Pre-commit Hooks**: Install `pre-commit` (Python) and `eslint/prettier` for frontend.
5.  [ ] **Taskfile/Makefile**: Create a `Makefile` to automate commands like `make run-dev` or `make test`.
6.  [ ] **Docker Backend**: Create a `Dockerfile` for Python FastAPI (slim-buster image).
7.  [ ] **Docker Frontend**: Create a `Dockerfile` for React SPA (multi-stage build with Nginx).
8.  [ ] **Docker Compose**: Create `docker-compose.yml` to spin up Frontend + Backend + Database.
9.  [ ] **Environment Config**: Create `.env.example` templates for both services; add `.env` to `.gitignore`.
10. [ ] **CI Pipeline V1**: Write a GitHub Action to simply lint code on Pull Requests.

## Phase 2: Database Modeling & Data Layer (The Foundation)
11. [ ] **ERD Diagram**: Draw the Entity Relationship Diagram (Users, Products, Orders, Quotes).
12. [ ] **PostgreSQL Setup**: Configure the Postgres service in `docker-compose` with persistent volumes.
13. [ ] **ORM Selection**: Install `SQLModel` and `alembic` for migrations.
14. [ ] **User Model**: Define the `User` schema (email, hashed_password, is_active, is_superuser).
15. [ ] **Product Model**: Define `Product` schema (name, description, price, stock, category_id).
16. [ ] **Category Model**: Define `Category` schema (for uniform types like 'Security', 'Medical').
17. [ ] **Order Models**: Define `Order` and `OrderItem` schemas with foreign keys.
18. [ ] **Migration Init**: Run `alembic init` and configure `env.py` to read models.
19. [ ] **First Migration**: Generate and apply the initial migration to create tables.
20. [ ] **Seeding Script**: Write a Python script to populate the DB with initial "Senteng" categories.

## Phase 3: Backend Core & Authentication (The Security)
21. [ ] **FastAPI Setup**: Initialize the `FastAPI` app with CORS middleware (allow frontend URL).
22. [ ] **Folder Structure**: Create `api/v1/endpoints`, `core/security`, `crud/`, `schemas/`.
23. [ ] **Pydantic Schemas**: Define Request/Response schemas for User creation (DTOs).
24. [ ] **Password Hashing**: Implement `Passlib` with bcrypt for password hashing.
25. [ ] **JWT Utils**: Create functions to generate access and refresh tokens.
26. [ ] **Login Endpoint**: Implement `/auth/login` returning a JWT.
27. [ ] **Registration Endpoint**: Implement `/auth/register` with email validation.
28. [ ] **Dependency Injection**: Create `get_current_user` dependency for protected routes.
29. [ ] **Superuser Check**: Create `get_current_superuser` dependency for admin routes.
30. [ ] **Profile Endpoint**: Implement `/users/me` to fetch current user data.

## Phase 4: Backend Business Logic (The Features)
31. [ ] **Product CRUD**: Implement Create, Read, Update, Delete modules for Products.
32. [ ] **Image Handling**: Integrate `UploadFile` to handle product image uploads.
33. [ ] **Cloud Storage**: Set up AWS S3 (or MinIO locally) to store uploaded images; save URL to DB.
34. [ ] **Public Products API**: Implement `GET /products` with pagination and filtering.
35. [ ] **Category API**: Implement endpoints to list and manage categories.
36. [ ] **Quote Schema**: Define a `QuoteRequest` model (company name, bulk details, logo upload).
37. [ ] **Quote Endpoint**: Create `POST /quotes` for users to submit requests.
38. [ ] **Email Integration**: Configure `FastAPI-Mail` or SendGrid.
39. [ ] **Email Trigger**: Send an automated email to admin when a new Quote is received.
40. [ ] **Swagger Customization**: Add descriptions and auth buttons to the automatic API docs.

## Phase 5: Frontend Architecture (The Structure)
41. [ ] **React Init**: Initialize a standard React project (using a clean template).
42. [ ] **MUI Installation**: Install `@mui/material`, `@emotion/react`, `@emotion/styled`.
43. [ ] **Font Setup**: Import "Abril Fatface" and "Inter" from Google Fonts in your main entry file.
44. [ ] **MUI Theme Config**: Create `theme.js` defining Senteng brand colors and typography.
45. [ ] **Project Structure**: Set up `src/components`, `src/pages`, `src/services`, `src/context`.
46. [ ] **State Management**: Install `Zustand` and create a `useAuthStore` specific to user session.
47. [ ] **Router Setup**: Install `react-router-dom` and define the main route structure in `App.js`.
48. [ ] **Protect Routes**: Create a private route wrapper to protect `/admin` components.
49. [ ] **Global CSS**: Create `App.css` for custom MUI overrides and base styles.
50. [ ] **Icon Library**: Install `@mui/icons-material` for official Google Material icons.

## Phase 6: Frontend Components (The Lego Bricks)
51. [ ] **Navbar Component**: Build a responsive MUI AppBar with a mobile drawer.
52. [ ] **Footer Component**: Build the detailed footer using MUI `Box` and `Typography`.
53. [ ] **Hero Component**: Create a dynamic Hero section using MUI `Box` with standard gradients.
54. [ ] **Product Card**: Design a reusable MUI `Card` for displaying uniforms/products.
55. [ ] **MUI Customization**: Customize MUI Buttons for "Senteng Green" and "Red" accents.
56. [ ] **Input Fields**: Create styled MUI `TextField` variants with validation support.
57. [ ] **Loader/Backdrop**: Create a loading state using MUI `CircularProgress`.
58. [ ] **Modal/Dialog**: Implement an MUI `Dialog` for product quick views.
59. [ ] **Snackbar Notifications**: Set up MUI `Snackbar` and `Alert` for success/error messages.
60. [ ] **Breadcrumbs**: Implement MUI `Breadcrumbs` for deep site navigation.

## Phase 7: Frontend Pages - Customer Facing (The Experience)
61. [ ] **Landing Page**: Assemble the Home page using the new MUI components.
62. [ ] **About Page**: Port the "Who We Are" and "Mission" content to an MUI-based layout.
63. [ ] **Shop Page**: Create a grid layout using MUI `Grid` fetching data from the backend.
64. [ ] **Product Detail Page**: Create dynamic route `/shop/:id` to show single product details.
65. [ ] **Contact Page**: Create a form hooking into a backend email endpoint.
66. [ ] **Quote Builder UI**: Build a multi-step form using MUI `Stepper`.
67. [ ] **Login Page**: Create a login form with MUI `Paper` for a card-like feel.
68. [ ] **Register Page**: Create a registration form with validation (React Hook Form).
69. [ ] **404 Page**: Design a custom MUI-styled "Not Found" page.
70. [ ] **Profile Page**: User dashboard to view their past quote requests using MUI `List`.

## Phase 8: Admin Dashboard (The Control Center)
71. [ ] **Admin Layout**: Create a sidebar navigation layout (Mini-variant drawer).
72. [ ] **Dashboard Home**: Show stats using MUI `Card` and basic charts (SimpleBar or similar).
73. [ ] **Product Table**: Implement MUI `DataGrid` for powerful sorting/filtering of products.
74. [ ] **Add Product Form**: Create a form to upload image and create product (MUI components).
75. [ ] **Edit Product Flow**: Implement logic to pre-fill MUI forms and update products.
76. [ ] **Quote Management**: View list of received quotes in a scrollable MUI `Table`.
77. [ ] **Quote Status**: Add MUI `Chips` to mark quotes as "Pending", "Responded", "Closed".
78. [ ] **User Management**: View list of registered users in the admin panel.
79. [ ] **Settings Page**: (Optional) Update admin profile or password.
80. [ ] **Logout Flow**: Ensure secure cleanup of tokens and redirect to login.

## Phase 9: Advanced Features & Refinement (The 'Steroids')
81. [ ] **Search Bar**: Implement real-time search filtering using MUI `Autocomplete` or standard Input.
82. [ ] **Pagination**: Implement MUI `Pagination` for the Shop and Admin tables.
83. [ ] **SEO Meta Data**: Use `react-helmet-async` to manage document head and SEO tags.
84. [ ] **Sitemap Generator**: Create a script to generate `sitemap.xml` for public pages.
85. [ ] **Robots.txt**: Add robots configuration to the public folder.
86. [ ] **Image Optimization**: Implement lazy loading and responsive sizes for all images.
87. [ ] **Transitions**: Add MUI `Collapse`, `Fade`, or `Grow` transitions for UI updates.
88. [ ] **Skeleton Loaders**: Replace loading circles with MUI `Skeleton` placeholders.
89. [ ] **Form Validation**: Ensure strict validation on every form using `yup` or `zod`.
90. [ ] **Error Boundaries**: Wrap components in Error Boundaries to catch JS errors gracefully.

## Phase 10: Testing (The Quality Assurance)
91. [ ] **Pytest Config**: Configure `pytest` and `pytest-asyncio` for backend.
92. [ ] **Unit Test Models**: Write tests for Pydantic models and validation logic.
93. [ ] **Integration Tests**: Write tests for API endpoints using a test DB.
94. [ ] **Jest Setup**: Setup Jest and React Testing Library for the frontend.
95. [ ] **Component Tests**: Write tests for critical components (MUI Buttons, Navbar).
96. [ ] **E2E Testing Setup**: Install Playwright or Cypress for browser testing.
97. [ ] **Critical Flow Test**: Write an E2E test for the "Request a Quote" flow.
98. [ ] **Admin Flow Test**: Write an E2E test for "Admin logs in and adds product".
99. [ ] **Accessibility Audit**: Run Lighthouse/Wave to check for MUI accessibility.
100. [ ] **Performance Audit**: Run Lighthouse to check Core Web Vitals (FCP, LCP).

## Phase 11: Deployment & DevOps (The Release)
101. [ ] **Production Dockerfile**: Optimize Dockerfiles for production (Nginx for frontend assets).
102. [ ] **Nginx Reverse Proxy**: Setup Nginx to serve static files and proxy API requests.
103. [ ] **Domain Setup**: DNS configuration (A records/CNAME) for the domain.
104. [ ] **SSL Certificates**: Setup Let's Encrypt / Certbot for HTTPS.
105. [ ] **CI/CD Build Job**: Configure GitHub Actions to build Docker images on push.
106. [ ] **CI/CD Test Job**: Configure GitHub Actions to run Pytest/Jest on pull request.
107. [ ] **CD Deploy Job**: Configure SSH deployment or Cloud Platform deployment.
108. [ ] **Database Backup Strategy**: script to dump Postgres data periodically.
109. [ ] **Log Management**: Basic logging setup (Sentry or simple logger).
110. [ ] **Environment Variables**: Securely set production ENV variables on the server.

## Phase 12: Documentation & Portfolio Polish (The Presentation)
111. [ ] **README Main**: Write a world-class README with "How to Run", "Tech Stack", and "Screenshots".
112. [ ] **README Backend**: Detailed API doc link and setup guide in `backend/README.md`.
113. [ ] **README Frontend**: Detailed script guide in `frontend/README.md`.
114. [ ] **Architecture Diagram**: Embed the mermaid architecture diagram in the main README.
115. [ ] **Demo Video**: Record a 1-minute walk-through of the MUI-powered platform.
116. [ ] **Portfolio Link**: Add links to your GitHub/LinkedIn on the site footer.
117. [ ] **License**: Add MIT License.
118. [ ] **Code Cleanup**: Remove all console.logs and debugging comments.
119. [ ] **Final Manual QA**: Click every button, test every edge case manually.
120. [ ] **Launch**: Make the repository public and share your achievement!

---
**Completion Status: 0/120**
*Mark tasks with `[x]` as you complete them.*
