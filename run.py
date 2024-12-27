from app import create_app

# Use the correct path to the configuration class
app = create_app(config_class='app.config.DevelopmentConfig')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)