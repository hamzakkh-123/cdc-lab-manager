import os
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    # Local development: auto-seed if DB is empty
    db_path = os.path.join(app.instance_path, 'cdc_lab_manager.db')
    if not os.path.exists(db_path):
        print("Database not found. Initializing and seeding demo data...")
        os.makedirs(app.instance_path, exist_ok=True)
        from seed import seed_data
        seed_data()

    print("Starting Flask dev server...")
    app.run(debug=True, host='0.0.0.0', port=5000)

