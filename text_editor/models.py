import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        content TEXT
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def create_document(title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO documents (title, content) VALUES (%s, %s)', (title, content))
    conn.commit()
    cursor.close()
    conn.close()

def get_documents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title FROM documents')
    documents = cursor.fetchall()
    cursor.close()
    conn.close()
    return documents

def get_document_by_id(doc_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM documents WHERE id = %s', (doc_id,))
    document = cursor.fetchone()
    cursor.close()
    conn.close()
    return document

def update_document(doc_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE documents SET title = %s, content = %s WHERE id = %s', (title, content, doc_id))
    conn.commit()
    cursor.close()
    conn.close()
