# 📚 Fahasa Bookstore — Microservice System

Hệ thống quản lý nhà sách trực tuyến được xây dựng theo kiến trúc **Microservices** sử dụng **Django REST Framework** và **Docker Compose**.

---

## 📋 Mục lục

- [Tổng quan kiến trúc](#tổng-quan-kiến-trúc)
- [Danh sách services](#danh-sách-services)
- [Cấu trúc thư mục](#cấu-trúc-thư-mục)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt và chạy dự án](#cài-đặt-và-chạy-dự-án)
- [API Endpoints](#api-endpoints)
- [Giao diện Web](#giao-diện-web)
- [Phát triển cục bộ](#phát-triển-cục-bộ)

---

## 🏗️ Tổng quan kiến trúc

```
                        ┌─────────────────────────────┐
                        │        Người dùng           │
                        │    http://localhost:8010     │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │         API Gateway         │
                        │      (port 8010)             │
                        │   Django Templates + Proxy  │
                        └──┬──┬──┬──┬──┬──┬──┬──┬───┘
                           │  │  │  │  │  │  │  │
           ┌───────────────┘  │  │  │  │  │  │  └──────────────┐
           │         ┌────────┘  │  │  │  │  └────────f──┐      │
           │         │      ┌────┘  │  │  └──────┐      │      │
           ▼         ▼      ▼       ▼  ▼         ▼      ▼      ▼
        book      customer cart   order ship    pay  comment recommender
       :8012      :8011   :8013  :8017 :8018  :8019  :8020    :8021

       staff     manager  catalog
       :8014     :8015    :8016
```

**Nguyên tắc:**
- Mỗi service là một ứng dụng Django độc lập với database riêng (SQLite)
- API Gateway là điểm vào duy nhất cho người dùng, proxy request đến các service
- Các service giao tiếp nội bộ qua HTTP sử dụng Docker service name

---

## 📦 Danh sách services

| Service | Port | Mô tả | Model chính |
|---|---|---|---|
| **api-gateway** | 8010 | Giao diện web + proxy đến tất cả services | — |
| **customer-service** | 8011 | Quản lý khách hàng | `Customer` |
| **book-service** | 8012 | Quản lý sách | `Book` |
| **cart-service** | 8013 | Giỏ hàng | `Cart`, `CartItem` |
| **staff-service** | 8014 | Quản lý nhân viên | `Staff` |
| **manager-service** | 8015 | Quản lý cấp quản lý | `Manager` |
| **catalog-service** | 8016 | Danh mục sách | `Category`, `BookCatalog` |
| **order-service** | 8017 | Đơn hàng | `Order`, `OrderItem` |
| **ship-service** | 8018 | Vận chuyển | `Shipment` |
| **pay-service** | 8019 | Thanh toán | `Payment` |
| **comment-rate-service** | 8020 | Bình luận & đánh giá | `Comment`, `Rating` |
| **recommender-ai-service** | 8021 | Gợi ý sách AI | `Recommendation` |

---

## 📁 Cấu trúc thư mục

```
bookstore-microservice/
├── docker-compose.yml
├── README.md
│
├── api-gateway/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── api_gateway/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   │   ├── base.html          ← Base template (Fahasa style)
│   │   ├── books.html
│   │   ├── cart.html
│   │   ├── customers.html
│   │   ├── orders.html
│   │   ├── shipments.html
│   │   ├── payments.html
│   │   ├── comments.html
│   │   ├── recommendations.html
│   │   ├── staff.html
│   │   └── managers.html
│   └── static/
│       └── css/
│           └── fahasa.css     ← Main stylesheet
│
├── book-service/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── app/                   ← Django app (models, views, serializers, urls)
│   └── book_service/          ← Django project (settings, urls, wsgi)
│
├── customer-service/          ← (cấu trúc tương tự book-service)
├── cart-service/
├── staff-service/
├── manager-service/
├── catalog-service/
├── order-service/
├── ship-service/
├── pay-service/
├── comment-rate-service/
└── recommender-ai-service/
```

---

## ⚙️ Yêu cầu hệ thống

| Công cụ | Phiên bản tối thiểu |
|---|---|
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | 4.x trở lên |
| [Docker Compose](https://docs.docker.com/compose/) | v2.x (tích hợp sẵn trong Docker Desktop) |
| RAM | Tối thiểu 4GB |
| Disk | Tối thiểu 3GB |

> **Lưu ý:** Python không cần cài trên máy host — tất cả chạy trong Docker container.

---

## 🚀 Cài đặt và chạy dự án

### Bước 1 — Cài Docker Desktop

Tải và cài đặt [Docker Desktop](https://www.docker.com/products/docker-desktop/), sau đó khởi động ứng dụng và đợi icon Docker dưới taskbar chuyển sang trạng thái **Running**.

### Bước 2 — Clone / mở thư mục dự án

```bash
cd bookstore-microservice
```

### Bước 3 — Build và chạy tất cả services

**Lần đầu tiên (build images):**
```bash
docker compose up --build
```

**Các lần sau (dùng images đã build):**
```bash
docker compose up -d
```

> Lần đầu build sẽ mất khoảng 3-5 phút tùy tốc độ internet.

### Bước 4 — Mở trình duyệt

```
http://localhost:8010
```

---

## 🛠️ Các lệnh Docker hữu ích

```bash
# Xem trạng thái tất cả containers
docker compose ps

# Xem logs của một service cụ thể
docker compose logs api-gateway
docker compose logs book-service

# Xem logs realtime
docker compose logs -f api-gateway

# Dừng tất cả containers (giữ nguyên data)
docker compose stop

# Dừng và xóa containers (giữ nguyên images)
docker compose down

# Rebuild một service cụ thể sau khi thay đổi code
docker compose up --build api-gateway

# Rebuild toàn bộ dự án
docker compose up --build

# Xóa toàn bộ (containers + volumes + images của project)
docker compose down --rmi local -v
```

---

## 🌐 API Endpoints

### Book Service (`http://localhost:8012`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/books/` | Danh sách tất cả sách |
| POST | `/books/` | Thêm sách mới |
| GET | `/books/<id>/` | Chi tiết sách |
| PUT | `/books/<id>/` | Cập nhật sách |
| DELETE | `/books/<id>/` | Xóa sách |

### Customer Service (`http://localhost:8011`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/customers/` | Danh sách khách hàng |
| POST | `/customers/` | Thêm khách hàng |
| GET | `/customers/<id>/` | Chi tiết khách hàng |
| PUT | `/customers/<id>/` | Cập nhật khách hàng |
| DELETE | `/customers/<id>/` | Xóa khách hàng |

### Cart Service (`http://localhost:8013`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/cart/<customer_id>/` | Giỏ hàng của khách |
| POST | `/cart/<customer_id>/add/` | Thêm sách vào giỏ |
| DELETE | `/cart/<customer_id>/clear/` | Xóa giỏ hàng |

### Order Service (`http://localhost:8017`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/orders/` | Tất cả đơn hàng |
| POST | `/orders/` | Tạo đơn hàng mới |
| GET | `/orders/<id>/` | Chi tiết đơn hàng |
| GET | `/orders/customer/<id>/` | Đơn hàng theo khách |

### Ship Service (`http://localhost:8018`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/shipments/` | Tất cả vận đơn |
| POST | `/shipments/` | Tạo vận đơn |
| GET | `/shipments/<id>/` | Chi tiết vận đơn |
| GET | `/shipments/order/<id>/` | Vận đơn theo đơn hàng |

### Pay Service (`http://localhost:8019`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/payments/` | Tất cả giao dịch |
| POST | `/payments/` | Tạo giao dịch |
| GET | `/payments/<id>/` | Chi tiết giao dịch |

### Comment & Rate Service (`http://localhost:8020`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/comments/` | Tất cả bình luận |
| POST | `/comments/` | Thêm bình luận |
| GET | `/comments/book/<id>/` | Bình luận theo sách |
| GET | `/ratings/` | Tất cả đánh giá |
| POST | `/ratings/` | Thêm đánh giá (1-5 ⭐) |
| GET | `/ratings/book/<id>/` | Đánh giá trung bình theo sách |

### Recommender AI Service (`http://localhost:8021`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/recommend/<customer_id>/` | Gợi ý sách cho khách |
| GET | `/top-books/` | Top sách được đánh giá cao nhất |

### Staff Service (`http://localhost:8014`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/staff/` | Danh sách nhân viên |
| POST | `/staff/` | Thêm nhân viên |
| GET | `/staff/<id>/` | Chi tiết nhân viên |

### Manager Service (`http://localhost:8015`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/managers/` | Danh sách quản lý |
| POST | `/managers/` | Thêm quản lý |
| GET | `/managers/<id>/` | Chi tiết quản lý |

### Catalog Service (`http://localhost:8016`)

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/categories/` | Danh mục sách |
| GET | `/catalog/` | Toàn bộ catalog |
| GET | `/categories/<id>/books/` | Sách theo danh mục |

---

## 🖥️ Giao diện Web

Truy cập qua **API Gateway** tại `http://localhost:8010`:

| URL | Trang |
|---|---|
| `/` | Trang chủ — danh sách sách |
| `/books/` | Quản lý sách |
| `/customers/` | Quản lý khách hàng |
| `/orders/` | Quản lý đơn hàng |
| `/shipments/` | Quản lý vận chuyển |
| `/payments/` | Quản lý thanh toán |
| `/staff/` | Quản lý nhân viên |
| `/managers/` | Quản lý cấp quản lý |
| `/books/<id>/comments/` | Đánh giá sách |
| `/cart/<customer_id>/` | Giỏ hàng khách |
| `/recommend/<customer_id>/` | Gợi ý sách cho khách |
| `/top-books/` | Sách được đánh giá cao nhất |

---

## 💻 Phát triển cục bộ

### Cài đặt môi trường Python (cho VS Code)

```bash
# Tạo virtual environment
python -m venv .venv

# Kích hoạt (Windows)
.venv\Scripts\activate

# Cài dependencies để VS Code nhận dạng (không cần để chạy Docker)
pip install django djangorestframework requests
```

Sau đó chọn interpreter `.venv` trong VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter**.

### Thay đổi code và rebuild

Sau khi sửa code một service, rebuild service đó:

```bash
# Rebuild và restart chỉ service bị thay đổi
docker compose up --build api-gateway

# Rebuild nhiều services
docker compose up --build book-service api-gateway
```

### Xem database của một service

```bash
# Truy cập shell của container
docker compose exec book-service python manage.py shell

# Chạy migrations thủ công (nếu cần)
docker compose exec book-service python manage.py migrate
```

---

## 🔧 Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| **Django 5.x** | Web framework cho mỗi microservice |
| **Django REST Framework** | Xây dựng REST API |
| **SQLite** | Database nhúng cho mỗi service |
| **Docker** | Container hóa từng service |
| **Docker Compose** | Orchestration multi-container |
| **Python 3.11** | Runtime |
| **requests** | HTTP client giao tiếp giữa services |

---

## 📊 Mô hình dữ liệu

```
Book ──────────────── CartItem ──── Cart ──── Customer
 │                                                │
 │                                             Order ──── OrderItem
 │                                                │
 ├── Comment (customer_id)                   Shipment
 ├── Rating  (customer_id, score 1-5)         Payment
 │
 └── (Recommender đọc Rating để tính gợi ý)
```

---

*Xây dựng bởi Django + Docker Compose — Phong cách giao diện Fahasa Bookstore*
