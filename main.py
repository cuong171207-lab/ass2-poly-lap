import product_manager as pm

def main():
    # 1. Tải dữ liệu khi khởi động
    products = pm.load_data()
    print("Chào mừng đến với hệ thống quản lý POLYLAP!")

    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm theo tên")
        print("6. Lưu dữ liệu")
        print("0. Thoát chương trình")
        print("======================================")
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '3':
            products = pm.update_product(products)
        elif choice == '4':
            products = pm.delete_product(products)
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '6':
            pm.save_data(products)
        elif choice == '0':
            # Lưu dữ liệu trước khi thoát
            pm.save_data(products)
            print("Đã thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")
"""
Main menu chương trình POLYLAP
"""
