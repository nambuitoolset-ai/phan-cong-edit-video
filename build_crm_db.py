import sqlite3
import json
import os

DB_PATH = 'brain.db'
WAITLIST_PATH = 'waitlist.json'

def init_crm():
    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} not found. Creating a new database.")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('physical', 'digital', 'service')),
        price INTEGER NOT NULL,
        description TEXT,
        stock INTEGER
    )
    ''')
    
    # 2. Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        zalo TEXT,
        created_at TEXT NOT NULL
    )
    ''')
    
    # 3. Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        customer_phone TEXT NOT NULL,
        product_id INTEGER,
        amount INTEGER NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('pending', 'success', 'failed')),
        created_at TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')
    
    conn.commit()
    print("✓ Created tables: products, customers, orders in SQLite database.")

    # 4. Insert default products
    default_products = [
        ("Máy Chiếu Mini ETOE Starfish 2", "physical", 3490000, "Máy chiếu mini sắc nét Full HD 1080P tích hợp Android TV bản quyền.", 50),
        ("Dịch Vụ KOC Booking - Video Review", "service", 5000000, "Video review dài 30s-60s đăng tải trên kênh TikTok @namoinam.", None),
        ("Ebook Bí Kíp Làm KOC Hái Ra Tiền", "digital", 199000, "Cẩm nang hướng dẫn từ số 0 để trở thành KOC chuyên nghiệp.", None)
    ]
    
    for name, p_type, price, desc, stock in default_products:
        cursor.execute("SELECT id FROM products WHERE name = ?", (name,))
        if not cursor.fetchone():
            cursor.execute('''
            INSERT INTO products (name, type, price, description, stock)
            VALUES (?, ?, ?, ?, ?)
            ''', (name, p_type, price, desc, stock))
            print(f"✓ Added product: {name}")
    
    conn.commit()

    # 5. Import customers from waitlist.json
    if os.path.exists(WAITLIST_PATH):
        try:
            with open(WAITLIST_PATH, 'r', encoding='utf-8') as f:
                waitlist_data = json.load(f)
            
            imported_count = 0
            for customer in waitlist_data:
                name = customer.get('name')
                phone = customer.get('phone')
                zalo = customer.get('zalo')
                created_at = customer.get('created_at')
                
                # Check for duplicates by phone number
                cursor.execute("SELECT id FROM customers WHERE phone = ?", (phone,))
                if not cursor.fetchone():
                    cursor.execute('''
                    INSERT INTO customers (name, phone, zalo, created_at)
                    VALUES (?, ?, ?, ?)
                    ''', (name, phone, zalo, created_at))
                    imported_count += 1
            
            conn.commit()
            print(f"✓ Imported {imported_count} customers from {WAITLIST_PATH} without duplication.")
        except Exception as e:
            print(f"Error importing waitlist.json: {e}")
    else:
        print(f"Warning: {WAITLIST_PATH} not found. Skipped customer import.")
        
    conn.close()

if __name__ == '__main__':
    init_crm()
