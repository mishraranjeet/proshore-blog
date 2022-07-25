echo Starting Gunicorn.
exec gunicorn proshore_scrap.wsgi:application \
    --bind 0.0.0.0:8000 \
    --timeout 300 \
    --workers 3