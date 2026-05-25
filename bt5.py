raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 " 

while True:
    decision = int(input("===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====\n"
                         "1. Hiển thị chuỗi mã vạch gốc\n"
                         "2. Giải mã, làm sạch và in báo cáo kiểm kê\n"
                         "3. Tra cứu nhanh theo đuôi Serial\n"
                         "4. Thoát chương trình\n"
                         "Nhập lựa chọn của bạn (1-4):"
                         ))
    match decision:
        case 1:
            print(raw_batch)
        case 2:
            pass_prod = 0
            print("MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
            seperate_data = raw_batch.split(";")
            for i in range (len(seperate_data)):
                core_data = seperate_data[i].split("-")
                prod_id = core_data[0].strip().upper()
                nati_id = core_data[1].strip().upper()
                cre_year = core_data[2].strip()
                seri_num = core_data[3].strip()
                if seri_num.isalpha():
                    print(f"{prod_id} | {nati_id} | {cre_year} | {seri_num} | Reject")
                else:
                    print(f"{prod_id} | {nati_id} | {cre_year} | {seri_num} | Pass")
                    pass_prod+=1
            print(f"Đã giải mã thành công {pass_prod} sản phẩm hợp lệ / Tổng số {len(seperate_data)} sản phẩm.")
        case 3:
            found = False
            search_id = input("Nhập vào số serial của sản phẩm bạn muốn tìm kiếm: ").strip()
            seperate_data = raw_batch.split(";")
            for i in range (len(seperate_data)):
                core_data = seperate_data[i].split("-")
                prod_id = core_data[0].strip().upper()
                nati_id = core_data[1].strip().upper()
                cre_year = core_data[2].strip()
                seri_num = core_data[3].strip()
                if search_id == seri_num:
                    if seri_num.isalpha():
                        print("MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
                        print(f"{prod_id} | {nati_id} | {cre_year} | {seri_num} | Reject")
                        found = True
                        break
                    else:
                        print("MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
                        print(f"{prod_id} | {nati_id} | {cre_year} | {seri_num} | Pass")
                        found = True
                        break
            if not found:
                print("Không tìm thấy sản phẩm phù hợp")
        case 4:
            print("Đóng ca kiểm kho. Chào tạo biệt!")
            break
        case _:
            print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
'''
    Cách giải quyết các vấn đề được đưa ra:
    Sau khi đã tách dữ liệu thành các dữ liệu con từ chuỗi đưa ra bằng lệnh split
        Serial sai định dạng
            Tại biến lưu trữ giá trị của mã seri, sử dụng isalpha để kiểm tra liệu có phải chữ cái không? Nếu đúng thì báo trạng thái reject
        Nhập dư khoảng trắng khi tra cứu
            Tại biến lưu trữ giá trị tìm kiếm, dùng strip để xóa bỏ khoảng trống 2 bên của phần nhập liệu
         Nhập sai lựa chọn menu
            Trong match-case, torng trường hợp case _: đặt thông báo cho biết người dùng đã nhập sai và chức năng không tồn tại         
'''
'''
    Với chức năng tìm kiếm, sử dụng trực tiếp luôn strip và upper cho biến tìm kiếm để tránh trường hợp người dùng nhập nhầm hoặc sai định dạng
'''