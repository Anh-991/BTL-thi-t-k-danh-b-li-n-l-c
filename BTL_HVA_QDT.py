import json

FILE_JSON = 'danhba.json'

def doc_danh_ba_tu_json():
    try:
        with open(FILE_JSON, 'r', encoding='utf-8') as f:
            danh_ba = json.load(f)
            if danh_ba == [{}]:
                return []
            return danh_ba
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def luu_danh_ba_vao_json(danh_ba):
    try:
        with open(FILE_JSON, 'w', encoding='utf-8') as f:
            json.dump(danh_ba, f, ensure_ascii=False, indent=4)
        print("Đã lưu danh bạ vào file JSON thành công.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def nhap_danh_ba():
    global danh_ba
    danh_ba = []
    so_luong = int(input("Nhập số lượng liên hệ: "))
    for i in range(so_luong):
        ten = input(f"Nhập tên liên hệ thứ {i+1}: ")
        sdt = input(f"Nhập số điện thoại của {ten}: ")
        danh_ba.append({'ten': ten, 'sdt': sdt})
    luu_danh_ba_vao_json(danh_ba)
    return danh_ba

def them_lien_he_moi():
    global danh_ba
    ten = input("Nhập tên liên hệ mới: ")
    sdt = input("Nhập số điện thoại: ")
    
    for lien_he in danh_ba:
        if lien_he['sdt'] == sdt:
            print(f"Số điện thoại {sdt} đã tồn tại trong danh bạ!")
            return
    
    danh_ba.append({'ten': ten, 'sdt': sdt})
    luu_danh_ba_vao_json(danh_ba)
    print("Đã thêm liên hệ mới thành công.")

def hien_thi_danh_ba(danh_ba):
    if not danh_ba:
        print("Danh bạ trống.")
        return
    print(f"\n===== DANH BẠ ĐIỆN THOẠI ({len(danh_ba)} liên hệ) =====")
    for i, lien_he in enumerate(danh_ba, start=1):
        print(f"{i}. Tên: {lien_he['ten']}, SĐT: {lien_he['sdt']}")

def kiem_tra_ton_tai_sdt(sdt):
    for lien_he in danh_ba:
        if lien_he['sdt'] == sdt:
            print(f"Số điện thoại {sdt} có trong danh bạ (Tên: {lien_he['ten']}).")
            return True
    print(f"Số điện thoại {sdt} không tồn tại trong danh bạ.")
    return False

def tim_kiem_theo_ten(ten):
    ket_qua = [lh for lh in danh_ba if ten.lower() in lh['ten'].lower()]
    if ket_qua:
        print(f"Tìm thấy {len(ket_qua)} liên hệ có tên chứa '{ten}':")
        for i, lh in enumerate(ket_qua, start=1):
            print(f"  {i}. Tên: {lh['ten']}, SĐT: {lh['sdt']}")
    else:
        print(f"Không tìm thấy liên hệ nào có tên chứa '{ten}'.")

def tim_kiem_theo_sdt(sdt):
    for lien_he in danh_ba:
        if lien_he['sdt'] == sdt:
            return lien_he
    return None

def sua_lien_he(thu_tu):
    if 1 <= thu_tu <= len(danh_ba):
        print(f"Thông tin hiện tại: Tên: {danh_ba[thu_tu-1]['ten']}, SĐT: {danh_ba[thu_tu-1]['sdt']}")
        ten_moi = input("Nhập tên mới (Enter để giữ nguyên): ").strip()
        sdt_moi = input("Nhập số điện thoại mới (Enter để giữ nguyên): ").strip()
        
        if ten_moi:
            danh_ba[thu_tu - 1]['ten'] = ten_moi
        if sdt_moi:
            for i, lien_he in enumerate(danh_ba):
                if i != thu_tu - 1 and lien_he['sdt'] == sdt_moi:
                    print(f"Số điện thoại {sdt_moi} đã tồn tại trong danh bạ!")
                    return
            danh_ba[thu_tu - 1]['sdt'] = sdt_moi
        
        luu_danh_ba_vao_json(danh_ba)
        print("Cập nhật thành công.")
    else:
        print("Thứ tự không hợp lệ.")

def xoa_lien_he(ten):
    global danh_ba
    for i, lh in enumerate(danh_ba):
        if lh['ten'].lower() == ten.lower():
            danh_ba.pop(i)
            luu_danh_ba_vao_json(danh_ba)
            print(f"Đã xóa liên hệ '{ten}' thành công.")
            return
    print(f"Không tìm thấy liên hệ tên '{ten}'.")

def xoa_lien_he_theo_sdt(sdt):
    global danh_ba
    for i, lh in enumerate(danh_ba):
        if lh['sdt'] == sdt:
            ten = lh['ten']
            danh_ba.pop(i)
            luu_danh_ba_vao_json(danh_ba)
            print(f"Đã xóa liên hệ '{ten}' (SĐT: {sdt}) thành công.")
            return
    print(f"Không tìm thấy liên hệ có số điện thoại '{sdt}'.")

def dem_lien_he_khong_trung_ten():
    ten_khac_nhau = {lh['ten'].lower() for lh in danh_ba}
    print(f"Số lượng tên khác nhau trong danh bạ: {len(ten_khac_nhau)}")

def sap_xep_danh_ba():
    global danh_ba
    danh_ba.sort(key=lambda x: x['ten'].lower())
    luu_danh_ba_vao_json(danh_ba)
    print("Đã sắp xếp danh bạ theo tên thành công.")

def thong_ke_danh_ba():
    if not danh_ba:
        print("Danh bạ trống.")
        return
    
    print(f"\n===== THỐNG KÊ DANH BẠ =====")
    print(f"Tổng số liên hệ: {len(danh_ba)}")
    
    ten_khac_nhau = {lh['ten'].lower() for lh in danh_ba}
    print(f"Số tên khác nhau: {len(ten_khac_nhau)}")
    
    do_dai_sdt = {}
    for lh in danh_ba:
        do_dai = len(lh['sdt'])
        do_dai_sdt[do_dai] = do_dai_sdt.get(do_dai, 0) + 1
    
    print("Phân bố độ dài số điện thoại:")
    for do_dai, so_luong in sorted(do_dai_sdt.items()):
        print(f"  {do_dai} chữ số: {so_luong} số")

if __name__ == "__main__":
    danh_ba = doc_danh_ba_tu_json()
    print(f"Đã tải {len(danh_ba)} liên hệ từ file JSON.")
    
    while True:
        print("\n" + "="*50)
        print("           MENU DANH BẠ ĐIỆN THOẠI")
        print("="*50)
        print("1.  Nhập danh bạ mới (thay thế toàn bộ)")
        print("2.  Thêm liên hệ mới")
        print("3.  Hiển thị danh bạ")
        print("4.  Kiểm tra số điện thoại có tồn tại")
        print("5.  Tìm kiếm liên hệ theo tên")
        print("6.  Tìm kiếm liên hệ theo số điện thoại")
        print("7.  Sửa thông tin liên hệ")
        print("8.  Xóa liên hệ theo tên")
        print("9.  Xóa liên hệ theo số điện thoại")
        print("10. Đếm số tên không trùng trong danh bạ")
        print("11. Sắp xếp danh bạ theo tên")
        print("12. Thống kê danh bạ")
        print("13. Lưu danh bạ vào JSON")
        print("14. Tải lại danh bạ từ JSON")
        print("15. Thoát")
        print("="*50)
        
        lua_chon = input("Nhập lựa chọn (1-15): ").strip()

        if lua_chon == "1":
            nhap_danh_ba()
        elif lua_chon == "2":
            them_lien_he_moi()
        elif lua_chon == "3":
            hien_thi_danh_ba(danh_ba)
        elif lua_chon == "4":
            sdt = input("Nhập số điện thoại cần kiểm tra: ").strip()
            kiem_tra_ton_tai_sdt(sdt)
        elif lua_chon == "5":
            ten = input("Nhập tên liên hệ cần tìm: ").strip()
            tim_kiem_theo_ten(ten)
        elif lua_chon == "6":
            sdt = input("Nhập số điện thoại cần tìm: ").strip()
            lien_he = tim_kiem_theo_sdt(sdt)
            if lien_he:
                print(f"Tìm thấy: Tên: {lien_he['ten']}, SĐT: {lien_he['sdt']}")
            else:
                print("Không tìm thấy liên hệ với số điện thoại này.")
        elif lua_chon == "7":
            try:
                thu_tu = int(input("Nhập thứ tự liên hệ cần sửa: "))
                sua_lien_he(thu_tu)
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
        elif lua_chon == "8":
            ten = input("Nhập tên liên hệ cần xóa: ").strip()
            xoa_lien_he(ten)
        elif lua_chon == "9":
            sdt = input("Nhập số điện thoại cần xóa: ").strip()
            xoa_lien_he_theo_sdt(sdt)
        elif lua_chon == "10":
            dem_lien_he_khong_trung_ten()
        elif lua_chon == "11":
            sap_xep_danh_ba()
        elif lua_chon == "12":
            thong_ke_danh_ba()
        elif lua_chon == "13":
            luu_danh_ba_vao_json(danh_ba)
        elif lua_chon == "14":
            danh_ba = doc_danh_ba_tu_json()
            print(f"Đã tải lại {len(danh_ba)} liên hệ từ file JSON.")
        elif lua_chon == "15":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")