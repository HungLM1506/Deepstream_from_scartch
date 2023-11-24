# file is_aarch_64 sử dụng để làm gì

- Kiểm tra xem hệ thống đang chạy có phải là kiến trúc aarch64 (64-bit ARM) hay không

- platform.uname()[4] == 'aarch64': Sử dụng platform.uname() để lấy thông tin về hệ thống, trong đó [4] là chỉ số của kiến trúc CPU. Nếu kiến trúc là 'aarch64' (64-bit ARM), hàm trả về True; ngược lại, trả về False.
