## PipeLine Display_mp4

1. Gst.debug_set_active(True): sử dụng để bật chế ghi log của GStreamer. Khi giá trị bằng True, thì sẽ ghi thông tin debug để bạn có thể theo dõi quá trình thực thi của ứng dụng

2. Gst.debug_set_default_threadhold(4): Đặt ngưỡng mức debug mặc định cho GStreamer là 4. Các thông điệp debug có mức độ quan trọng dưới mức này sẽ không được ghi lại bên trong log.

3. GObject.thread_init(): Khởi tạo hệ thống thread cho thư viện GObject. Điều này là quan trọng nếu bạn đang sử dụng đa luồng trong ứng dụng của mình.

4. Gst.init(None): Hàm khởi tạo. Hàm này được gọi trước khi bạn chạy bất kì chức năng nào cửa GStreamer trong ứng dụng của mình.

5. Gst.pipeline: Khởi tạo đối tượng pipeline. Đây gồm một chuỗi các phần tử được kết nối với nhau để xử lý và chuyển đổi đối tượng da phương tiện.

6. source = create_element("filesrc", "file-source"): Khởi tạo đối tượng sourc. Đây có thể là mp4,image,h264,...

7. source.set_property('location', 'path/image'): Set thuộc tính của source.

8. sink sink = create_element("nvoverlaysink", "overlay"): Trong DeepStream, "sink" thường được sử dụng để chỉ một phần tử cuối cùng trong một đường dẫn xử lý đa phương tiện, nơi dữ liệu được đưa ra hoặc hiển thị. DeepStream là một nền tảng của NVIDIA được thiết kế để xử lý và phân tích dữ liệu video đa kênh với sự hỗ trợ mạnh mẽ từ phần cứng GPU.

   - nvoverlaysink: Sink này được sử dụng để hiển thị video trực tiếp trên màn hình sử dụng GPU overlays. Nó thường được sử dụng để hiển thị video trong các ứng dụng như camera giám sát.

   - fakesink: Sink này không hiển thị thực tế dữ liệu video mà thay vào đó loại bỏ chúng. Nó thường được sử dụng khi bạn chỉ quan tâm đến quá trình xử lý (ví dụ: để đo lường hiệu suất) mà không cần hiển thị video đầu ra.

   - filesink: Sink này được sử dụng để lưu trữ video đầu ra vào một file. Điều này thường được sử dụng để ghi lại dữ liệu video xử lý.

9. pipeline.add(source)
   pipeline.add(sink)
   --> thêm các thuộc thành phần vào pipeline

10. source.add(sink),...: Khi có nhiều thành phần trong pipeline chúng ta cần linking với nhau.
