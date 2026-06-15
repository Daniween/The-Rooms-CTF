from flask import Flask, request, Response
import sqlite3

app = Flask(__name__)
DB_PATH = '/var/db/ctf.db'


def query_db(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return rows, None
    except Exception as e:
        conn.close()
        return None, str(e)


@app.route('/')
def index():
    html = """<!DOCTYPE html>
<html>
<head><title>EvilCorp - Portail RH Interne</title></head>
<body style="font-family:monospace;padding:20px">
<h1>EvilCorp &mdash; Portail RH Interne</h1>
<p>Recherchez un employe par son identifiant numerique :</p>
<form method="GET" action="/search">
    <input type="text" name="id" placeholder="ID employe (ex: 1)" size="30">
    <input type="submit" value="Rechercher">
</form>
</body>
</html>"""
    return Response(html, content_type='text/html; charset=utf-8')


@app.route('/search')
def search():
    emp_id = request.args.get('id', '').strip()
    if not emp_id:
        return Response(
            '<html><body><p>Parametre manquant : <code>id</code></p></body></html>',
            content_type='text/html; charset=utf-8',
            status=400
        )

    # Vulnerable to SQL injection — intentional for CTF purposes
    sql = f"SELECT id, name, department FROM employees WHERE id = {emp_id}"
    rows, error = query_db(sql)

    if error:
        return Response(
            f'<html><body><p>Erreur SQL : <code>{error}</code></p></body></html>',
            content_type='text/html; charset=utf-8',
            status=500
        )

    rows_html = ''.join(
        f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>'
        for r in rows
    ) or '<tr><td colspan="3">Aucun resultat</td></tr>'

    html = f"""<!DOCTYPE html>
<html>
<body style="font-family:monospace;padding:20px">
<h2>Resultats de la recherche :</h2>
<table border="1" cellpadding="5">
<tr><th>ID</th><th>Nom</th><th>Departement</th></tr>
{rows_html}
</table>
</body>
</html>"""
    return Response(html, content_type='text/html; charset=utf-8')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
