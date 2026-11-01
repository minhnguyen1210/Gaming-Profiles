# Nhật ký quyết định

> Ghi lại mọi quyết định mà **cả hai** cần làm theo, để hai notebook không xử lý cùng một dữ liệu theo hai cách khác nhau,
> và để khi Q&A ai cũng trả lời được "vì sao nhóm chọn như vậy".
> Quy trình: một người đề xuất (qua PR hoặc khi họp) → người kia đồng ý → ghi một dòng vào bảng. Không xoá dòng cũ;
> nếu đổi ý thì thêm dòng mới và ghi "thay cho #…".

## Cần ghi những gì

- Quy tắc làm sạch dùng chung: bỏ game thử nghiệm (playtest, beta), xử lý giá trị thiếu, chuẩn hoá nhãn thể loại…
- Ngưỡng và tham số: ngưỡng outlier, khoảng thời gian phân tích, số tối thiểu để giữ một nhóm…
- Phạm vi: nền tảng, bảng, cột nào dùng hay bỏ.
- Chốt câu hỏi, người sở hữu, tiêu chí D1–D6.
- Thay đổi môi trường, công cụ, quy trình.

## Bảng quyết định

| # | Ngày | Quyết định | Lý do | Ảnh hưởng tới | Đề xuất | Đồng ý |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-01 | Dùng **phiên bản 1** của dataset trên Kaggle (cập nhật 2025-02-25); script tải dữ liệu chốt phiên bản này | Tác giả ghi dataset "Regularly Updated"; chốt phiên bản để hai người và người chấm phân tích cùng một dữ liệu | toàn bộ | A | ⏳ B |
| 2 | 2026-11-01 | Môi trường: Python 3.11, pandas 2.3, chỉ dùng kênh conda-forge, phiên bản ghi đầy đủ trong `environment.yml` | Cùng dòng Python với môn học; pandas 2 có nhiều tài liệu hơn pandas 3; tái lập được | toàn bộ | A | ⏳ B |
| 3 | 2026-11-01 | Không commit dữ liệu; bảng trung gian tạo bằng code, lưu vào `data/processed/` | Dữ liệu 4 GB, GitHub chặn file > 100 MB; tái lập bằng script | toàn bộ | A | ⏳ B |
| 4 | 2026-11-01 | File bắt buộc nộp viết tiếng Anh; file nội bộ (quy trình, kế hoạch, nhật ký) viết tiếng Việt | Người chấm đọc file nộp; nội bộ cần rõ ràng cho cả hai | tài liệu | A | ⏳ B |
| 5 | 2026-11-01 | AI không thao tác Git, không có dấu vết AI trong Git history; bật hook `.githooks/commit-msg` | Điểm cá nhân dựa trên Git history; đề chỉ cho dùng AI như gia sư | Git | A | ⏳ B |
