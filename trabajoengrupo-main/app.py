from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mayte - Proyecto DevOps</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }

            .container {
                max-width: 1000px;
                width: 100%;
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            }

            .header {
                text-align: center;
                margin-bottom: 40px;
            }

            .header h1 {
                font-size: 3em;
                color: #667eea;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            }

            .header p {
                font-size: 1.3em;
                color: #666;
            }

            .emoji-large {
                font-size: 4em;
                margin: 20px 0;
                animation: bounce 2s infinite;
            }

            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-20px); }
            }

            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }

            .feature-card {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                cursor: pointer;
            }

            .feature-card:hover {
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
            }

            .feature-card .emoji {
                font-size: 3em;
                display: block;
                margin-bottom: 15px;
            }

            .feature-card h3 {
                font-size: 1.3em;
                margin-bottom: 10px;
            }

            .feature-card p {
                opacity: 0.9;
            }

            .info-section {
                background: #f8f9fa;
                padding: 30px;
                border-radius: 15px;
                margin: 30px 0;
                border-left: 5px solid #667eea;
            }

            .info-section h2 {
                color: #667eea;
                margin-bottom: 20px;
                font-size: 1.8em;
            }

            .info-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 20px;
            }

            .info-item {
                background: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }

            .info-item strong {
                color: #764ba2;
                display: block;
                margin-bottom: 5px;
            }

            .status-badge {
                background: #28a745;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                display: inline-block;
            }

            .tech-stack {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin: 20px 0;
                justify-content: center;
            }

            .tech-badge {
                background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                transition: all 0.3s ease;
            }

            .tech-badge:hover {
                transform: scale(1.1);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }

            footer {
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #e0e0e0;
                color: #666;
                font-size: 1.1em;
            }

            footer .heart {
                color: #e74c3c;
                animation: heartbeat 1.5s infinite;
            }

            @keyframes heartbeat {
                0%, 100% { transform: scale(1); }
                25% { transform: scale(1.1); }
                50% { transform: scale(1); }
            }

            @media (max-width: 768px) {
                .header h1 {
                    font-size: 2em;
                }
                
                .features {
                    grid-template-columns: 1fr;
                }
                
                .container {
                    padding: 20px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="emoji-large">🚀</div>
                <h1>¡Hola! Soy Mayte</h1>
                <p>Aplicación Flask desplegada con CI/CD</p>
            </div>

            <div class="features">
                <div class="feature-card">
                    <span class="emoji">🐳</span>
                    <h3>Docker</h3>
                    <p>Contenedorizada</p>
                </div>
                <div class="feature-card">
                    <span class="emoji">⚙️</span>
                    <h3>GitHub Actions</h3>
                    <p>CI/CD Automatizado</p>
                </div>
                <div class="feature-card">
                    <span class="emoji">🔄</span>
                    <h3>Docker Swarm</h3>
                    <p>Orquestación</p>
                </div>
                <div class="feature-card">
                    <span class="emoji">🌐</span>
                    <h3>Traefik</h3>
                    <p>Proxy Inverso</p>
                </div>
            </div>

            <div class="info-section">
                <h2>📊 Información del Proyecto</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Estudiante:</strong>
                        Mayte
                    </div>
                    <div class="info-item">
                        <strong>Curso:</strong>
                        DevOps 5-VE-B-SD4-515
                    </div>
                    <div class="info-item">
                        <strong>Tarea:</strong>
                        9.0 - CI/CD con AWS
                    </div>
                    <div class="info-item">
                        <strong>Estado:</strong>
                        <span class="status-badge">✅ Activo</span>
                    </div>
                </div>
            </div>

            <div class="info-section">
                <h2>🛠️ Stack Tecnológico</h2>
                <div class="tech-stack">
                    <span class="tech-badge">🐍 Python</span>
                    <span class="tech-badge">🌶️ Flask</span>
                    <span class="tech-badge">🐳 Docker</span>
                    <span class="tech-badge">⚙️ GitHub Actions</span>
                    <span class="tech-badge">📦 GHCR</span>
                    <span class="tech-badge">🌐 Traefik</span>
                    <span class="tech-badge">☁️ VPS Contabo</span>
                </div>
            </div>

            <footer>
                <p>Hecho con <span class="heart">💜</span> por Mayte</p>
                <p>Curso DevOps 2025 | Equipo: Villaruel, Villagomez</p>
            </footer>
        </div>
    </body>
    </html>
    '''

@app.route("/about")
def about():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Acerca de - Mayte</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            }
            h1 {
                color: #667eea;
                text-align: center;
                margin-bottom: 30px;
            }
            .back-btn {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                margin-bottom: 20px;
            }
            .back-btn:hover {
                background: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← Volver</a>
            <h1>📚 Acerca del Proyecto</h1>
            <p>Pipeline de CI/CD implementado para el curso de DevOps.</p>
            <h3>🎯 Flujo de Despliegue:</h3>
            <ol>
                <li>Push de código a GitHub</li>
                <li>GitHub Actions construye imagen Docker</li>
                <li>Imagen se sube a GHCR</li>
                <li>Despliegue automático al servidor</li>
                <li>Traefik enruta el tráfico HTTPS</li>
            </ol>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)