## custom detection parser

1. custom-lib-path=/{đường đẫn file}.so

   - Trong DeepStream, tham số custom-lib-path thường được sử dụng để chỉ định đường dẫn đến thư viện (library) tùy chỉnh mà bạn muốn sử dụng trong quá trình xây dựng và triển khai ứng dụng của mình.

   - Cụ thể, tham số này có thể được sử dụng để chỉ định thư mục chứa các thư viện động (shared libraries) mà ứng dụng của bạn cần để chạy. Các thư viện này có thể bao gồm các module tùy chỉnh, plugins, hoặc các thành phần phần mềm khác mà bạn tích hợp vào hệ thống DeepStream của mình.

2. net-scale-factor = 1.0

   - Trong DeepStream, tham số net-scale-factor được sử dụng để xác định tỷ lệ mà các giá trị pixel có thể thay đổi khi được đưa vào trong mô hình đầu vào. Cụ thể, net-scale-factor là một hệ số số thực, và giá trị mặc định thường là 1.0.

   - Khi bạn thiết lập giá trị net-scale-factor khác 1.0, chẳng hạn như 0.003922 (1/255) hoặc 0.007843 (1/127.5), điều này có thể làm thay đổi tỷ lệ giá trị pixel trong ảnh đầu vào trước khi đưa vào mô hình. Điều này có thể quan trọng khi mô hình của bạn được huấn luyện với một phạm vi giá trị pixel cụ thể.

3. offsets = 104.0; 117.0; 123.0

   - Trong DeepStream, tham số offsets thường được sử dụng trong quá trình chuẩn hóa (normalization) đối với giá trị pixel của các khung hình đầu vào trước khi đưa vào mô hình học máy. Tham số này xác định giá trị được thêm vào hoặc trừ đi từ mỗi kênh màu (R, G, B) của pixel.

   - Trong trường hợp offsets = 104.0; 117.0; 123.0, giá trị này thường liên quan đến việc chuẩn hóa pixel theo giá trị trung bình của các kênh màu trong ảnh. Cụ thể:

     - 104.0 là giá trị trung bình của kênh màu đỏ (R).
     - 117.0 là giá trị trung bình của kênh màu xanh lục (G).
     - 123.0 là giá trị trung bình của kênh màu xanh dương (B).

   --> Khi áp dụng offsets này, mục đích là để làm cho giá trị pixel của ảnh thỏa mãn các yêu cầu chuẩn hóa của mô hình học máy. Một số mô hình yêu cầu đầu vào được chuẩn hóa để có giá trị trung bình gần với 0 và phương sai gần với 1 để giúp quá trình học hiệu quả hơn.

4. force-implicit-batch-dim = 0

   - Trong DeepStream, tham số force-implicit-batch-dim được sử dụng để xác định liệu mô hình học máy sử dụng kích thước batch (batch size) là 1 hoặc không. Khi force-implicit-batch-dim được đặt thành giá trị "0," điều này thường có nghĩa là mô hình không yêu cầu kích thước batch là 1.

   - Kích thước batch là số lượng dữ liệu đầu vào mà mô hình sẽ xử lý mỗi lần truyền qua mạng nơ-ron. Nếu một mô hình không yêu cầu một kích thước batch cụ thể và có thể xử lý một hình ảnh mỗi lần, thì force-implicit-batch-dim có thể được sử dụng để chỉ định điều này.

5. interval=0
   - Trong DeepStream, tham số interval thường được sử dụng để xác định tần suất của quá trình xử lý. Khi interval được đặt thành giá trị "0," điều này thường có nghĩa là quá trình xử lý sẽ được thực hiện cho mỗi khung hình mà không có sự chờ đợi giữa các khung hình liên tiếp.
   - Lưu ý rằng giá trị cụ thể của interval có thể phụ thuộc vào yêu cầu cụ thể của ứng dụng hoặc mô hình và cách mà quá trình xử lý được tổ chức trong pipeline DeepStream của bạn.
