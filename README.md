# ComunidadConnect (Final_Case)

Quick start:
1. Build: docker build -t comunidadconnect:latest .
2. Run: docker run --rm -p 8080:8080 --env-file .env.example comunidadconnect:latest
3. Health: curl http://localhost:8080/health
