# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa đúng mã đơn hàng bị sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

# Hiển thị kết quả đúng nghiệp vụ
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)

# Trạng thái list sau khi chèn GE100-FAST: Chèn vào đầu (index 0). List trở thành ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]
# Lỗi dòng sửa mã: Do chèn phần tử vào đầu, toàn bộ list bị đẩy lùi 1 vị trí. Index 1 lúc này là "GE101", không phải "GE102-WRONG"
# Vị trí mới của GE102-WRONG: Đang nằm ở index 2
# Lỗi dòng pop(3): Trừ đi phần tử "GE101" vừa bị ghi đè sai ở bước trước, index 3 lúc này tương ứng với "GE104". Lệnh này xóa nhầm "GE104" thay vì đơn bị hủy
# Cách dùng remove(): express_orders.remove("GE103-CANCEL")
# Tác dụng của pop() không truyền tham số: Mặc định lấy và xóa phần tử cuối cùng của danh sách
# Lỗi dòng lấy đơn đang giao: Dùng pop() không truyền index nên lấy nhầm đơn cuối cùng ("GE104"), thay vì đơn đầu tiên
# Cách lấy đơn đầu tiên: Sử dụng express_orders.pop(0)