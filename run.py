from app import create_app
from app.seed import seed_data

app = create_app()

@app.cli.command("seed")
def seed():
    seed_data()
    print("Database seeded successfully!")

if __name__ == '__main__':
    app.run(debug=True)
