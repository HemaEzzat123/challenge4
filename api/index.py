from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import hashlib
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    flag = os.getenv("FLAG", "FLAG NOT FOUND")

    cookies = request.cookies
    uid = cookies.get("UID")

    headers = {}

    if uid is None:
        uid_val = hashlib.md5("100".encode()).hexdigest()
        headers["set-cookie"] = f"UID={uid_val}; Max-Age=172800; Path=/"
    else:
        if uid == hashlib.md5("0".encode()).hexdigest():
            headers["set-cookie"] = f"FLAG={flag}; Path=/"
        else:
            headers["set-cookie"] = "FLAG=AzCTF{y0u_c4nt_U53_m3}; Path=/"

    html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Halib Al-Khair</title>
        <style>
            :root {
                --primary-color: #1a5f7a;
                --secondary-color: #88c0d0;
                --accent-color: #2e3440;
                --text-color: #2e3440;
                --background-color: #eceff4;
            }
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--background-color);
            }
            a {
                text-decoration: none;
                color: inherit;
            }
            header {
                background-color: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                position: sticky;
                top: 0;
                z-index: 10;
            }
            nav {
                max-width: 1200px;
                margin: 0 auto;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo img {
                height: 50px;
            }
            nav ul {
                display: flex;
                list-style: none;
            }
            nav ul li {
                margin-left: 2rem;
            }
            nav ul li a {
                color: var(--text-color);
                font-weight: 500;
                transition: color 0.3s ease;
            }
            nav ul li a:hover {
                color: var(--primary-color);
            }
            .hero {
                text-align: center;
                padding: 4rem 1rem;
                background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)),
                border-radius: 10px;
                margin: 2rem auto;
                max-width: 1200px;
            }
            .hero h1 {
                font-size: 3rem;
                color: var(--primary-color);
                margin-bottom: 1rem;
            }
            .hero p {
                font-size: 1.2rem;
            }
            .featured-products {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem 1rem;
            }
            .featured-products h2 {
                text-align: center;
                font-size: 2rem;
                margin-bottom: 2rem;
                color: var(--primary-color);
            }
            .product-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
            }
            .product-card {
                background: white;
                border-radius: 10px;
                padding: 1rem;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .product-card:hover {
                transform: translateY(-5px);
            }
            .product-card img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 5px;
                margin-bottom: 1rem;
            }
            .product-card h3 {
                margin-bottom: 0.5rem;
                color: var(--accent-color);
            }
            .product-card p {
                font-size: 0.95rem;
                margin-bottom: 1rem;
            }
            .btn {
                display: inline-block;
                padding: 0.5rem 1rem;
                background-color: var(--primary-color);
                color: white;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .btn:hover {
                background-color: var(--secondary-color);
            }
            footer {
                text-align: center;
                padding: 2rem;
                background-color: var(--accent-color);
                color: white;
                margin-top: 3rem;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">
                    <!-- Add your logo here -->
                </div>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/products">Products</a></li>
                    <li><a href="/reports/generate">Reports</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>

        <main>
            <section class="hero">
                <h1>Welcome to Halib Al-Khair</h1>
                <p>Delivering the finest dairy products since 1985</p>
            </section>

            <h2>Hey You, yes you!<br>are you looking for a flag, well it's not here bruh!<br>Try someplace else<h2>

            <section class="featured-products">
                <h2>Our Premium Products</h2>
                <div class="product-grid">
                    <div class="product-card">
                        <h3>Fresh Milk</h3>
                        <p>Farm-fresh whole milk</p>
                        <a href="/products?id=1" class="btn">Learn More</a>
                    </div>
                    <div class="product-card">
                        <h3>Natural Yogurt</h3>
                        <p>Creamy and healthy</p>
                        <a href="/products?id=2" class="btn">Learn More</a>
                    </div>
                    <!-- Add more products as needed -->
                </div>
            </section>
        </main>

        <footer>
            <p>&copy; 2024 Halib Al-Khair. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

    return HTMLResponse(content=html, headers=headers)
