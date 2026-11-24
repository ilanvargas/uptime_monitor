from fastapi import FastAPI


def create_app():
    app = FastAPI()

    @app.get("/healthz")
    def health_check():
        return {"status": "ok"}

    return app
