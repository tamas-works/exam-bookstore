bookstore-exam/
├── bookstore/                      # Projekt konfiguráció mappa
│   ├── __init__.py
│   ├── asgi.py                     # ASGI konfig (async)
│   ├── settings.py                 # Globális beállítások (DB, apps, stb.)
│   ├── urls.py                     # Root URL routing
│   └── wsgi.py                     # WSGI konfig (deployment)
│
├── library/                        # Alkalmazás (app)
│   ├── migrations/                 # Adatbázis migrációk (auto-generált)
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                    # Admin panel konfiguráció
│   ├── apps.py                     # App konfiguráció
│   ├── models.py                   # Modellek (Category, Product)
│   ├── serializers.py              # DRF serializers (JSON <-> Model)
│   ├── views.py                    # ViewSets (API logika)
│   ├── urls.py                     # App-specifikus URL routing
│   └── tests.py                    # Unit tesztek
│
├── requirements.txt                # Python függőségek listája
└── README.md  
