## Một số thuộc tính quan trọng thường dùng trong file config

1. gpu-id = 0/1/2/3/...

   - Sử dụng gpu có số id tương ứng để chạy

2. model-color-format = 0/1

   - Nếu bằng 0 thì sử dụng thứ tự màu là RGB
   - Nếu bằng 1 thì sử dụng thứ tự màu là BGR

3. model-engine-file = ./{đường dẫn file}.engine

   - Đây là 1 file weight của môt mô hình nào đó đã được biên dịch sang TensorRT

4. label-file-path = ./{đường dẫn file}.txt

   - Đây là file chứa tên các class mà người dùng muốn predict

5. process-mode = 0/1

   - Process-mode = 0: Serial Mode (Chế độ tuần tự)
     - Khi process-mode được đặt thành 0, nghĩa là một khối xử lý sẽ tiếp nhận và xử lý các frame theo thứ tự tuần tự. Điều này có nghĩa là mỗi khối xử lý đang hoạt động trên một frame trước khi chuyển sang frame tiếp theo.
     - Điều này phù hợp cho các ứng dụng nơi yêu cầu sự tuần tự trong xử lý, hoặc khi có sự phụ thuộc giữa các bước xử lý.
   - Process-mode = 1: Pipeline Mode (Chế độ đường ống)
     - Khi process-mode được đặt thành 1, các khối xử lý có thể hoạt động độc lập trên các frame khác nhau cùng 1 lúc. Điều này giúp tăng hiệu suất bằng cách tận dụng được nhiều luồng xử lý và giảm độ trễ.
     - Chế độ này thích hợp cho các ứng dụng đòi hỏi xử lý đa nhiệm và tận dụng được sức mạnh của các thiết bị đa nhân.

6. network-mode = 0/1/2:
   Mục đich sử dụng để tăng cường hiệu suất của mô hình. Khi các trọng số tốn ít bộ nhớ hơn thì thực hiện các phép toán sẽ nhanh hơn đáng kể

   - network-mode = 0: sử dụng FP32
     Các trọng số của mô hình được lưu dưới dạng float point 32-bit
   - network-mode = 1: sử dụng INT8
     Các trọng số của mô hình được lưu dưới dạng int 8-bit
   - network-mode = 2: sử dụng FP16
     Các trọng số của mô hình được lưu dưới dạng float point 16-bit

7. gie-unique-id = 1
   Viết tắt là Generalized Instance Engine - GIE

   - Khi bạn có nhiều mô hình nhận diện chạy đồng thời trong một ứng dụng DeepStream, việc sử dụng gie-unique-id giúp phân biệt giữa chúng. Mỗi mô hình được khởi tạo với một gie-unique-id duy nhất, giúp hệ thống theo dõi và quản lý chúng một cách hiệu quả.
     ```
     [property]
     gpu-id=0
     ...
     num-detectors=2
     gie-unique-id=1 # Các cấu hình cho mô hình nhận diện khuôn mặt
     ...
     gie-unique-id=2 # Các cấu hình cho mô hình nhận diện đối tượng
     ...
     ```

8. network-type = 0

9. output-blob-names = prob

   - Là một tham số cấu hình được sử dụng để chỉ định tên của các lớp (layers) đầu ra trong mô hình của bạn. Trong ngữ cảnh của DeepStream và các mô hình nhận diện đối tượng, "prob" thường được sử dụng để đặt tên cho lớp đầu ra liên quan đến xác suất (probability) của các đối tượng được dự đoán.

   Ví dụ, nếu mô hình của bạn được huấn luyện để nhận diện đối tượng và dự đoán xác suất của mỗi đối tượng trong ảnh, thì lớp đầu ra có thể được đặt tên là "prob" để chỉ định xác suất dự đoán. Cụ thể, tên "prob" không phải là một quy ước cứng nhắc và có thể thay đổi tùy thuộc vào cách bạn đã đặt tên các lớp trong mô hình của mình.

   Khi bạn cấu hình output-blob-names=prob trong DeepStream, nó có nghĩa là DeepStream sẽ tìm kiếm lớp đầu ra với tên là "prob" trong mô hình của bạn để trích xuất kết quả dự đoán từ đó. Điều này quan trọng khi bạn tích hợp mô hình vào DeepStream để đảm bảo rằng kết quả dự đoán được đọc chính xác từ lớp đầu ra mong muốn của mô hình của bạn.

10. batch-size = 32

    - Số frame được load và xử lý cùng 1 lúc là 32 frames. Con số này có thể thay đổi để phù hợp với phần cứng

11. maintain-aspect-ratio = 1

    - Khi maintain-aspect-ratio được đặt thành giá trị "1" (hoặc "true"), tỷ lệ khung hình của video sẽ được giữ nguyên. Điều này có nghĩa là, nếu video đầu vào có tỷ lệ khung hình khác so với tỷ lệ khung hình mong muốn cho mô hình, hệ thống sẽ thực hiện việc thích ứng để giữ nguyên tỷ lệ khung hình.
    - Ngược lại, khi maintain-aspect-ratio được đặt thành giá trị "0" (hoặc "false"), tỷ lệ khung hình của video đầu vào có thể thay đổi khi được đưa vào mô hình.

12. num-detected-classes = 1/...
    - Số lượng class được sẽ được mô hình phát hiện
