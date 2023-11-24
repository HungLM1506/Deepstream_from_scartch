## Các thông số trong file bus_call

I. Tham só đầu vào 
    
    1. Bus:
        
    2. Message:

    3. Loop:

II. Tham số trong quá trình xử lý

    1. Gst.MessageType.EOS: (End-of-stream) - Khi một ứng dụng sử dụng GStreamer để xử lý dữ liệu đa phương tiện, việc truyền tải dữ liệu thông thường kết thúc bằng việc gửi một tin nhắn EOS. Điều này thường xảy ra khi một tệp đa phương tiện đã được chơi hết, hoặc khi một luồng dữ liệu khác có điều kiện kết thúc. Tin nhắn EOS có thể được sử dụng để báo hiệu các thành phần khác nhau trong đồ thị GStreamer để kết thúc xử lý.

        - Khi một thành phần GStreamer nhận được một tin nhắn EOS, nó có thể thực hiện các công việc cần thiết để dừng quá trình xử lý, giải phóng tài nguyên, và thông báo cho các thành phần khác trong hệ thống biết rằng quá trình đã kết thúc.

        ```
            if t == Gst.MessageType.EOS:
                sys.stdout.write("End-of-stream")
                loop.quit()
        ```

    2. Gst.MessageType.WARNING()
        - Trong GStreamer, GST_MESSAGE_WARNING là một loại tin nhắn (message type) được sử dụng để thông báo về các cảnh báo (warnings) xuất hiện trong quá trình xử lý đa phương tiện. Các cảnh báo này thường xuất hiện khi có các vấn đề không nguy hiểm hoặc không nghiêm trọng, nhưng vẫn cần được lưu ý.

        ```
        elif t == Gst.MessageType.WARNING():
            err, debug = message.parse_warining()
            sys.stderr.write("Warning: %s: %s\n" % (err, debug))
        ```

    3. Gst.MessageType.ERROR()
        - Trong GStreamer, GST_MESSAGE_ERROR là một loại tin nhắn (message type) được sử dụng để báo cáo về các lỗi xuất hiện trong quá trình xử lý đa phương tiện. Khi một thành phần trong pipeline GStreamer gặp một vấn đề nghiêm trọng, nó sẽ gửi một tin nhắn lỗi để thông báo về tình trạng đó.

        ```
            elif t == Gst.MessageType.ERROR:
                err, debug = message.parse_error()
                sys.stderr.write("Error: %s: %s\n" % (err, debug))
                loop.quit()
        ```
