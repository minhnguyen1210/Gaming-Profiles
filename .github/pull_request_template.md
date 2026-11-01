## Thay đổi gì

<!-- 1–3 câu: PR này làm gì, thuộc phase / câu hỏi nào. Ví dụ: "Phase 2: khám phá bảng history của 3 nền tảng." -->

Liên quan issue: #

## Người mở PR tự kiểm tra

- [ ] Notebook đã *Restart & Run All*, chạy hết từ trên xuống không lỗi
- [ ] Không có file dữ liệu (`data/`, `.csv`, `.parquet`…) và không có đường dẫn tuyệt đối
- [ ] In số dòng sau mỗi bước làm thay đổi dữ liệu (lọc, merge, xoá) và giải thích thay đổi
- [ ] Biểu đồ có tiêu đề, nhãn trục, đơn vị, chú thích
- [ ] Commit message đúng quy ước `<scope>: <tóm tắt>`, không có dòng ghi công AI
- [ ] Quyết định dùng chung (nếu có) đã ghi vào `docs/DECISIONS.md`
- [ ] Đã ghi `LLM_USAGE.md` nếu có dùng công cụ AI
- [ ] Thư viện mới (nếu có) đã thêm vào `environment.yml`

## Người review kiểm tra

- [ ] Tôi hiểu và tự giải thích được code trong PR này (đủ để trả lời Q&A)
- [ ] Kết luận khớp với số liệu; câu trả lời có con số cụ thể
- [ ] Câu non-ML: dùng rõ ràng ≥ 2 tiêu chí D1–D6 · Câu ML: đủ 6 yêu cầu của đề
