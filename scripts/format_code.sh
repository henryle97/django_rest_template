find app_name -name "*.py" -not -path "app_name/apps/engine/migrations/*" \
    -not -path "app_name/apps/cron/migrations/*" | xargs python -m isort


find app_name -name "*.py" -not -path "app_name/apps/engine/migrations/*" \
    -not -path "app_name/apps/cron/migrations/*" | xargs python -m black -l 79

