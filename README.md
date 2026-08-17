# Saraswoti Auto Workshop — Website

A simple, modern, fully responsive one-page website for Saraswoti Auto Workshop
(Narayangarh, Chitwan, Nepal), built with Django + SQLite on the backend and
plain HTML/CSS/JavaScript on the frontend.

## Tech Stack
- Django 6 (Python)
- SQLite (default database — stores contact-form messages)
- HTML5 / CSS3 (no frameworks, no build step)
- Vanilla JavaScript (mobile menu, active-link highlighting)

## Project Structure
```
saraswoti_project/
├── manage.py
├── config/                  # Django project settings
│   ├── settings.py
│   └── urls.py
└── workshop/                 # Main app
    ├── models.py             # ContactMessage model
    ├── views.py               # Renders the page + saves contact form
    ├── urls.py
    ├── admin.py                # View contact messages in /admin/
    ├── templates/workshop/index.html
    └── static/workshop/
        ├── css/style.css
        ├── js/script.js
        └── images/logo.png    # <-- REPLACE with the real workshop logo
```

## Getting Started

1. **Install dependencies** (only Django is required):
   ```bash
   pip install django
   ```

2. **Run migrations** (creates db.sqlite3):
   ```bash
   python manage.py migrate
   ```

3. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

4. Open **http://127.0.0.1:8000/** in your browser.

## Replacing the Logo
Swap the placeholder file at:
```
workshop/static/workshop/images/logo.png
```
with your real logo (same filename, ideally a square image, transparent PNG works best).
It's used in the header, hero section, and footer.

## Adding Real Team Photos
The "Our Mechanics" section (`#team` in `index.html`) currently uses icon
placeholders (`.team-photo` divs with an emoji inside). To use real photos:

1. Add your photo files to `workshop/static/workshop/images/` (e.g. `mechanic1.jpg`).
2. In `index.html`, replace a `.team-photo` div like this:
   ```html
   <div class="team-photo">🧑‍🔧</div>
   ```
   with an actual image:
   ```html
   <img src="{% static 'workshop/images/mechanic1.jpg' %}" alt="Senior Mechanic" class="team-photo">
   ```
3. Update the name/role text below it, and repeat for each team member.

## Updating Customer Reviews
The "Customer Reviews" section (`#reviews` in `index.html`) currently shows
**sample placeholder reviews** — replace the text inside each `.review-card`
with real customer feedback and names whenever you have them.

## Updating the Google Map
In `workshop/templates/workshop/index.html`, find the `<iframe>` inside the
Contact section (`class="map-wrap"`) and replace its `src` with your exact
Google Maps embed link (Google Maps → Share → Embed a map → copy the `src` URL).

## Contact Form
Messages submitted through the "Send us a quick message" form are saved to
the SQLite database (`ContactMessage` model). To view them:

1. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
2. Visit **http://127.0.0.1:8000/admin/** and log in.

## Deployment Notes
- Set `DEBUG = False` and a proper `SECRET_KEY` / `ALLOWED_HOSTS` in
  `config/settings.py` before deploying to production.
- Run `python manage.py collectstatic` to gather static files for production serving.
